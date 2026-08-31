# pyOCD debugger
# Copyright (c) 2026 NationsTech
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
    0x4603b510, 0x4018484d, 0x444c4c4d, 0x20006020, 0x60204c4c, 0x69004620, 0x40202480, 0xd0042800,
    0x4c484849, 0x48496060, 0x48466060, 0x240469c0, 0x28004020, 0x4846d106, 0x60204c46, 0x60602006,
    0x60a04845, 0xbd102000, 0x483e4601, 0x22806900, 0x4a3c4310, 0x20006110, 0x483a4770, 0x21046900,
    0x49384308, 0x46086108, 0x21406900, 0x49354308, 0xe0026108, 0x49374839, 0x48326008, 0x07c068c0,
    0x28000fc0, 0x482fd1f6, 0x21046900, 0x492d4388, 0x20006108, 0x46014770, 0x6900482a, 0x43102202,
    0x61104a28, 0x61414610, 0x22406900, 0x4a254310, 0xe0026110, 0x4a274829, 0x48226010, 0x07c068c0,
    0x28000fc0, 0x481fd1f6, 0x22026900, 0x4a1d4390, 0x20006110, 0xb5104770, 0x48204603, 0x60204c1d,
    0x08411c48, 0xe0240049, 0x69004816, 0x43202401, 0x61204c14, 0x60186810, 0x4812bf00, 0x07c068c0,
    0x28000fc0, 0x480fd1f9, 0x08406900, 0x4c0d0040, 0x46206120, 0x241468c0, 0x28004020, 0x4809d006,
    0x432068c0, 0x60e04c07, 0xbd102001, 0x1d121d1b, 0x29001f09, 0x2000d1d8, 0x0000e7f7, 0xffff8a00,
    0x00000004, 0x40022000, 0x45670123, 0xcdef89ab, 0x00005555, 0x40002c00, 0x00000fff, 0x0000aaaa,
    0x00000000, 0x00000000
    ],

    # Relative function addresses
    'pc_init': 0x20000005,
    'pc_unInit': 0x2000004d,
    'pc_program_page': 0x200000db,
    'pc_erase_sector': 0x2000009b,
    'pc_eraseAll': 0x2000005f,

    'static_base' : 0x20000000 + 0x00000004 + 0x00000160,
    'begin_stack' : 0x20001570,
    'end_stack' : 0x20000600,
    'page_size' : 0x200,
    'analyzer_supported' : False,
    'analyzer_address' : 0x00000000,
    # Enable double buffering
    'page_buffers' : [
        0x20000170,
        0x20000370
    ],
    'min_program_length' : 0x200,

    # Relative region addresses and sizes
    'ro_start': 0x4,
    'ro_size': 0x160,
    'rw_start': 0x164,
    'rw_size': 0x8,
    'zi_start': 0x16c,
    'zi_size': 0x0,

    # Flash information
    'flash_start': 0x8000000,
    'flash_size': 0x7600,
    'sector_sizes': (
        (0x0, 0x200),
    )
}
