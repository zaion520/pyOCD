# pyOCD debugger
# Copyright (c) 2026 Arm Limited
# SPDX-License-Identifier: Apache-2.0
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from unittest import mock

import pytest

from pyocd.probe.pydapaccess import dap_access_cmsis_dap as dap
from pyocd.probe.pydapaccess.dap_access_api import DAPAccessIntf


class FakeInterface:
    """@brief Minimal stand-in for a CMSIS-DAP USB interface."""

    def __init__(self, serial, fail_open=False, is_bulk=False):
        self.serial_number = serial
        self.vid = 0x1234
        self.pid = 0x5678
        self.vendor_name = "Vendor"
        self.product_name = "Product"
        self.fallback_v1 = None
        self.is_bulk = is_bulk
        self._fail_open = fail_open
        self.opened = False

    def get_serial_number(self):
        return self.serial_number

    def open(self):
        if self._fail_open:
            raise DAPAccessIntf.DeviceError(f"simulated open failure for {self.serial_number}")
        self.opened = True

    def close(self):
        self.opened = False


class FakeBackend:
    """@brief Returns a fixed list of fake interfaces."""

    def __init__(self, interfaces):
        self._interfaces = interfaces

    def get_all_connected_interfaces(self):
        return list(self._interfaces)


def _install_fake_backends(monkeypatch, v1_interfaces, v2_interfaces):
    monkeypatch.setattr(dap, "INTERFACE", {
        "fake_v1": FakeBackend(v1_interfaces),
        "fake_v2": FakeBackend(v2_interfaces),
        })
    monkeypatch.setattr(dap, "USB_BACKEND", "fake_v1")
    monkeypatch.setattr(dap, "USB_BACKEND_V2", "fake_v2")


class TestGetInterfacesFallback:
    def test_v2_interfaces_get_v1_fallback(self, monkeypatch):
        v1a, v1b = FakeInterface("AAA"), FakeInterface("BBB")
        v2a, v2b = FakeInterface("AAA", is_bulk=True), FakeInterface("BBB", is_bulk=True)
        _install_fake_backends(monkeypatch, [v1a, v1b], [v2a, v2b])

        result = dap._get_interfaces()

        # Each v2 interface points at its matching v1 interface.
        assert v2a.fallback_v1 is v1a
        assert v2b.fallback_v1 is v1b
        # The v1 interfaces are still removed from the returned list.
        assert set(result) == {v2a, v2b}

    def test_no_fallback_when_prefer_v1(self, monkeypatch):
        v1a = FakeInterface("AAA")
        v2a = FakeInterface("AAA", is_bulk=True)
        _install_fake_backends(monkeypatch, [v1a], [v2a])

        fake_session = mock.Mock(options={"cmsis_dap.prefer_v1": True})
        monkeypatch.setattr(dap.session.Session, "get_current", classmethod(lambda cls: fake_session))

        result = dap._get_interfaces()

        # With prefer_v1, v2 is dropped and no fallback is set.
        assert v2a.fallback_v1 is None
        assert result == [v1a]

    def test_no_fallback_when_only_v2_present(self, monkeypatch):
        v2a = FakeInterface("AAA", is_bulk=True)
        _install_fake_backends(monkeypatch, [], [v2a])

        result = dap._get_interfaces()

        assert v2a.fallback_v1 is None
        assert result == [v2a]


class TestOpenFallback:
    def _make_device(self, interface):
        # Skip the rest of open(), which talks to the probe, by pretending the probe was
        # already examined once. _has_swo_uart is set because open() reads it in that path.
        dev = dap.DAPAccessCMSISDAP("SER123", interface=interface)
        dev._has_opened_once = True
        dev._has_swo_uart = False
        return dev

    def test_v2_falls_back_to_v1_on_open_failure(self):
        v1 = FakeInterface("SER123")
        v2 = FakeInterface("SER123", fail_open=True, is_bulk=True)
        v2.fallback_v1 = v1
        dev = self._make_device(v2)

        dev.open()

        assert dev._interface is v1
        assert dev._protocol.interface is v1
        assert v1.opened
        assert dev.is_open

    def test_open_failure_without_fallback_propagates(self):
        v2 = FakeInterface("SER123", fail_open=True, is_bulk=True)
        dev = self._make_device(v2)

        with pytest.raises(DAPAccessIntf.DeviceError):
            dev.open()

        # The original interface is retained and the probe is not marked open.
        assert dev._interface is v2
        assert not dev.is_open

    def test_v2_and_v1_both_fail_reports_both(self):
        v1 = FakeInterface("SER123", fail_open=True)
        v2 = FakeInterface("SER123", fail_open=True, is_bulk=True)
        v2.fallback_v1 = v1
        dev = self._make_device(v2)

        with pytest.raises(DAPAccessIntf.DeviceError) as exc_info:
            dev.open()

        message = str(exc_info.value)
        assert "v2" in message and "v1" in message
        assert not dev.is_open
