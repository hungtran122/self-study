import math
import sys

from utils import print_tab

print('CHAPTER 6 - DESIGN PATTERN')
print('Using inspect to get members of a module')

def strategy_1(a,b):
	return (a+b) / 2

def strategy_2(a,b):
	return math.sqrt(a*b)

def best_strat(a,b):
	import inspect
	strats = [func for name,func in inspect.getmembers(sys.modules[__name__], inspect.isfunction) if 'strategy_' in name]
	return max((strat(a,b) for strat in strats))

print_tab(f'{best_strat(20,10)}')