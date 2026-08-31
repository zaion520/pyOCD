from ...coresight.coresight_target import CoreSightTarget
from ...core.memory_map import FlashRegion, RamRegion, MemoryMap

from .flash_algos_n32g003.flash_algo_n32g003x import FLASH_ALGO as FLASH_ALGO_N32G003

class _N32G003Base(CoreSightTarget):
    VENDOR = "Nations Technologies"

    def __init__(self, session):
        super().__init__(session, self.MEMORY_MAP)

def _mk(clazz, fsize):
    return type(clazz, (_N32G003Base,), {
        "MEMORY_MAP": MemoryMap(
            FlashRegion(start=0x08000000, length=fsize, page_size=0x200, sector_size=0x200,
                        is_boot_memory=True, algo=FLASH_ALGO_N32G003),
            RamRegion(start=0x1FFFF800, length=0x800),
            RamRegion(start=0x20000000, length=0x1000),
        ),
        "__module__": __name__,
    })

N32G003F5 = _mk("N32G003F5", 0x7600)
N32G003F4 = _mk("N32G003F4", 0x4000)

__all__ = ['N32G003F5', 'N32G003F4']
