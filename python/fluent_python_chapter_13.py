import itertools
from numbers import Real

from utils import print_tab

outline = ''' CHAPTER 13: OPERATOR OVERLOADING: DOING IT RIGHT
• How Python supports infix operators with operands of different types
• Using duck typing or explicit type checks to deal with operands of various types
• How an infix operator method should signal it cannot handle an operand
• The special behavior of the rich comparison operators (e.g., == , > , <= , etc.)
• The default handling of augmented assignment operators, like += , and how to overload them
'''
print(outline)
print('UNARY OPERATORS: - ( __neg__ ), + ( __pos__ ), ~ ( __invert__ )')
class Vector:
	def __init__(self, components: 'Iterable'):
		self._components = list(components)
	def __iter__(self):
		return iter(self._components)
	def __abs__(self):
		return sum([i**2 for i in self])
	def __neg__(self):
		return Vector([-i for i in self])
	def __pos__(self):
		return Vector([+i for i in self])
	def __add__(self, other):
		try:
			return Vector([s+o for s,o in itertools.zip_longest(self, other, fillvalue=0.0)])
		except TypeError:
			return NotImplemented
	def __radd__(self, other): # reversed add or righthand add
		return self + other
	def __mul__(self, scalar):
		return Vector(i*scalar for i in self) if isinstance(scalar, Real) else NotImplemented
	def __rmul__(self, scalar):
		return self*scalar
	def __eq__(self, other):
		if isinstance(other, Vector):
			return len(self) == len(other) and all(s==o for s,o in zip(self, other))
		else:
			return NotImplemented
	# def __iadd__(self, other):
		# no need to implement this when __add__ is already implemented
	# 	return self + other
	def __str__(self):
		return ', '.join([str(i) for i in self])
	def __len__(self):
		return len(self._components)

v1 = Vector([1,2,3,4])
v2 = Vector([1,2,3,4])

print('IMPLEMENT __add__ OPERATOR')
print_tab(f'In duck typing, we should refrain from testing type of object, therefore we use try-except command to handle wrong class input in __add__ method')
print_tab(f'By this try-expect, if we add a vector instance and a str. It will raise NotImplemented exception')
# v3 = v1 + 'ABC'

print('IMPLEMENT __mul__ OPERATOR')
print_tab('In __mul__ we should use geese typing, because we do not need to use many if-else to check class type. \n'
          '\tSo we should check type of object against some early superclass. In this case numbers.Real class')

print('RICH COMPARISON OPERATORS')
print_tab('a == b =>  __eq__')
print_tab('a != b =>  __ne__')
print_tab('a > b =>  __gt__')
print_tab('a < b =>  __lt__')
print_tab('a >= b =>  __ge__')
print_tab('a <= b =>  __le__')

print_tab(f'v1 == v2: {v1 == v2}')
print_tab(f'v1 == (1,2,3,4): {v1 == (1,2,3,4)}')

print('AUGMENTED ASSIGNMENT OPERATORS')
v1_alias = v1
v1 += v2
print_tab(f'v1: {v1}, v1 id: {id(v1)}, v1_alias: {id(v1_alias)}')

summary = '''SUMMARY:
1. Not recommend to overload of operators in built-in types
2. Using duck typing (try-except) to avoid using type checking requiring multiple if-else
3. Using geese typing (type checking) to check type of early superclass (eg: numbers.Real) which is superclass of many subclasses. That might require only 1 check type command.
4. If __add__ is implemented, __iadd__ might not need an implementation 
5. To support operations with other types, we return the NotImplemented special value—not an exception allowing the interpreter to try again by swapping the operands and calling the reverse special method for that operator (e.g., __radd__ ).
'''
print(summary)


