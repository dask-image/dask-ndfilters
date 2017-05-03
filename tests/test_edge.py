#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

import pytest

import numpy as np
import scipy.ndimage.filters as sp_ndf

import dask.array as da
import dask.array.utils as dau

import dask_ndfilters as da_ndf


@pytest.mark.parametrize(
    "err_type, axis",
    [
        (ValueError, 0.0),
        (ValueError, 2),
        (ValueError, -3),
    ]
)
@pytest.mark.parametrize(
    "da_func",
    [
        da_ndf.prewitt,
    ]
)
def test_edge_func_params(da_func, err_type, axis):
    a = np.arange(140.0).reshape(10, 14)
    d = da.from_array(a, chunks=(5, 7))

    with pytest.raises(err_type):
        da_func(d, axis)


@pytest.mark.parametrize(
    "axis",
    [
        0,
        1,
        2,
        -1,
        -2,
        -3,
    ]
)
@pytest.mark.parametrize(
    "da_func, sp_func",
    [
        (da_ndf.prewitt, sp_ndf.prewitt),
    ]
)
def test_edge_func_compare(da_func, sp_func, axis):
    s = (10, 11, 12)
    a = np.arange(float(np.prod(s))).reshape(s)
    d = da.from_array(a, chunks=(5, 5, 6))

    dau.assert_eq(
        sp_func(a, axis),
        da_func(d, axis)
    )
