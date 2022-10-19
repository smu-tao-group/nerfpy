#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test reconstruct
"""

try:
    import mdtraj as md
except ModuleNotFoundError:
    raise Exception("Need mdtraj package to run this test!")

import os
import numpy as np
from nerf.utils import (
    calc_r_from_coords,
    calc_alpha_from_coords,
    calc_psi_from_coords,
    pdb_to_coords,
    coords_to_pdb,
    reconstruct_from_internal_coords
)
from nerf.datafiles import PDB_S, PDB_M


def test_reconstruct():
    size = 100
    r = np.random.random((size, ))
    alpha = np.random.random((size - 1, ))
    psi = np.random.random((size - 2, ))
    coords_rec = reconstruct_from_internal_coords(r, alpha, psi)
    assert coords_rec.shape == (size + 1, 3)


def test_reconstruct_accuracy():
    for pdb in [PDB_S, PDB_M]:
        # reconstruct pdb
        coords = pdb_to_coords(pdb)
        r = calc_r_from_coords(coords)
        alpha = calc_alpha_from_coords(coords)
        psi = calc_psi_from_coords(coords)
        coords_rec = reconstruct_from_internal_coords(r, alpha, psi)

        # write to new file
        new_pdb_dir = "./new.pdb"
        coords_to_pdb(pdb, coords_rec, new_pdb_dir)

        # read and calculate rmsd
        old = md.load(pdb)
        new = md.load(new_pdb_dir)
        rmsd = md.rmsd(old, new)
        assert rmsd <= 1e-5

        # remove generated file
        os.system(f"rm {new_pdb_dir}")
