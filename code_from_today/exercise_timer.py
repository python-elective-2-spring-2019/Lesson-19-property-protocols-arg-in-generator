import sys
import time
import math
import random


text = sys.argv[1]
elm = sys.argv[2]

f = open(text)
text = f.read()
list = text.split()


# Decorator
def timer(func):
    print('im in decorator')
    def wrapper(*args, **kwargs):
        start = time.time()
        
        value = func(*args, **kwargs)
    
        end = time.time()
        print('The scripts execusion time was', format(end - start, '.6f'), 'seconds')
        print('========')

        return value
    return wrapper

@timer
def liniear_search(l, e):
    print('im in linear search')
    number = 0
    for i in range(len(l)):
        if l[i] == e:
            number += 1
    return number


print(liniear_search(list, elm))








"""
print()

# linear search for unsorted list
num = liniear_search(list, elm)
print('linear search on unsorted')
print('========')

print(f'{elm} was in the file {num} times')
"""