from ...coresight.coresight_target import CoreSightTarget
from ...core.memory_map import FlashRegion, RamRegion, MemoryMap

from .flash_algos_at32.flash_algo_at32f403a_256 import FLASH_ALGO as FLASH_ALGO_AT32F403A_256
from .flash_algos_at32.flash_algo_at32f403a_512 import FLASH_ALGO as FLASH_ALGO_AT32F403A_512
from .flash_algos_at32.flash_algo_at32f403a_1024 import FLASH_ALGO as FLASH_ALGO_AT32F403A_1024
from .flash_algos_at32.flash_algo_at32f407_256 import FLASH_ALGO as FLASH_ALGO_AT32F407_256
from .flash_algos_at32.flash_algo_at32f407_512 import FLASH_ALGO as FLASH_ALGO_AT32F407_512
from .flash_algos_at32.flash_algo_at32f407_1024 import FLASH_ALGO as FLASH_ALGO_AT32F407_1024

from .flash_algos_at32.flash_algo_at32_ext_type1_remap0 import FLASH_ALGO as FLASH_ALGO_AT32_EXT_TYPE1_REMAP0
from .flash_algos_at32.flash_algo_at32_ext_type1_remap1 import FLASH_ALGO as FLASH_ALGO_AT32_EXT_TYPE1_REMAP1
from .flash_algos_at32.flash_algo_at32_ext_type2_remap0 import FLASH_ALGO as FLASH_ALGO_AT32_EXT_TYPE2_REMAP0
from .flash_algos_at32.flash_algo_at32_ext_type2_remap1 import FLASH_ALGO as FLASH_ALGO_AT32_EXT_TYPE2_REMAP1

SPIM_ALGO_MAP = {
    'type1_remap0': FLASH_ALGO_AT32_EXT_TYPE1_REMAP0,
    'type1_reamp0': FLASH_ALGO_AT32_EXT_TYPE1_REMAP0,
    'type1_remap1': FLASH_ALGO_AT32_EXT_TYPE1_REMAP1,
    'type1_reamp1': FLASH_ALGO_AT32_EXT_TYPE1_REMAP1,
    'type2_remap0': FLASH_ALGO_AT32_EXT_TYPE2_REMAP0,
    'type2_reamp0': FLASH_ALGO_AT32_EXT_TYPE2_REMAP0,
    'type2_remap1': FLASH_ALGO_AT32_EXT_TYPE2_REMAP1,
    'type2_reamp1': FLASH_ALGO_AT32_EXT_TYPE2_REMAP1,
    'type1': FLASH_ALGO_AT32_EXT_TYPE1_REMAP1,
    'type2': FLASH_ALGO_AT32_EXT_TYPE2_REMAP1,
}

# Default SPIM algorithm (evaluation boards AT-START-F403A / AT-START-F407 standard: QSPI Type 2, REMAP 1)
FLASH_ALGO_SPIM_DEFAULT = FLASH_ALGO_AT32_EXT_TYPE2_REMAP1


class _AT32Base(CoreSightTarget):
    VENDOR = "ArteryTek"

    def __init__(self, session):
        if not session.options.is_set("frequency"):
            session.options.set("frequency", 5000000)
        if not session.options.is_set("chip_erase"):
            session.options.set("chip_erase", "chip")
        if not session.options.is_set("fast_program"):
            session.options.set("fast_program", True)

        memory_map = self.MEMORY_MAP.clone()

        # Check for user-selected external flash (SPIM) algorithm option
        spim_opt = session.options.get("at32.spim_algo")
        if spim_opt:
            normalized_opt = str(spim_opt).strip().lower().replace("-", "_")
            if normalized_opt in SPIM_ALGO_MAP:
                spim_algo = SPIM_ALGO_MAP[normalized_opt]
                spim_region = memory_map.get_first_matching_region(name="spim")
                if spim_region and isinstance(spim_region, FlashRegion):
                    spim_region.algo = spim_algo

        super().__init__(session, memory_map)


