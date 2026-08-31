from ...coresight.coresight_target import CoreSightTarget
from ...core.memory_map import FlashRegion, RamRegion, MemoryMap

from .flash_algos_gd32f30x.flash_algo_cl import FLASH_ALGO as FLASH_ALGO_GD32F30x_CL
from .flash_algos_gd32f30x.flash_algo_hd import FLASH_ALGO as FLASH_ALGO_GD32F30x_HD
from .flash_algos_gd32f30x.flash_algo_xd import FLASH_ALGO as FLASH_ALGO_GD32F30x_XD


class _GD32F30xBase(CoreSightTarget):
    VENDOR = "GigaDevice"
    def __init__(self, session):
        super().__init__(session, self.MEMORY_MAP)


def _mk(clazz, algo, fsize, rsize):
    return type(clazz, (_GD32F30xBase,), {
        "MEMORY_MAP": MemoryMap(
            FlashRegion(start=0x08000000, length=fsize,
                        blocksize=0x400 if algo != FLASH_ALGO_GD32F30x_XD else 0x800,
                        is_boot_memory=True, algo=algo),
            RamRegion(start=0x20000000, length=rsize),
        ),
        "__module__": __name__,
    })


GD32F303RC = _mk("GD32F303RC", FLASH_ALGO_GD32F30x_HD, 0x040000, 0x0C000)
GD32F303RE = _mk("GD32F303RE", FLASH_ALGO_GD32F30x_HD, 0x080000, 0x010000)
GD32F303RG = _mk("GD32F303RG", FLASH_ALGO_GD32F30x_XD, 0x100000, 0x018000)
GD32F303RI = _mk("GD32F303RI", FLASH_ALGO_GD32F30x_XD, 0x200000, 0x018000)
GD32F303RK = _mk("GD32F303RK", FLASH_ALGO_GD32F30x_XD, 0x300000, 0x018000)
GD32F305RC = _mk("GD32F305RC", FLASH_ALGO_GD32F30x_CL, 0x040000, 0x018000)
GD32F305RE = _mk("GD32F305RE", FLASH_ALGO_GD32F30x_CL, 0x080000, 0x018000)
GD32F305RG = _mk("GD32F305RG", FLASH_ALGO_GD32F30x_CL, 0x100000, 0x018000)
GD32F307RC = _mk("GD32F307RC", FLASH_ALGO_GD32F30x_CL, 0x040000, 0x018000)
GD32F307RE = _mk("GD32F307RE", FLASH_ALGO_GD32F30x_CL, 0x080000, 0x018000)
GD32F307RG = _mk("GD32F307RG", FLASH_ALGO_GD32F30x_CL, 0x100000, 0x018000)

__all__ = ['GD32F303RC', 'GD32F303RE', 'GD32F303RG', 'GD32F303RI', 'GD32F303RK',
           'GD32F305RC', 'GD32F305RE', 'GD32F305RG',
           'GD32F307RC', 'GD32F307RE', 'GD32F307RG']
