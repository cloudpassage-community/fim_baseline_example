import fim_baseline_example
from halo_general import HaloGeneral

# Build config
config = fim_baseline_example.ConfigHelper()

# get a halo object for api methods wrapper
halo = HaloGeneral(config)

# let's go
fim_baseline_example.FIM_BaselineExample(halo)
