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
    number = 0
    for i in range(len(l)):
        if l[i] == e:
            number += 1
    return number
@timer
def liniear_search_sorted(l, e):
    number = 0
    for i in range(len(l)):
        if l[i] == e:
            number += 1
        if l[i] > e:
            return number
    return number

@timer
def bubble_sort(L):
    swap = False
    while not swap:
        #print('bubble sort: ' + str(L))
        swap = True
        for j in range(1, len(L)):
            if L[j-1] > L[j]:
                swap = False
                temp = L[j]
                L[j] = L[j-1]
                L[j-1] = temp
    return L




liniear_search(list, elm)
sl = bubble_sort(list)
liniear_search_sorted(sl, elm)







"""
print()

# linear search for unsorted list
num = liniear_search(list, elm)
print('linear search on unsorted')
print('========')

print(f'{elm} was in the file {num} times')
"""