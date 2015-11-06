Franges
===========

Franges adds support for floating point and fixed precision (Decimal) range generator functions.

Usage
=====

```python
#!/usr/bin/env python

from franges import drange
from franges import frange

for x in drange(0,2,0.1, precision = 6):
print(x)
for x in frange(0,2,0.1):
print(x)

list(drange(0,1,0.1, 6)) # [0, 0.1, 0.2, ... , 0.9]
list(frange(1,0,-0.2)) # [1.0, 0.8, 0.6, 0.3999999999999999, 0.19999999999999996]
list(drange(1,0,-0.2,6)) # [1.0, 0.8, 0.6, 0.4, 0.2]
```
    
Contributors
============
Nisan Haramati       hanisan@gmail.com
