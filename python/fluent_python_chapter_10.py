from utils import print_tab
print(f'Chapter 10: Sequence Hacking, Hashing, and Slicing'.upper())
outline = '''OUTLINE:
• Basic sequence protocol: __len__ and __getitem__ .
• Safe representation of instances with many items.
• Proper slicing support, producing new Vector instances.
• Aggregate hashing taking into account every contained element value.
• Custom formatting language extension.
'''
print(outline)

print('UNDERSTAND __getitem__ TO MAKE A CLASS BEHAVE LIKE A SEQUENCE')
class Vector:
	def __init__(self, *components):
		self._components = list(*components)

	def __str__(self):
		return "Vector class, attributes: " + str(self._components)

	def __len__(self):
		return len(self._components)

	def __getitem__(self, idx): # __getitem__ make the class slicing like a sequence
		cls = type(self)
		if isinstance(idx, slice):
			return cls(self._components[idx])
		elif isinstance(idx, int):
			return self._components[idx]
		else:
			msg = '{cls.__name__} indices must be integer'
			print_tab(msg.format(cls=cls))

v1 = Vector([1,2,3,4])
print_tab(f'Slicing Vector instance is still a Vector instance: {v1[1:3]}')
v1[1.2]

print('DYNAMIC ATTRIBUTE USING __getattr__')

import string

class Vector_Dyna_Attr(Vector):
	attr_list = string.ascii_lowercase

	def __str__(self):
		return "Vector_Dyna_Attr class, attributes: " + str(self._components)

	def __getattr__(self, name):
		if len(name) == 1:
			pos = self.attr_list.find(name)
			if 0 <= pos < len(self):
				return self._components[pos]
v2 = Vector_Dyna_Attr([1,2,3,4])
for i in range(len(v2)):
	attr = v2.attr_list[i]
	print_tab(f'v2.{attr} = {v2.__getattr__(attr)}')

print('HASHING A CLASS WHICH BEHAVE LIKE SEQUENCE')

from functools import reduce
from operator import xor
class Vector_Hashable(Vector):
	def __eq__(self, other):
		return tuple(self._components) == tuple(other.components)

	def __hash__(self):
		return reduce(xor, [hash(i) for i in self._components])

v3 = Vector_Hashable([1,2,3,104.1])
print_tab(f'Hash of v3: {hash(v3)}')

summary = '''SUMMARY:
1. This chapter shows how to create a class that behave like a sequence. That means slice of an instance will create new instance.
2. How to use __getattr__ to create attributes for class
3. How to use functools.reduce to make hashing method for class
'''


