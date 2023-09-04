import time
from itertools import cycle

class Nature:
    x = 5
    test = "Nature"

lights = [
    ("Green", 2),
    ("Yellow", 0.5),
    ("Red", 2)
]

colors = cycle(lights)

while True:
    c,s = next(colors)
    print (c)
    time.sleep(s)
    n1 = Nature()
    print(n1.test)

