ilist = [1,2,3,4,5,6]
print([i for i in ilist])
print([i**2 for i in ilist])
print([i**3 for i in ilist])

import math
print([int(math.sqrt(i)) for i in (i**2 for i in ilist if i**2%2==0)])

print([i for i in range(0,10) if i%2==0])

