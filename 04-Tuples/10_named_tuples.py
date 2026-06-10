#named_tuple

from collections import namedtuple
Point=namedtuple('Point',['x','y'])
p=Point(3,4)
print("Named tuple:",p)
print("x:",p.x,"y:",p.y)
