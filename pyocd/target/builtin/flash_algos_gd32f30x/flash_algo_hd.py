# pyOCD debugger
# Copyright (c) 2026 PyOCD Authors
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

FLASH_ALGO = {
    'load_address' : 0x20000000,

    # Flash algorithm as a hex string
    'instructions': [
    0xe7fdbe00,
    0xf36f4939, 0x44490012, 0x48386008, 0x60012100, 0x60414937, 0x60414937, 0x074069c0, 0x4836d408,
    0x5155f245, 0x21066001, 0xf6406041, 0x608171ff, 0x47702000, 0x6901482d, 0x0180f041, 0x20006101,
    0x482a4770, 0xf0416901, 0x61010104, 0xf0416901, 0x61010140, 0x21aaf64a, 0xe0004a27, 0x68c36011,
    0xd1fb07db, 0xf0216901, 0x61010104, 0x47702000, 0x690a491e, 0x0202f042, 0x6148610a, 0xf0406908,
    0x61080040, 0x20aaf64a, 0xe0004a1b, 0x68cb6010, 0xd1fb07db, 0xf0206908, 0x61080002, 0x47702000,
    0x1cc9b510, 0x0103f021, 0xe0194b10, 0xf044691c, 0x611c0401, 0x60046814, 0x07e468dc, 0x691cd1fc,
    0x0401f024, 0x68dc611c, 0x0f14f014, 0x68d8d005, 0x0014f040, 0x200160d8, 0x1d00bd10, 0x1f091d12,
    0xd1e32900, 0xbd102000, 0x00000004, 0x40022000, 0x45670123, 0xcdef89ab, 0x40003000, 0x00000000,
    0x00000000
    ],

    # Relative function addresses
    'pc_init': 0x20000005,
    'pc_unInit': 0x20000039,
    'pc_program_page': 0x200000a5,
    'pc_erase_sector': 0x20000075,
    'pc_eraseAll': 0x20000047,

    'static_base' : 0x20000000 + 0x00000004 + 0x000000fc,
    'begin_stack' : 0x20004910,
    'end_stack' : 0x20000a00,
    'page_size' : 0x400,
    'analyzer_supported' : False,
    'analyzer_address' : 0x00000000,
    # Enable double buffering
    'page_buffers' : [
        0x20000110,
        0x20000510
    ],
    'min_program_length' : 0x400,

    # Relative region addresses and sizes
    'ro_start': 0x4,
    'ro_size': 0xfc,
    'rw_start': 0x100,
    'rw_size': 0x8,
    'zi_start': 0x108,
    'zi_size': 0x0,

    # Flash information
    'flash_start': 0x8000000,
    'flash_size': 0x80000,
    'sector_sizes': (
        (0x0, 0x800),
    )
}
