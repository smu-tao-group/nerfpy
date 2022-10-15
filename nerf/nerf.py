#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""NERF class
"""

import numpy as np
from .utils import (
    calc_r_from_coords,
    calc_alpha_from_coords,
    calc_psi_from_coords,
    pdb_to_coords,
    coords_to_pdb,
    reconstruct_from_internal_coords
)


class NERF():
    """NeRF: construct 3D coordinates from internal coordinates

    Args:
        pdb_dir (str): path to PDB file
        coords (np.ndarray): 3D coordinates
        coords_rec (np.ndarray): reconstructed 3D coordinates
    """
    def __init__(self) -> None:
        self.pdb_dir = None
        self.coords = None
        self.coords_rec = None

    def read_pdb(self, pdb_dir) -> None:
        """Read in PDB file

        Args:
            pdb_dir (str): path to PDB file
        """
        self.pdb_dir = pdb_dir
        self.coords = pdb_to_coords(pdb_dir)

    def save_pdb(self, new_pdb_dir) -> None:
        """Save reconstructed coordinates to PDB file

        Args:
            new_pdb_dir (str): path to PDB file
        """
        assert self.coords_rec is not None, (
            "Must call reconstruct to calculate reconstructed coordinates"
        )
        coords_to_pdb(self.pdb_dir, self.coords_rec, new_pdb_dir)

    def reconstruct(self) -> np.ndarray:
        """Reconstruct 3D coordinates from internal coordinates

        Returns:
            coords (list): 3D coordinates
        """
        r = calc_r_from_coords(self.coords)
        alpha = calc_alpha_from_coords(self.coords)
        psi = calc_psi_from_coords(self.coords)

        self.coords_rec = reconstruct_from_internal_coords(r, alpha, psi)

        return self.coords_rec
