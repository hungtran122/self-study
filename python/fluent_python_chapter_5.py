'''
CODE EXAMPLES OF CHAPTER 5
'''
from utils import print_tab
print('CHAPTER 5: FIRST-CLASS FUNCTIONS')
print_tab('In python, functions are first class objects')

print('TREATING FUNCTION AS AN OBJECT')
def factorial(n):
	''' Function to calculate factorial of an integer'''
	return 1 if n < 2 else n * factorial(n-1)
print_tab(f'{factorial.__doc__}, type:  {type(factorial)}')

print('HIGHER ORDER FUNCTION')
print_tab('Pass function as argument to another function')
list_str = ['chào mừng', 'tiếng cười', 'bố', 'mẹ', 'con', 'ngôi nhà']
print_tab(f'Using sorting string by length: {sorted(list_str, key=len)}')

print('map, filter CAN BE REPLACED BY LIST COMP')
list_facts = [factorial(n) for n in range(5)]
print_tab(str(list_facts))
list_facts = [factorial(n) for n in range(10) if n%2 == 0]
print_tab(str(list_facts))

from functools import reduce
from operator import add
print('USING reduce, add TO SUM ALL ELEMENTS IN LIST')
print_tab(f'Sum of 10 first integers: {reduce(add, range(10))}')

print('ANONYMOUS FUNCTION/LAMBDA EXPRESSION')
names = ['TRAN MANH HUNG', 'NGUYEN QUANG HUNG', 'PHAN VAN ANH', 'ANH THI VIEN']
print_tab(f'sort full name by first name: {sorted(names, key = lambda n: n.split(" ")[-1])}')

print('POSITIONAL AND KEYWORD-ONLY ARGUMENTS'.upper())
def tag(name: str = "hung", *content: 'list of args', cls: int = None, **attrs) -> int:
	for c in content:
		print('content: ', c)
	for k,v in attrs.items():
		print(k,v)
	if cls:
		print(cls)
	return cls
print('FUNCTION ANNOTATIONS')
print_tab(f"tag func annotations: {tag.__annotations__}")
print('KEYWORD-ONLY ARGUMENTS')
def func(a,*,b):
	print_tab(f'a: {a} is positional argument, and b: {b} is keyword-only argument')
func(10,b=20)

print('RETRIEVING INFORMATION ABOUT ARGUMENTS')
print_tab(f'__default__ store default value of function definition')
print_tab(f"tag function arg default values: {tag.__defaults__}")
print_tab(f'__code__ contains many information including arg names')
print_tab(f"__code__.co_varnames includes all input args and local variables: {tag.__code__.co_varnames}")
print_tab(f"__code__.co_argcount stores number of arguments excluding * and ** args: {func.__code__.co_argcount}")

print('USING inspect LIBRARY TO RETRIEVE ARGUMENT INFORMATION')
from inspect import signature
sig = signature(tag)
print_tab('tag function arguments: ' + str(sig))
print_tab('Showing arguments name and default value')
for name, param in sig.parameters.items():
	print_tab(f"{str(param.kind)}: {name} = {param.default}")

print('OPERATOR MODULE FOR ARITHMETIC FUNCTIONS')
import operator
from functools import reduce
def factorial(n):
	return reduce(operator.mul, range(1,n+1))
print_tab(f'factorial of 3 first integers: {factorial(3)}')

print('USING itemgetter and attrgetter')
from operator import itemgetter, attrgetter
import collections
names = [('Hung', 30), ('Tuan', 25), ('Dung', 50)]
Person = collections.namedtuple('Person', 'name age')
persons = [Person(name='Hung', age=30), Person(name='Tuan', age=25), Person(name='Dung', age=50)]
print_tab(f"sorting people by age {sorted(names, key=itemgetter(1))}")
print_tab(f"sorting people by age {sorted(persons, key=attrgetter('age'))}")

print('USING methodcaller TO CALL A METHOD OF A GIVEN OBJECT')
class MyNumber:
	def __init__(self, n):
		self.n = n
	def sum(self, is_odd):
		items = [i for i in range(self.n) if (i%2==1)==is_odd]
		return reduce(add, items)
mynumber = MyNumber(10)
sum_odd = operator.methodcaller('sum', is_odd=True)
print_tab(f'using methodcaller to create summation of odd numbers: {sum_odd(mynumber)}')
hyphenate = operator.methodcaller('replace', ' ', '-')
s = 'xin chao vietnam'
print_tab(f'using methodcaller to create hyphenate function: {s} => {hyphenate(s)}')

print('USING partial TO CREATE NEW FUNCTION WITH FEWER ARGUMENTS')
import unicodedata, functools
nfc = functools.partial(unicodedata.normalize, 'NFC')
s1 = 'café'
s2 = 'cafe\u0301'
print_tab(f's1:{s1} s2:{s2}, is s1 = s2: {s1==s2}, after normalized: {nfc(s1)==nfc(s2)}')