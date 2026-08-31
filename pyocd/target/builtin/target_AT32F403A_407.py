from ...coresight.coresight_target import CoreSightTarget
from ...core.memory_map import FlashRegion, RamRegion, MemoryMap

from .flash_algos_at32.flash_algo_at32f403a_256 import FLASH_ALGO as FLASH_ALGO_AT32F403A_256
from .flash_algos_at32.flash_algo_at32f403a_512 import FLASH_ALGO as FLASH_ALGO_AT32F403A_512
from .flash_algos_at32.flash_algo_at32f403a_1024 import FLASH_ALGO as FLASH_ALGO_AT32F403A_1024
from .flash_algos_at32.flash_algo_at32f407_256 import FLASH_ALGO as FLASH_ALGO_AT32F407_256
from .flash_algos_at32.flash_algo_at32f407_512 import FLASH_ALGO as FLASH_ALGO_AT32F407_512
from .flash_algos_at32.flash_algo_at32f407_1024 import FLASH_ALGO as FLASH_ALGO_AT32F407_1024

class _AT32Base(CoreSightTarget):
    VENDOR = "ArteryTek"

    def __init__(self, session):
        if not session.options.is_set("frequency"):
            session.options.set("frequency", 5000000)
        if not session.options.is_set("chip_erase"):
            session.options.set("chip_erase", "chip")
        if not session.options.is_set("fast_program"):
            session.options.set("fast_program", True)
        if not session.options.is_set("flash.skip_external"):
            session.options.set("flash.skip_external", True)
        super().__init__(session, self.MEMORY_MAP)


class AT32F403ACCT7(_AT32Base):
    MEMORY_MAP = MemoryMap(
        FlashRegion(start=0x08000000, length=0x00040000, page_size=0x400, sector_size=0x800,
                    is_boot_memory=True, algo=FLASH_ALGO_AT32F403A_256),
        RamRegion(start=0x20000000, length=0x18000),
    )

class AT32F403ACET7(_AT32Base):
    MEMORY_MAP = MemoryMap(
        FlashRegion(start=0x08000000, length=0x00080000, page_size=0x400, sector_size=0x800,
                    is_boot_memory=True, algo=FLASH_ALGO_AT32F403A_512),
        RamRegion(start=0x20000000, length=0x18000),
    )

class AT32F403ACGT7(_AT32Base):
    MEMORY_MAP = MemoryMap(
        FlashRegion(start=0x08000000, length=0x00100000, page_size=0x400, sector_size=0x800,
                    is_boot_memory=True, algo=FLASH_ALGO_AT32F403A_1024),
        RamRegion(start=0x20000000, length=0x18000),
    )

class AT32F407RCT7(_AT32Base):
    MEMORY_MAP = MemoryMap(
        FlashRegion(start=0x08000000, length=0x00040000, page_size=0x400, sector_size=0x800,
                    is_boot_memory=True, algo=FLASH_ALGO_AT32F407_256),
        RamRegion(start=0x20000000, length=0x18000),
    )

class AT32F407RET7(_AT32Base):
    MEMORY_MAP = MemoryMap(
        FlashRegion(start=0x08000000, length=0x00080000, page_size=0x400, sector_size=0x800,
                    is_boot_memory=True, algo=FLASH_ALGO_AT32F407_512),
        RamRegion(start=0x20000000, length=0x18000),
    )

class AT32F407RGT7(_AT32Base):
    MEMORY_MAP = MemoryMap(
        FlashRegion(start=0x08000000, length=0x00100000, page_size=0x400, sector_size=0x800,
                    is_boot_memory=True, algo=FLASH_ALGO_AT32F407_1024),
        RamRegion(start=0x20000000, length=0x18000),
    )

__all__ = ['AT32F403ACCT7', 'AT32F403ACET7', 'AT32F403ACGT7',
           'AT32F407RCT7', 'AT32F407RET7', 'AT32F407RGT7']
