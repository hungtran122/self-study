import collections.abc as abc
import re
import reprlib

from utils import print_tab

outline = '''CHAPTER 14: ITERABLES, ITERATORS, AND GENERATORS
• How the iter(...) built-in function is used internally to handle iterable objects
• How to implement the classic Iterator pattern in Python
• How a generator function works in detail, with line-by-line descriptions
• How the classic Iterator can be replaced by a generator function or generator ex‐
pression
• Leveraging the general-purpose generator functions in the standard library
• Using the new yield from statement to combine generators
• A case study: using generator functions in a database conversion utility designed
to work with large datasets
• Why generators and coroutines look alike but are actually very different and should
not be mixed
'''
print(outline)

print('HOW iter(...) FUNCTION MAKES SEQUENCES ITERABLE')
RE_WORD = re.compile('\w+')
class Sentence:
	def __init__(self, text):
		self.text = text
		self.words = RE_WORD.findall(text) #re.findall returns a list with all nonoverlapping matches of the regular expression, as a list of strings.
	def __len__(self):
		return len(self.words)
	def __getitem__(self, item):
		# if item == 0:
		# 	raise KeyError
		return self.words[item]
	def __repr__(self):
		return f'Sentence: {reprlib.repr(self.text)}'
	# def __iter__(self):


s = Sentence('This book is awesome')
print_tab('If __getitem__ is implemented and index starts from 0, class will behave like sequence')
print_tab('__getitem__ does not guarantee the class is iterable when using checking type like issubclass/isinstance')
print_tab(f'Sentence class is Iterable: {issubclass(Sentence, abc.Iterable)}')

print(f'ITERABLEs vs ITERATORs')
print_tab('Iterator can be built from Iterable')
print_tab('Once iterator is exhausted, it is useless. You should delete it')
it = iter(s)
while True:
	try:
		print_tab(f'{next(it)}')
	except StopIteration:
		del it
		break

print(f'DESIGN A CLASSIC ITERATOR')
print_tab('Iterables have __iter__ method that instantiates a new iterator everytime')
print_tab('Iterators have __next__ method returns individual item and __iter__ method returns self')
print_tab('Iterator is Iterable. But Iterable is not Iterator')

class SentenceIterator:
	def __init__(self, words):
		self.words = words
		self.index = 0
	def __next__(self):
		try:
			word = self.words[self.index]
		except:
			raise StopIteration
		self.index += 1
		return word
	def __iter__(self):
		return self
class Sentence2:
	def __init__(self, text):
		self.text = text
		self.words = RE_WORD.findall(text)
	def __len__(self):
		return len(self.words)
	def __iter__(self):
		return SentenceIterator(self.words)

s2 = Sentence2('This Sentence class with iterator implemented')
it = iter(s2)
while True:
	try:
		print_tab(f'{next(it)}')
	except StopIteration:
		del it
		break

print('HOW GENERATOR FUNCTION WORKS')
print_tab('Generator is Iterator. Generator is implemented in form of a function called generator function')
def gen():
	yield 1
	yield 2
	yield 3
print_tab(f'Result of gen function is a generator object {gen()}. gen function is a function {gen}')
print_tab(f'Implement __iter__ method of an iterable Sentence class as a generator function. So we can get rid of SentenceIterator class')
class Sentence3:
	def __init__(self, text):
		self.text = text
		self.words = RE_WORD.findall(text)
	def __len__(self):
		return len(self.words)
	def __iter__(self):
		for w in self.words:
			yield w
s3 = Sentence3('Sentence class using a generator function to make __iter__ method')
it = iter(s3)
while True:
	try:
		print_tab(f'{next(it)}')
	except StopIteration:
		del it
		break

print('A LAZY IMPLEMENTATION WHICH SAVES MEMORY')
print_tab('To save memory we can build a Sentence class with __iter__ method will yield value directly from the text. No need to create words')
class Sentence4:
	def __init__(self, text):
		self.text = text
	def __iter__(self):
		for match in RE_WORD.finditer(self.text):
			yield match.group()

print('USE GENERATOR EXPRESSION TO BUILD EVEN SHORTER VERSION')
print_tab('A list comprehension is a factory of lists. A generator expression is a factory of generators')

class Sentence5:
	def __init__(self, text):
		self.text = text
	def __iter__(self):
		return (match.group() for match in RE_WORD.finditer(self.text))

print('SOME TIPS WHEN USING GENERATOR EXPRESSION')
print_tab('Only use generator expression if you can implement it in 1 line')
print_tab('Use generator function if it is reused multiple times')

print('ARITHMETIC PROGRESSION GENERATOR WHERE YOU CAN LOOP OVER ITERABLE USING BEGIN, STEP, AND END POSITION')
print_tab('Build-in funciton range() is an example if pregression generator')

