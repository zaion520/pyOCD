from ...coresight.coresight_target import CoreSightTarget
from ...core.memory_map import FlashRegion, RamRegion, MemoryMap

from .flash_algos_at32f421.flash_algo_at32f421_64 import FLASH_ALGO as FLASH_ALGO_AT32F421_64
from .flash_algos_at32f421.flash_algo_at32f421_32 import FLASH_ALGO as FLASH_ALGO_AT32F421_32
from .flash_algos_at32f421.flash_algo_at32f421_16 import FLASH_ALGO as FLASH_ALGO_AT32F421_16


class _AT32F421Base(CoreSightTarget):
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


class AT32F421C8T7(_AT32F421Base):
    MEMORY_MAP = MemoryMap(
        FlashRegion(start=0x08000000, length=0x10000, page_size=0x400, sector_size=0x400,
                    is_boot_memory=True, algo=FLASH_ALGO_AT32F421_64),
        RamRegion(start=0x20000000, length=0x4000),
    )

class AT32F421C6T7(_AT32F421Base):
    MEMORY_MAP = MemoryMap(
        FlashRegion(start=0x08000000, length=0x8000, page_size=0x400, sector_size=0x400,
                    is_boot_memory=True, algo=FLASH_ALGO_AT32F421_32),
        RamRegion(start=0x20000000, length=0x4000),
    )

class AT32F421C4T7(_AT32F421Base):
    MEMORY_MAP = MemoryMap(
        FlashRegion(start=0x08000000, length=0x4000, page_size=0x400, sector_size=0x400,
                    is_boot_memory=True, algo=FLASH_ALGO_AT32F421_16),
        RamRegion(start=0x20000000, length=0x2000),
    )

__all__ = ['AT32F421C8T7', 'AT32F421C6T7', 'AT32F421C4T7']
