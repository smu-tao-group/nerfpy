#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test coords to pdb
"""

import os
import numpy as np
from nerf.utils import pdb_to_coords, coords_to_pdb
from nerf.datafiles import PDB_S


def test_coords_to_pdb():
    coords = pdb_to_coords(PDB_S)
    file_path = "./new.pdb"
    coords_new = np.random.random(coords.shape)
    coords_to_pdb(PDB_S, coords_new, file_path)
    # assert file exist and remove it
    assert os.path.isfile(file_path)
    os.system(f"rm {file_path}")
