# NeRFpy

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org)
[![github ci](https://github.com/smu-tao-group/nerfpy/actions/workflows/ci.yml/badge.svg)](https://github.com/smu-tao-group/nerfpy/actions/workflows/ci.yml)
[![codecov](https://codecov.io/gh/smu-tao-group/nerfpy/branch/main/graph/badge.svg?token=fl4kUOywR3)](https://codecov.io/gh/smu-tao-group/nerfpy)

NeRFpy: A Python implementation and extension of Natural Extension Reference Frame.


## Install

Using `pip` to install:

```
# for release (stable) version
pip install nerfpy

# for the latest version
pip install git+https://github.com/smu-tao-group/nerfpy.git
```

## Usage

For high level usage, use NERF class to interact with PDB (read, reconstruct and write). There are also utility functions for low level usage.

```python
# interact with PDB file
from nerfpy import NERF

nerf = NERF()
nerf.read_pdb(PDB_PATH)
nerf.reconstruct()
nerf.save_pdb(NEW_PDB_PATH)

# use your own coordinates (n * 3)
from nerf.utils import (
    calc_r_from_coords,
    calc_alpha_from_coords,
    calc_psi_from_coords,
    reconstruct_from_internal_coords
)

r = calc_r_from_coords(COORDS)
alpha = calc_alpha_from_coords(COORDS)
psi = calc_psi_from_coords(COORDS)
reconstructed_coords = reconstruct_from_internal_coords(r, alpha, psi)
```

## License

Apache-2.0 license
