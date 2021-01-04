from utils import print_tab
### GENERATOR EXPRESSIONS
print('GENERATOR EXPRESSIONS')
symbols = 'Hello'
for i in tuple(ord(symbol) for symbol in symbols):
    print_tab(i)
### SLICE OBJECTS
print('SLICE OBJECTS')
a = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'), (5, 'five'), (6, 'six'), (7, 'seven'), (8, 'eight'), (9, 'nine')]
slice_name = slice(1,None,3)
print_tab(a[1::3])
print_tab(a[slice_name])

### BULDING LIST OF LISTS
print("BUILDING LIST OF LISTS")
row = ['_'] * 2
b = []
for i in range(3):
    b.append(row)
print_tab(b)
b[1][1] = 'abc'
print_tab(b)
print_tab('This is unexpected result because now 3 items in b refer to the same object row')

### MANAGING ORDERED SEQUENCES WITH bisect
print('MANAGING ORDERED SEQUENCES WITH bisect')
import bisect
def grade(score, breakpoints=[60,70,80,90], grades = 'FDCBA'):
    i = bisect.bisect(breakpoints, score)
    return grades[i]
grades = [grade(sc) for sc in [33, 99, 77, 70, 89, 90, 100]]
print_tab(grades)

print('INSERT ITEM INTO ORDERED SEQUENCE BY bisect.insort')
import random
a = list(range(10))
for i in range(5):
    new_i = random.randint(0, 20)
    bisect.insort(a, new_i)
    new_str = '{0:2d} -> {1}'
    print_tab(new_str.format(new_i, a))
# ARRAY TO STORE NUMBERS
print('ARRAY TO STORE NUMBERS')
from array import array
from random import random
a_1 = array('d', (random() for i in range(10**6)))

### DEQUE TO REMOVE OR INSERT ELEMENT FAST
print('DEQUE TO REMOVE OR INSERT ELEMENT FAST')
from collections import deque
dq = deque(range(10), maxlen=10)
print_tab(dq)
dq.rotate(3)
print_tab(dq)
dq.rotate(-3)
print_tab(dq)
dq.appendleft(100)
print_tab(dq)
dq.extend([99,98])
print_tab(dq)


