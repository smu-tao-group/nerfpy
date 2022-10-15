#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test numpy conversion
"""

import numpy as np
from nerf.utils import check_numpy


def test_check_numpy():
    coords = [[1, 2, 3], [4, 5, 6]]
    coords_new = check_numpy(coords)
    assert isinstance(coords_new, np.ndarray)
