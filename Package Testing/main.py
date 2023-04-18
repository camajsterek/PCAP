from sys import path
path.append('C:\\Users\\user\\py\\modules')

import module as m  # noqa

zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]
print(m.suml(zeroes))
print(m.prodl(ones))
