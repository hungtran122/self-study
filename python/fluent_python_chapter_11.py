from collections import namedtuple
from collections.abc import MutableSequence

from utils import print_tab

print('CHAPTER 11: INTERFACES: FROM PROTOCOL TO ABCs')
print('monkey patching IS A TEQNIQUE TO CHANGE A CLASS OR MODULE AT RUNTIME')
print('duck typing IS A TEQNIQUE TO OPERATE WITH OBJECTS REGARDLESS OF THEIR TYPES, AS LONG AS THEY IMPLEMENT CERTAIN PROTOCOLS/INTERFACES ')
print('collections.abc MODULE PROVIDE CLASSES FOR DATA STRUCTURE')
print('numbers MODULE PROVIDE CLASSES FOR NUMBERS INCLUDING INTEGRAL, REAL, RATIONAL, COMPLEX ETC.')
print('abc MODULE PROVIDES INFRASTRUCTURE TO CREATE CUSTOM ABSTRACT CLASS')

Card = namedtuple('Card', ['rank', 'suit'])
class FrenchDeck(MutableSequence):
	ranks = [str(i) for i in range(2,11)] + list('JQKA')
	suits = 'spades diamonds clubs hearts'.split()

	def __init__(self):
		self._cards = [(rank, suit) for suit in self.suits
		               for rank in self.ranks]

	def __len__(self):
		return len(self._cards)

	def __delitem__(self, key):
		del self._cards[key]

	def __setitem__(self, key, value):
		self._cards[key] = value

	def __getitem__(self, item):
		return self._cards[item]

	def insert(self, index: int, value) -> None:
		self._cards.insert(index, value)

deck = FrenchDeck()
print_tab(f'When inherit from a class with abstract methods. You must implement all abstract methods in subclass. Otherwise, TypeError will be raised in runtime')

print('TO CHECK FOR INTEGER/FLOAT YOU CAN USE numbers MODULE')
from numbers import *

a = 10
print_tab(f'a = {a}, a is integer: {isinstance(a, Integral)}')
print_tab(f'a = {a}, a is float: {isinstance(a, Real)}. a is float because integer is subclass of float')
a = 10.5
print_tab(f'a = {a}, a is integer: {isinstance(a, Integral)}')
print_tab(f'a = {a}, a is float: {isinstance(a, Real)}')

import abc
print('CREATE CUSTOM ABC (Abstract Base Class)')
class Shape(abc.ABC):
	@abc.abstractmethod
	def area(self): # abstract method
		# return area of the shape
		pass
	def __bool__(self): # concrete method can be also implemented in ABC
		return False if self.area() == 0 else True

class Rectangle(Shape):
	def __init__(self, height, width):
		self._h = height
		self._w = width
	def area(self):
		return self._h * self._w
r = Rectangle(10,20)
print_tab(f'Created custom ABC named Shape. Custom ABC can have abstract methods and concrete methods as well. Rectangle class inherits from Shape.')
print_tab(f'If you use stacked decorators with abc.abstracmethod, then abc.abstractmethod should be the innermost decorator. That means no decorators between abstractmethod and def')

print('REGISTER SUBCLASS OF AN ABSTRACT CLASS USING DECORATOR')
print_tab(f'When using decorator, the subclass will not inherit any methods from the abstract class.')
print_tab(f'And the subclass do not need to implement all abstract methods from the abstract class')
print_tab(f'However it will be recognized as issubclass/isinstance')

class Transportation(abc.ABC):
	@abc.abstractmethod
	def pick(self, passenger):
		pass
	@abc.abstractmethod
	def leave(self, passenger):
		pass

@Transportation.register
class Bus(list):
	def pick(self, passenger):
		self.append(passenger)
	def leave(self, passenger):
		self.pop(self.index(passenger))

bus = Bus(['Hung', 'Dung', 'Tien'])
bus.leave('Tien')
print_tab(f'bus is subclass of Transportation: {issubclass(Bus, Transportation)}')
print_tab(f'bus is instance of Transportation: {isinstance(bus, Transportation)}')

summary = '''SUMMARY:
1. Definition of monkey patching, duck typing
2. collections.abc provide data structure classes (Sequence, MutableSequence, etc.)
3. numbers module provides number class (Real, Integral, etc.)
4. abc module provides an infrastructure for Abstract Base Class
5. How to create custom abstract class:
    Inherit from abc.ABC class
    Create abstract methods, this is mandatory
    Create concrete methods if necessary
6. Create virtual class by registering abstract class using decorator register           
'''
print(summary)



