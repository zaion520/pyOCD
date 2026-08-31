# pyOCD debugger
# Copyright (c) 2026 PyOCD Authors
# SPDX-License-Identifier: Apache-2.0

from ...coresight.coresight_target import CoreSightTarget
from ...core.memory_map import FlashRegion, RamRegion, MemoryMap

from .flash_algos_mh2457.flash_algo_MH2457 import FLASH_ALGO as FLASH_ALGO_MH2457


class MH2457(CoreSightTarget):
    VENDOR = "MegaHunt"
    
    MEMORY_MAP = MemoryMap(
        FlashRegion(
            start=0x08000000,
            length=0x4000000,
            blocksize=0x1000,
            is_boot_memory=True,
            algo=FLASH_ALGO_MH2457,
        ),
        RamRegion(start=0x20000000, length=0x00080000),
    )

    def __init__(self, session):
        super().__init__(session, self.MEMORY_MAP)
