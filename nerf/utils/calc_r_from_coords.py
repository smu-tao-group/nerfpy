#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Calculate atom distance
"""

import numpy as np
from .check_numpy import check_numpy


def calc_r_from_coords(coords) -> list:
    """Calculate atom distance

    Args:
        coords (list): a list of atom coordinates with size of (n, 3)

    Returns:
        r (list): atom distance
    """
    coords = check_numpy(coords)

    r = np.sqrt(
        np.sum(
            (coords[1:] - coords[:-1]) ** 2, axis=1
        )
    )
    return r
