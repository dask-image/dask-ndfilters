# -*- coding: utf-8 -*-

from dask_ndfilters.conv import (
    convolve,
    correlate,
)

from dask_ndfilters.diff import (
    laplace,
)

from dask_ndfilters.edge import (
    prewitt,
    sobel,
)

from dask_ndfilters.gaussian import (
    gaussian_filter,
    gaussian_gradient_magnitude,
    gaussian_laplace,
)

from dask_ndfilters.generic import (
    generic_filter,
)

from dask_ndfilters.order import (
    minimum_filter,
    median_filter,
    maximum_filter,
    rank_filter,
    percentile_filter,
)

from dask_ndfilters.smooth import (
    uniform_filter,
)
