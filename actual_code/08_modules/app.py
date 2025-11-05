import util as u
import random
import sys


from util import Shape, default_shape

# import numpy as np
# import pandas as pd

u.printer("I'm in app.py!")

triangle = u.Shape("triangle")

u.printer(triangle)

print(u.default_shape)

# namespacing

square = Shape("square")

print("From app.py:")
print(f"__name__ -> {__name__}")
print(u.__name__)

