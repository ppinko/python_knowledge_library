"""
a > exp > b

As soon as one comparison returns False , the expression evaluates immediately
to False , skipping all remaining comparisons.

Note that the expression exp in a > exp > b will be evaluated only once,
whereas in the case of a > exp and exp > b
exp will be computed twice if a > exp is true.
"""

import math

"""
this equals to:
3 < math.sqrt(16) and math.sqrt(16) < 5
"""
print(3 < math.sqrt(16) < 5)
# Out: True
