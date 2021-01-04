from chapter_7_decorators import *

print("CHAPTER 7: FUNCTION DECORATORS AND CLOSURES")
'''
• How Python evaluates decorator syntax
• How Python decides whether a variable is local
• Why closures exist and how they work
• What problem is solved by nonlocal
'''

print('Decorator has power to replaced decorated function with another one')
@deco
def target():
	print_tab('running target')
target()

print('Decorators are executed immediately when a module is loaded')
@register
def f1():
	print_tab('running f1()', 2)
@register
def f2():
	print_tab('running f2()', 2)
def f3():
	print_tab('running f3()', 2)
def main():
	f1()
if __name__ == '__main__':
	main()
print('Decorator and Decorated functions are normally defined in two different modules')
print('In practice, most decorators define inner function and return it')
print('VARIABLE SCOPE RULES')
print_tab('When assign a variable, Python assume that variable is local. Use global statement to when assign value to global variable in a function')
print('CLOSURE FUNCTION')
def make_avarager():
	series = []
	def add(x):
		series.append(x)
		avg = sum(series)/len(series)
		print_tab(avg)
	return add
avg = make_avarager()
avg(10)
avg(11)
avg(12)
print('nonlocal DECLARATION')
print_tab('closure function helps inner function access free variables')
print_tab("but it doesn't work on immutable variables. In that case, we have to use nonlocal variables")
def make_averager_2():
	total = 0
	count = 0
	def add(x):
		# using nonlocal total, count this function will work fine
		nonlocal total, count
		total += x
		count += 1
		print(total/count)
	return add
avg = make_averager_2()
avg(10)

print('A SIMPLE DECORATOR EXAMPLE')
@log
def log_info(*args, **kwargs):
	print('INFO: ' + kwargs['txt'])

print('A SIMPLE PARAMETERIZED DECORATOR EXAMPLE')
@param_log(fmt='{%y-%m-%d-%H-%M-%S}')
def log_news(*args, **kwargs):
	print('NEWS: ' + kwargs['txt'])


log_info(txt='hello')
log_news(txt='hello')
print('USING functools.lru_cache FOR MEMOIZATION, APPLY TO RECURSIVE FUNCTION')

@clock
def fibonachi_1(n):
	if n < 2:
		return n
	return fibonachi_1(n-1) + fibonachi_1(n-2)
print('fibonachi_1 function gets called many times if not using lru_cache decorators')
fibonachi_1(3)

@functools.lru_cache
@clock
def fibonachi_2(n):
	if n < 2:
		return n
	return fibonachi_2(n-2) + fibonachi_2(n-1)
print('fibonachi_2 gets called only once')
fibonachi_2(3)

print('USING singledispatch TO MAKE GENERIC FUNCTION')
print('YOU CAN REGISTER DIFFERENT FUNCTIONS FROM A GENERIC FUNCTION AND USE THEM DIFFERENTLY ACCORDING TO THE TYPE OF FIRST ARGUMENT')
@functools.singledispatch
def print_something(arg, verbose=False):
	pass
@print_something.register
def _(arg: int, verbose=True):
	if verbose:
		print_tab(f'printing integer: {arg}')

	else:
		print_tab(arg)
@print_something.register(str)
def _ (arg, verbose=True):
	if verbose:
		print_tab(f'printing str: {arg}')

	else:
		print_tab(arg)
@print_something.register
def _ (arg: dict, verbose=True):
	if verbose:
		print_tab(f'printing dict:')
		for k,v in arg.items():
			print_tab(f'{k} => {v}', 2)
	else:
		print_tab(arg)
print_something(10)
print_something('10')
print_something({'a': 10})










