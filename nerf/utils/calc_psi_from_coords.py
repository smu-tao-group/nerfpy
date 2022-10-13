#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Calculate dihedral angle
"""

import numpy as np
from .check_numpy import check_numpy


def calc_one_psi(p0, p1, p2, p3) -> float:
    """Calculate one dihedral angle
    Praxeolitic formula: https://stackoverflow.com/questions/20305272

    Args:
        p0 (list): coordinates of atom 0
        p1 (list): coordinates of atom 1
        p2 (list): coordinates of atom 2
        p3 (list): coordinates of atom 3

    Returns:
        psi (float): dihedral angle between these four atoms
    """
    b0 = -1.0 * (p1 - p0)
    b1 = p2 - p1
    b2 = p3 - p2

    # normalize b1 so that it does not influence magnitude of vector
    # rejections that come next
    b1 /= np.linalg.norm(b1)

    # vector rejections
    # v = projection of b0 onto plane perpendicular to b1
    #   = b0 minus component that aligns with b1
    # w = projection of b2 onto plane perpendicular to b1
    #   = b2 minus component that aligns with b1
    v = b0 - np.dot(b0, b1)*b1
    w = b2 - np.dot(b2, b1)*b1

    # angle between v and w in a plane is the torsion angle
    # v and w may not be normalized but that's fine since tan is y/x
    x = np.dot(v, w)
    y = np.dot(np.cross(b1, v), w)
    psi = np.arctan2(y, x)
    return psi


def calc_psi_from_coords(coords) -> np.ndarray:
    """Calculate dihedral angle

    Args:
        coords (list): a list of atom coordinates with size of (n, 3)

    Returns:
        psi (list): a list of dinedral angle
    """
    coords = check_numpy(coords)

    psi = map(
        calc_one_psi,
        coords[:-3], coords[1:-2], coords[2:-1], coords[3:]
    )
    return np.array(list(psi))
