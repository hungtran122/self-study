import math
from array import array

from utils import print_tab

print('CHAPTER 9: A PYTOHNIC OBJECT')
outline = '''OUTLINE:
\t • Support the built-in functions that produce alternative object representations (e.g., repr() , bytes() , etc).
\t • Implement an alternative constructor as a class method.
\t • Extend the format mini-language used by the format() built-in and the str.for mat() method.
\t • Provide read-only access to attributes.
\t • Make an object hashable for use in sets and as dict keys.
\t • Save memory with the use of __slots__ .
'''
print(outline)

class Vector2D:
	typecode = 'd'
	def __init__(self, x, y):
		self.x = x
		self.y = y
	def __iter__(self):
		return (i for i in (self.x, self.y))
	def __str__(self):
		return str(tuple(*self))
	def __repr__(self):
		name_class = type(self).__name__
		return f'Class: {name_class}, x: {self.x}, y: {self.y}'
	def __eq__(self, other):
		return tuple(self) == tuple(other)
	def __bytes__(self):
		ret = (bytes([ord(self.typecode)]) + bytes(array(self.typecode, self)))
		return ret
	def __abs__(self):
		return math.hypot(self.x, self.y)
	def __bool__(self):
		return bool(abs(self))
	def __format__(self, format_spec):
		return format_spec.format(self.x, self.y)
v1 = Vector2D(10,20)
v2 = Vector2D(10,20)
print_tab(f'v1 == v2: {v1==v2}')
print_tab(f'v1 to bytes {bytes(v1)}')
print_tab(f'format v1: {format(v1,"x: {}, y: {}")}')

print('classmethod VS staticmethod DECORATORS')
print_tab('classmethod always takes class itself as 1st argument. classmethod is often used as alternative constructor')
print_tab('staticmethod works just like a plain function')
class Demo:
	@classmethod
	def classmeth(*arg):
		return arg
	@staticmethod
	def staticmeth(*arg):
		return arg
print_tab(f'Invoke classmethod without args, but classmethod still takes class itself as 1st argument: {Demo.classmeth()}')

print(f'TURN Vector2d CLASS TO A HASHABLE CLASS')
print_tab(f'1st step is to turn class attributes to immutables')
class Vector2d_Hashable:
	def __init__(self, x, y):
		self.__x = x
		self.__y = y
	@property # make x become read-only attribute
	def x(self):
		return self.__x
	@property # make y become read-only attribute
	def y(self):
		return self.__y
	def __hash__(self):
		return hash(self.x) ^ hash(self.y)
v1 = Vector2d_Hashable(7,20)
print_tab(f'hash value of v1: {hash(v1)}')

print(f'PRIVATE AND PROTECTED ATTRIBUTES')
print_tab(f'In python, it is impossible to have private attributes')
print_tab(f'Python uses name mangling mechanism to help create "private" attribute. You should add 2 underscore (_) prefix in attribute names')
print_tab(f'It does not make private attributes. Otherwise it make combine name of class and attribute into one, as you can see: {v1.__dict__}')

print(f'SAVING A LOT OF SPACE WITH __slots__')
print_tab(f'Originally Python stores instance attributes by a dict (instance.__dict__)')
print_tab(f'But it wastes memory because it stores hash table as well')
print_tab(f'When storing a huge number of instances, we should use __slots__ to save memory')
class Slots_Cls:
	__slots__ = ('x', 'y')
	def __init__(self, x, y):
		self.x = x
		self.y = y

s = Slots_Cls(1,2)
print_tab(f'{s.__slots__}, {s.x}, {s.y}')
print_tab(f'Problems of __slots__: you have to redeclare __slots__ in every inherited subclass')

print(f'OVERRIDING CLASS ATTRIBUTE')
print_tab(f'Python allows to create class attribute with default value')
class Full_Name:
	first_name = 'TRAN'
	def __init__(self, x):
		self.name = x
	@property
	def full_name(self):
		return ' '.join([self.first_name, self.name])
p1 = Full_Name('HUNG')
print_tab(f'{p1.full_name}')

print_tab(f'You can override attribute for other uses')
class Nguyen_Name(Full_Name):
	first_name = 'NGUYEN'
p2 = Nguyen_Name('LONG')
print_tab(f'{p2.full_name}')

summary = ''' SUMMARY:
This chapter covers:
• All string/bytes representation methods: __repr__ , __str__ , __format__ , and
__bytes__ .
• Several methods for converting an object to a number: __abs__ , __bool__ ,
__hash__ .
• The __eq__ operator, to test bytes conversion and to enable hashing (along with
__hash__ ).
• Use classmethod to create alternative constructors (eg: frombytes => create instance from bytes)
• Customized __format__ method to use format built-in function
• Make hashable class. 1st step is to make attributes immutables. Using xor-ing the hashes is recommended when implementing hash
• If you want to create millions of class instances, we better reduce memory usage by using __slots__ instead of __dict__ to store class attributes
• Python allows you to create class attribute with default value. Using it you can override class attributes for other uses 
'''
print(summary)




