from ...coresight.coresight_target import CoreSightTarget
from ...core.memory_map import FlashRegion, RamRegion, MemoryMap

from .flash_algos_n32wb03x.flash_algo_n32wb03x import FLASH_ALGO as FLASH_ALGO_N32WB03X

class _N32WB03xBase(CoreSightTarget):
    VENDOR = "Nations Technologies"

    def __init__(self, session):
        super().__init__(session, self.MEMORY_MAP)

def _mk(clazz, fsize, rsize):
    return type(clazz, (_N32WB03xBase,), {
        "MEMORY_MAP": MemoryMap(
            FlashRegion(start=0x08000000, length=fsize, page_size=0x200, sector_size=0x200,
                        is_boot_memory=True, algo=FLASH_ALGO_N32WB03X),
            RamRegion(start=0x20000000, length=rsize),
        ),
        "__module__": __name__,
    })

N32WB031 = _mk("N32WB031", 0x20000, 0x4000)
N32WB031KCQ6_1 = _mk("N32WB031KCQ6_1", 0x40000, 0x4000)
N32WB031KEQ6_2 = _mk("N32WB031KEQ6_2", 0x40000, 0x8000)

__all__ = ['N32WB031', 'N32WB031KCQ6_1', 'N32WB031KEQ6_2']