class ArithmeticProgression:
	def __init__(self, begin, step, end=None):
		self.begin = begin
		self.step = step
		self.end = end
	def __iter__(self):
		ret = type(self.begin + self.step)(self.begin)
		inf_loop = self.end is None
		idx = 0
		while inf_loop or ret < self.end:
			yield ret
			idx += 1
			ret = self.begin + self.step * idx
from fractions import Fraction
print_tab(f'Result of progression generator class: {list(ArithmeticProgression(0, Fraction(1,2), 4))}')

print_tab('Using generator function is good enough to create progression generator')
def arithmetic_prog_gen(begin, step, end=None):
	ret = type(begin+step)(begin)
	inf_loop = end is None
	idx = 0
	while inf_loop or ret < end:
		yield ret
		idx += 1
		ret = begin + step * idx
print_tab(f'Result of progression generator function: {list(arithmetic_prog_gen(0, Fraction(1,2), 4))}')

print('USING itertools TO CREATE GENERATOR')
import itertools
def arithmetic_prog_gen_itertools(begin, step, end=None):
	first = type(begin+step)(begin)
	gen = itertools.count(first, step)
	if end is not None:
		gen = itertools.takewhile(lambda x: x < end, gen)
	return gen
print_tab(f'Result of progression generator function using itertools: {list(arithmetic_prog_gen_itertools(0, Fraction(1,2), 4))}')

print('HOW TO USE BUILT-IN GENERATOR FUNCTIONS')
print_tab('''List of built-ins
\t1. Itertools: compress, dropwhile, filterfalse, islice, takewhile, count
\t2. filter''')

def vowel(c):
	return c.lower() in 'aeiou'

s = 'Aardvark'
print_tab(f'How to use filter: {list(filter(vowel, s))}')
print_tab(f'How to use itertools.filterfalse: {list(itertools.filterfalse(vowel, s))}')
print_tab(f'How to use itertools.dropwhile: {list(itertools.dropwhile(vowel, s))}')
print_tab(f'How to use itertools.takewhile: {list(itertools.takewhile(vowel, s))}')
print_tab(f'How to use itertools.compress: {list(itertools.compress(s, (1,1,1,0,0,0)))}')
print_tab(f'How to use itertools.islice: {list(itertools.islice(s, 1,3,1))}')

print('HOW TO USE BUILT-IN MAPPING FUNCTIONS')

import operator
s = range(1,11)
print_tab('Mapping functions compute each individual item from iterable input/inputs then yield the result')
print_tab(f'How to use itertools.accumulate: {list(itertools.accumulate(s, operator.mul))}')
print_tab(f'How to use map: {list(map(operator.add, range(11), range(2,10)))}')
print_tab(f'How to use itertools.starmap: {list(itertools.starmap(operator.mul, enumerate("abc", 1)))}')

print('HOW TO USE MERGING GENERATOR FUNCTIONS')
print_tab('Merging generators take multiple iterable inputs and merge them in sequence or in parallel')
print_tab(f'How to use itertools.chain: {list(itertools.chain(range(11), range(11,20)))}')
print_tab(f'How to use itertools.chain.from_iterable: {list(itertools.chain.from_iterable(zip("ABC", "abc")))}')
print_tab(f'How to use itertools.zip_longest: {list(itertools.zip_longest("ABC", "abcd", fillvalue="?"))}')
print_tab(f'How to use itertools.product: {list(itertools.product("ABC", "abc"))}')

print('HOW TO USE EXPANDING GENERATOR FUNCTIONS')
print_tab('Expanding generators take 1 input and return multiple outputs')
print_tab(f'How to use itertools.count: {list(itertools.islice(itertools.count(0, 1), 3))}')
print_tab(f'How to use itertools.cycle: {list(itertools.islice(itertools.cycle(range(3)), 6))}')
print_tab(f'How to use itertools.repeat: {list(itertools.repeat("ABC", 2))}')
print_tab(f'How to use itertools.combinations: {list(itertools.combinations("ABC", 2))}')
print_tab(f'How to use itertools.permutations: {list(itertools.permutations("ABD", 3))}')

print('HOW TO USE REARRANGING GENERATOR FUNCTIONS')
print_tab('Rearranging generator functions will yield all items in input iterables but rearranged in some way')
animals = sorted(['duck', 'eagle', 'rat', 'giraffe', 'bear', 'bat', 'dolphin', 'shark', 'lion'], key=len)
print_tab(f'How to use itertools.groupby:')
for length, group in itertools.groupby(animals, len):
	print_tab(f'{length} => {list(group)}')

print('ITERABLE REDUCING FUNCTIONS')
print_tab('Those sum, reduce, all, any, max, min are reducing functions')

print('OTHER USAGE OF iter() FUNCTION')
print_tab(''' Using iter to read 
	with open('mydata.txt') as fp:
		for line in iter(fp.readline, ''):
		process_line(line)
''')
