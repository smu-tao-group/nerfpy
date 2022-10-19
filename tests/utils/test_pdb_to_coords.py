#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test pdb to coords
"""

import pytest
from nerf.utils import pdb_to_coords
from nerf.datafiles import PDB_S, PDB_M


def test_pdb_to_coords_s():
    coords = pdb_to_coords(PDB_S)
    assert coords.shape[0] == 260
    assert coords.shape[1] == 3


def test_pdb_to_coords_m():
    coords = pdb_to_coords(PDB_M)
    assert coords.shape[0] == 1049


def test_pdb_to_coords_wrong_file():
    with pytest.raises(Exception):
        pdb_to_coords("wrong_file_path")
