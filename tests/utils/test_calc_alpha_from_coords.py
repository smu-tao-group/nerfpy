#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test calc_alpha_from_coords
"""

import numpy as np
from nerf.utils import calc_alpha_from_coords


SIZE = 100


def test_calc_alpha_from_coords():
    coords = np.random.random((SIZE, 3))
    alpha = calc_alpha_from_coords(coords)
    assert alpha.shape[0] == SIZE - 2
