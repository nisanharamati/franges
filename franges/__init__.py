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

"""Franges adds support for floating point and fixed precision (Decimal) range generator functions

Syntax is identical to range([start,] stop [,step]) for frange,
and similar for drange, with an additional precision parameter
frange([start,] stop [, step])
drange([start,] stop [,step [,precision]])

drange returns Decimal types and can enforce precision if specified. Otherwise it is identical to frange.

Sample usage:

from franges import drange
for x in drange(0, 2, 0.1, 6):
    ...
    
from franges import frange
for x in frange(0, 2, 0.1):
    ...

list(drange(0,1,0.1, 6)) # [0, 0.1, 0.2, ... , 0.9]
list(frange(1,0,-0.2)) # [1.0, 0.8, 0.6, 0.3999999999999999, 0.19999999999999996]
list(drange(1,0,-0.2,6)) # [1.0, 0.8, 0.6, 0.4, 0.2]
"""




from .drange import drange
from .frange import frange

__all__ = ['frange', 'drange']
