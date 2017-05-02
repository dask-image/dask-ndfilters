#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

import inspect

from dask_ndfilters import _utils


def test__get_docstring():
    f = lambda : 0

    result = _utils._get_docstring(f)

    expected = """
    Wrapped copy of "{mod_name}.{func_name}"


    Excludes the output parameter as it would not work Dask arrays.


    Original docstring:

    {doc}
    """.format(
        mod_name=inspect.getmodule(f).__name__,
        func_name=f.__name__,
        doc="",
    )

    assert result == expected


def test__update_wrapper():
    f = lambda : 0

    @_utils._update_wrapper(f)
    def g():
        return f()


    assert f.__name__ == g.__name__

    expected = """
    Wrapped copy of "{mod_name}.{func_name}"


    Excludes the output parameter as it would not work Dask arrays.


    Original docstring:

    {doc}
    """.format(
        mod_name=inspect.getmodule(g).__name__,
        func_name=g.__name__,
        doc="",
    )

    assert g.__doc__ == expected
