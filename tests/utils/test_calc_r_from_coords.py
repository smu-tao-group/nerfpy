#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test calc_r_from_coords
"""

import numpy as np
from nerf.utils import calc_r_from_coords


SIZE = 100


def test_calc_r_from_coords():
    coords = np.random.random((SIZE, 3))
    r = calc_r_from_coords(coords)
    assert r.shape[0] == SIZE - 1
