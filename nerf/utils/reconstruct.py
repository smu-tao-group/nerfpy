#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Reconstruct 3D coordinates from internal coordinates
"""

import numpy as np
from numpy.linalg import norm


def reconstruct_from_internal_coords(r, alpha, psi) -> np.ndarray:
    n_atoms = len(r) + 1
    coords = np.zeros((n_atoms, 3))

    coords[0] = [0, 0, 0]
    coords[1] = [r[0], 0, 0]
    coords[2] = coords[1] + [
        r[1] * np.cos(alpha[0]), r[1] * np.sin(alpha[0]), 0
    ]

    coords[3:, 0] = r[2:] * np.cos(alpha[1:])
    coords[3:, 1] = r[2:] * np.sin(alpha[1:]) * np.cos(psi)
    coords[3:, 2] = r[2:] * np.sin(alpha[1:]) * np.sin(psi)

    for i in range(3, n_atoms):
        bc = coords[i - 1] - coords[i - 2]
        bc_norm = bc / norm(bc)
        n = np.cross(coords[i - 2] - coords[i - 3], bc_norm)
        n_norm = n / norm(n)
        m = np.array([bc_norm, np.cross(n_norm, bc_norm), n_norm]).T
        coords[i] = np.dot(m, coords[i]) + coords[i - 1]

    return coords
