from utils import print_tab
print("Chapter 8: Object References, Mutability,and Recycling".upper())
print("Variable are not boxes".upper())
a = [1,2,3]
b = a
print_tab(f'b and a refer to the same object in memory')
a.append(4)
print_tab(f'b get updated if a get updated {b} == {a}')

print('IDENTITY, EQUALITY, ALIASES')
print_tab(f'Using id() to get identity of a variable, id of b is: {id(b)}, id of a is: {id(a)}')
print_tab(f'a is b if only id of a == id of b')
print_tab(f'a equal to b if only value of a == value of b')

print('CHOOSING BETWEEN == AND is')
print_tab(f'In most cases, we use == to compare two variables. However if we compare with singleton (eg: None), we better use is')

print('COPY IS SHALLOW BY DEFAULT')
a = [1, (2,3,4)]
b = a[:] # this is copy a to b
print_tab(f'b == a: {b==a}, b is a: {b is a}')
print(f'SHALLOW COPY WILL CLONE THE OUTTERMOST OBJECT. IF THE OBJECT CONTAINS MUTABLE OBJECTS, IT DOES NOT CLONE THE INSIDE MUTABLE OBJECTS')
a = [1, [2,3,4]]
b = list(a) # shallow copy
b[1].append(5)
print_tab(f'Modify inside mutable objects of b will also modify them in a: {a}, {b}')
print('IF deepcopy MAY BE TOO DEEP IN SOME CASES, YOU CAN IMPLEMENT __copy__ and __deepcopy__ TO HANDLE EXCEPTION')

print(f'PARAMETERS INSIDE FUNCTION BECOME ALIASES OF ACTUAL ARGUMENTS')
a = [1,2,3]
def add(a, b):
	a += b
	return a
print_tab(f'After passed a to function add, a is changed: {add(a, [4])}')

print('NEVER USE MUTABLE TYPES AS DEFAULT VALUE')
class Bus:
	def __init__(self, passengers=[]):
		self.passengers = passengers
	def pick(self, p):
		self.passengers.append(p)
	def drop(self, p):
		self.passengers.remove(p)

bus1 = Bus()
bus1.pick('Hung')
bus2 = Bus()
print_tab(f'bus2 share same object passengers with bus1 because they use same mutable parameter by default: bus2: {bus2.passengers}, bus1: {bus1.passengers}')

print('del COMMAND and garbage COLLECTOR')
print_tab('del command only delete the name, not the object')
print_tab('if you delete a variable which is the only reference to an object, then the object will be garbage collected after del command')

print(f'WEAK REFERENCE')
print_tab(f'weak reference will not increase reference count of an object. Therefore when you delete the object, weakref will be gone')
import weakref
class Dummy:
	def __init__(self):
		self.type = 'nothing'
a = Dummy()
wr = weakref.ref(a)
print_tab(f'weakref before delete object: {wr()}')
del a
print_tab(f'weakref after delete object: {wr()}')

print('SOME TRICKS WITH IMMUTABLES')
print_tab('Create new tuple from other tuple will actually refer to the same tuple')
a = (1,2,3)
b = tuple(a)
print_tab(f'a is b: {a is b}')
c = a[:]
print_tab('Slicing does not make a new tuple')
print_tab(f'a is c: {a is c}')

print_tab('Creat variables to the same value of string, integer, float will not make new object')
a = 'abc'
b = 'abc'
print_tab(f'a is b : {a is b}')
a = 1e3
b = 1e3
print_tab(f'a is b : {a is b}')
a = float(0.2)
b = float(0.2)
print_tab(f'a is b : {a is b}')

summary = '''
Chapter Summary
Every Python object has an identity, a type, and a value. Only the value of an object
changes over time. 7
If two variables refer to immutable objects that have equal values ( a == b is True ), in
practice it rarely matters if they refer to copies or are aliases referring to the same object
because the value of an immutable object does not change, with one exception. The
exception is immutable collections such as tuples and frozensets: if an immutable col‐
lection holds references to mutable items, then its value may actually change when the
value of a mutable item changes. In practice, this scenario is not so common. What
never changes in an immutable collection are the identities of the objects within.
The fact that variables hold references has many practical consequences in Python pro‐
gramming:
• Simple assignment does not create copies.
• Augmented assignment with += or *= creates new objects if the lefthand variable is
bound to an immutable object, but may modify a mutable object in place.
• Assigning a new value to an existing variable does not change the object previously
bound to it. This is called a rebinding: the variable is now bound to a different object.
If that variable was the last reference to the previous object, that object will be
garbage collected.
• Function parameters are passed as aliases, which means the function may change
any mutable object received as an argument. There is no way to prevent this, except
making local copies or using immutable objects (e.g., passing a tuple instead of a
list).
• Using mutable objects as default values for function parameters is dangerous be‐
cause if the parameters are changed in place, then the default is changed, affecting
every future call that relies on the default.
In CPython, objects are discarded as soon as the number of references to them reaches
zero. They may also be discarded if they form groups with cyclic references but no
outside references. In some situations, it may be useful to hold a reference to an object
that will not—by itself—keep an object alive. One example is a class that wants to keep
track of all its current instances. This can be done with weak references, a low-level
mechanism underlying the more useful collections WeakValueDictionary , WeakKey
Dictionary , WeakSet , and the finalize function from the weakref module.
'''
print_tab(summary)