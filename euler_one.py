from functools import reduce
from operator import add
limit = 1000
print(reduce(add, [x for x in range(1, limit) if x % 3 == 0 or x % 5 == 0]))
