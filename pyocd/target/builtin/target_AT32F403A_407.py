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
}


class _AT32Base(CoreSightTarget):
    VENDOR = "ArteryTek"

    def __init__(self, session):
        if not session.options.is_set("frequency"):
            session.options.set("frequency", 5000000)
        if not session.options.is_set("chip_erase"):
            session.options.set("chip_erase", "chip")
        if not session.options.is_set("fast_program"):
            session.options.set("fast_program", True)
        super().__init__(session, self.MEMORY_MAP)


def _make_target(class_name, internal_algo, flash_size, spim_algo=None):
    regions = [
        FlashRegion(
            name="internal_flash",
            start=0x08000000,
            length=flash_size,
            page_size=0x400,
            sector_size=0x800,
            is_boot_memory=True,
            algo=internal_algo
        ),
    ]
    if spim_algo is not None:
        regions.append(
            FlashRegion(
                name="spim",
                start=0x08400000,
                length=0x01000000,
                page_size=0x400,
                sector_size=0x1000,
                is_boot_memory=False,
                is_external=True,
                algo=spim_algo
            )
        )
    regions.append(RamRegion(start=0x20000000, length=0x18000))
    return type(class_name, (_AT32Base,), {
        "MEMORY_MAP": MemoryMap(*regions),
        "__module__": __name__,
    })


# 1. Base targets (internal flash only)
AT32F403ACCT7 = _make_target("AT32F403ACCT7", FLASH_ALGO_AT32F403A_256, 0x00040000)
AT32F403ACET7 = _make_target("AT32F403ACET7", FLASH_ALGO_AT32F403A_512, 0x00080000)
AT32F403ACGT7 = _make_target("AT32F403ACGT7", FLASH_ALGO_AT32F403A_1024, 0x00100000)

AT32F407RCT7 = _make_target("AT32F407RCT7", FLASH_ALGO_AT32F407_256, 0x00040000)
AT32F407RET7 = _make_target("AT32F407RET7", FLASH_ALGO_AT32F407_512, 0x00080000)
AT32F407RGT7 = _make_target("AT32F407RGT7", FLASH_ALGO_AT32F407_1024, 0x00100000)

# 2. Suffix targets with external SPIM Flash
SPIM_CONFIGS = [
    ('type1_remap0', FLASH_ALGO_AT32_EXT_TYPE1_REMAP0),
    ('type1_remap1', FLASH_ALGO_AT32_EXT_TYPE1_REMAP1),
    ('type2_remap0', FLASH_ALGO_AT32_EXT_TYPE2_REMAP0),
    ('type2_remap1', FLASH_ALGO_AT32_EXT_TYPE2_REMAP1),
]

TARGET_MAP = {
    'at32f403axc': AT32F403ACCT7,
    'at32f403axe': AT32F403ACET7,
    'at32f403axg': AT32F403ACGT7,
    'at32f403a': AT32F403ACGT7,
    'at32f407xc': AT32F407RCT7,
    'at32f407xe': AT32F407RET7,
    'at32f407xg': AT32F407RGT7,
    'at32f407': AT32F407RGT7,
}

_FAMILIES = [
    ('AT32F403A', 'at32f403a', [
        ('xc', FLASH_ALGO_AT32F403A_256, 0x00040000),
        ('xe', FLASH_ALGO_AT32F403A_512, 0x00080000),
        ('xg', FLASH_ALGO_AT32F403A_1024, 0x00100000),
    ]),
    ('AT32F407', 'at32f407', [
        ('xc', FLASH_ALGO_AT32F407_256, 0x00040000),
        ('xe', FLASH_ALGO_AT32F407_512, 0x00080000),
        ('xg', FLASH_ALGO_AT32F407_1024, 0x00100000),
    ]),
]

for fam_name, fam_prefix, caps in _FAMILIES:
    for cap_code, int_algo, flash_size in caps:
        for suffix_name, spim_algo in SPIM_CONFIGS:
            cls_name = f"{fam_name}_{cap_code.upper()}_{suffix_name.upper()}"
            tgt_cls = _make_target(cls_name, int_algo, flash_size, spim_algo)
            # Register in current module globals
            globals()[cls_name] = tgt_cls
            
            # Map target names: at32f403axc_type1_remap0, at32f403axg_type2_remap1, etc.
            target_key = f"{fam_prefix}{cap_code}_{suffix_name}"
            TARGET_MAP[target_key] = tgt_cls
            # alias with reamp
            reamp_key = f"{fam_prefix}{cap_code}_{suffix_name.replace('remap', 'reamp')}"
            TARGET_MAP[reamp_key] = tgt_cls
            
            # If xg (1024KB default), also map without xg prefix: at32f403a_type2_remap1
            if cap_code == 'xg':
                short_key = f"{fam_prefix}_{suffix_name}"
                TARGET_MAP[short_key] = tgt_cls
                short_reamp_key = f"{fam_prefix}_{suffix_name.replace('remap', 'reamp')}"
                TARGET_MAP[short_reamp_key] = tgt_cls

__all__ = [
    'AT32F403ACCT7', 'AT32F403ACET7', 'AT32F403ACGT7',
    'AT32F407RCT7', 'AT32F407RET7', 'AT32F407RGT7',
    'SPIM_ALGO_MAP', 'TARGET_MAP'
]
