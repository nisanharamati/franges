#
# Copyright (C) 2012  POF.com
#
# This file is part of franges.
#
# franges is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# franges is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with franges.  If not, see <http://www.gnu.org/licenses/>.

# drange.py
import decimal
from math import ceil
# create the best xrange function you can based on python
# version (2.7.x / 3.x.x)
try:
    _xrange = xrange
except NameError:
    _xrange = range


def drange(start, stop=None, step=1, precision=None):
    """drange generates a set of Decimal values over the
    range [start, stop) with step size step

    drange([start,] stop, [step [,precision]])"""

    if stop is None:
        for x in _xrange(int(ceil(start))):
            yield x
    else:
        # find precision
        if precision is not None:
            decimal.getcontext().prec = precision
        # convert values to decimals
        start = decimal.Decimal(start)
        stop = decimal.Decimal(stop)
        step = decimal.Decimal(step)
        # create a generator expression for the index values
        indices = (
            i for i in _xrange(
                0,
                int(((stop-start)/step).to_integral_value())
            )
        )

        # yield results
        for i in indices:
            yield float(start + step*i)
