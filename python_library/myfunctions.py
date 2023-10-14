from random import random
from math import ceil

# Build function
def create_high_inc(income, v):
    if income >= v:
        high_inc = 1
    elif income < v:
        high_inc = 0
    else:
        high_inc = 'NA'
    return high_inc