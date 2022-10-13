#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Calculate bond angle
"""

import numpy as np
from .check_numpy import check_numpy


def calc_alpha_from_coords(coords) -> np.ndarray:
    """Calculate bond angle

    Args:
        coords (list): a list of atom coordinates with size of (n, 3)

    Returns:
        alpha (list): bond angle
    """
    coords = check_numpy(coords)

    vectors = coords[1:] - coords[:-1]
    dot_prod = np.sum(vectors[1:] * vectors[:-1], axis=1) / (
        np.linalg.norm(vectors[1:], axis=1) *
        np.linalg.norm(vectors[:-1], axis=1)
    )
    alpha = np.arccos(np.clip(dot_prod, -1.0, 1.0))
    return alpha
