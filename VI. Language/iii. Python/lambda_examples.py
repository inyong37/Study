# lambda arguments: function

# map(function, list/iterable)
map(lambda x: x**2, range(5)) # python 2
list(map(lambda x: x**2, range(5))) # python 3 and 2

# reduce(function, string/list/tuple)
from functools import reduce # python 3
reduce(lambda x, y: x + y, [0, 1, 2, 3, 4])
reduce(lambda x, y: y + x, 'abcde')

# filter(function, list)
filter(lambda x: x < 5, range(10)) # python 2
list(filter(lambda x: x < 5, range(10))) # python 3 and 2
filter(lambda x: x % 2, range(10)) # python2
list(filter(lambda x: x % 2, range(10))) # python 3 and 2

# Reference: https://wikidocs.net/64