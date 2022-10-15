#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Check and convert list to numpy
"""

import numpy as np


def check_numpy(coords) -> np.ndarray:
    """Check and convert coordinates to numpy array

    Args:
        coords (list): 2D coordinates

    Returns:
        np.ndarray: 2D coordinates
    """
    if not isinstance(coords, np.ndarray):
        coords = np.array(coords).reshape(-1, 3)
    return coords
