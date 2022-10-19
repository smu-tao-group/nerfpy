#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Read coordinates from PDB file
"""

import numpy as np


def pdb_to_coords(pdb_dir) -> np.ndarray:
    """Read PDB and record coordinates

    Args:
        pdb_dir (str): path to PDB file

    Returns:
        np.ndarray: 2D coordinates
    """
    assert pdb_dir[-3:] == "pdb", "Please input a valid PDB file!"

    pdb = open(pdb_dir, "r").readlines()
    coords = []
    for line in pdb:
        if line[:4] == "ATOM":
            coords.append(
                [float(line[30:38]), float(line[38:46]), float(line[46:54])]
            )
    return np.array(coords)
