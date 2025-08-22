from enum import Enum

from pandas.core.computation.engines import ENGINES


class subject(Enum):
    Engllis = 1
    math = 2
    Physics = 4
print(subject.math.value)

class overWride:
    def odd(self,*args):
        if len(args)==2:
            return args[0]+args[1]
            return a+b+c
        if len(args)==3:
            return args[0]+args[1]+args[2]


ov = overWride()
print(ov.odd(3,4))
print(ov.odd(6,5,4))