class AT32F403ACCT7(_AT32Base):
    MEMORY_MAP = MemoryMap(
        FlashRegion(name="internal_flash", start=0x08000000, length=0x00040000, page_size=0x400, sector_size=0x800,
                    is_boot_memory=True, algo=FLASH_ALGO_AT32F403A_256),
        FlashRegion(name="spim", start=0x08400000, length=0x01000000, page_size=0x400, sector_size=0x1000,
                    is_boot_memory=False, is_external=True, algo=FLASH_ALGO_SPIM_DEFAULT),
        RamRegion(start=0x20000000, length=0x18000),
    )

class AT32F403ACET7(_AT32Base):
    MEMORY_MAP = MemoryMap(
        FlashRegion(name="internal_flash", start=0x08000000, length=0x00080000, page_size=0x400, sector_size=0x800,
                    is_boot_memory=True, algo=FLASH_ALGO_AT32F403A_512),
        FlashRegion(name="spim", start=0x08400000, length=0x01000000, page_size=0x400, sector_size=0x1000,
                    is_boot_memory=False, is_external=True, algo=FLASH_ALGO_SPIM_DEFAULT),
        RamRegion(start=0x20000000, length=0x18000),
    )

class AT32F403ACGT7(_AT32Base):
    MEMORY_MAP = MemoryMap(
        FlashRegion(name="internal_flash", start=0x08000000, length=0x00100000, page_size=0x400, sector_size=0x800,
                    is_boot_memory=True, algo=FLASH_ALGO_AT32F403A_1024),
        FlashRegion(name="spim", start=0x08400000, length=0x01000000, page_size=0x400, sector_size=0x1000,
                    is_boot_memory=False, is_external=True, algo=FLASH_ALGO_SPIM_DEFAULT),
        RamRegion(start=0x20000000, length=0x18000),
    )

class AT32F407RCT7(_AT32Base):
    MEMORY_MAP = MemoryMap(
        FlashRegion(name="internal_flash", start=0x08000000, length=0x00040000, page_size=0x400, sector_size=0x800,
                    is_boot_memory=True, algo=FLASH_ALGO_AT32F407_256),
        FlashRegion(name="spim", start=0x08400000, length=0x01000000, page_size=0x400, sector_size=0x1000,
                    is_boot_memory=False, is_external=True, algo=FLASH_ALGO_SPIM_DEFAULT),
        RamRegion(start=0x20000000, length=0x18000),
    )

class AT32F407RET7(_AT32Base):
    MEMORY_MAP = MemoryMap(
        FlashRegion(name="internal_flash", start=0x08000000, length=0x00080000, page_size=0x400, sector_size=0x800,
                    is_boot_memory=True, algo=FLASH_ALGO_AT32F407_512),
        FlashRegion(name="spim", start=0x08400000, length=0x01000000, page_size=0x400, sector_size=0x1000,
                    is_boot_memory=False, is_external=True, algo=FLASH_ALGO_SPIM_DEFAULT),
        RamRegion(start=0x20000000, length=0x18000),
    )

class AT32F407RGT7(_AT32Base):
    MEMORY_MAP = MemoryMap(
        FlashRegion(name="internal_flash", start=0x08000000, length=0x00100000, page_size=0x400, sector_size=0x800,
                    is_boot_memory=True, algo=FLASH_ALGO_AT32F407_1024),
        FlashRegion(name="spim", start=0x08400000, length=0x01000000, page_size=0x400, sector_size=0x1000,
                    is_boot_memory=False, is_external=True, algo=FLASH_ALGO_SPIM_DEFAULT),
        RamRegion(start=0x20000000, length=0x18000),
    )

__all__ = ['AT32F403ACCT7', 'AT32F403ACET7', 'AT32F403ACGT7',
           'AT32F407RCT7', 'AT32F407RET7', 'AT32F407RGT7',
           'SPIM_ALGO_MAP']
