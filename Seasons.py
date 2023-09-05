import time
from itertools import cycle

class Nature:
    x = 5
    test = "Nature"

seasons = [
    ("Green", 2),
    ("Yellow", 0.5),
    ("Red", 2),
    ("White", 4)
]

colors = cycle(seasons)

while True:
    c,s = next(colors)
    print (c)
    time.sleep(s)
    n1 = Nature()
    print(n1.test)

