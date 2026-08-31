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
    0xf36f4964, 0x44490012, 0x48636008, 0x60012100, 0x60414962, 0x60424a62, 0x64426441, 0x074069c0,
    0x4860d408, 0x5155f245, 0x21066001, 0xf6406041, 0x608171ff, 0x47702000, 0x69014857, 0x0180f041,
    0x6d016101, 0x0180f041, 0x20006501, 0x48524770, 0xf0416901, 0x61010104, 0xf0416901, 0x61010140,
    0x21aaf64a, 0xe0004a4f, 0x68c36011, 0xd1fb07db, 0xf0236903, 0x61030304, 0xf0436d03, 0x65030304,
    0xf0436d03, 0x65030340, 0x6011e000, 0x07db6cc3, 0x6d01d1fb, 0x0104f021, 0x20006501, 0x493d4770,
    0x4449b510, 0x680c4b3c, 0xf504493e, 0xf64a2400, 0x42a022aa, 0x691cd212, 0x0402f044, 0x6158611c,
    0xf0406918, 0x61180040, 0x600ae000, 0x07c068d8, 0x6918d1fb, 0x0002f020, 0xe0116118, 0xf0446d1c,
    0x651c0402, 0x6d186558, 0x0040f040, 0xe0006518, 0x6cd8600a, 0xd1fb07c0, 0xf0206d18, 0x65180002,
    0xbd102000, 0xb5104b23, 0x1cc9444b, 0x4b22681c, 0x2400f504, 0x0103f021, 0xd31942a0, 0x691ce035,
    0x0401f044, 0x6814611c, 0x68dc6004, 0xd1fc07e4, 0xf024691c, 0x611c0401, 0xf01468dc, 0xd0040f14,
    0xf04068d8, 0x60d80014, 0x1d00e01a, 0x1f091d12, 0xd1e42900, 0x6d1ce01b, 0x0401f044, 0x6814651c,
    0x6cdc6004, 0xd1fc07e4, 0xf0246d1c, 0x651c0401, 0xf0146cdc, 0xd0050f14, 0xf0406cd8, 0x64d80014,
    0xbd102001, 0x1d121d00, 0x29001f09, 0x2000d1e3, 0x0000bd10, 0x00000004, 0x40022000, 0x45670123,
    0xcdef89ab, 0x40003000, 0x00000000, 0x00000000
    ],

    # Relative function addresses
    'pc_init': 0x20000005,
    'pc_unInit': 0x2000003d,
    'pc_program_page': 0x20000109,
    'pc_erase_sector': 0x200000a3,
    'pc_eraseAll': 0x20000053,

    'static_base' : 0x20000000 + 0x00000004 + 0x000001a8,
    'begin_stack' : 0x200049c0,
    'end_stack' : 0x20001200,
    'page_size' : 0x800,
    'analyzer_supported' : False,
    'analyzer_address' : 0x00000000,
    # Enable double buffering
    'page_buffers' : [
        0x200001c0,
        0x200009c0
    ],
    'min_program_length' : 0x800,

    # Relative region addresses and sizes
    'ro_start': 0x4,
    'ro_size': 0x1a8,
    'rw_start': 0x1ac,
    'rw_size': 0x8,
    'zi_start': 0x1b4,
    'zi_size': 0x0,

    # Flash information
    'flash_start': 0x8000000,
    'flash_size': 0x300000,
    'sector_sizes': (
        (0x0, 0x800),
    )
}
