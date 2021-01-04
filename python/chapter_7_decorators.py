'''
Since decorator has to be in separate file.
This module stores all decorators.
'''
from utils import print_tab
def deco(func):
	def inner():
		print_tab('running inner')
	return inner

registry = []
def register(func):
	print_tab('running register right after the decorator loaded (%s)' % func)
	registry.append(func)
	return func

import datetime
import functools
def log(func):
	@functools.wraps(func)
	def inner(*args, **kwargs):
		now = datetime.datetime.now().strftime('%H-%M-%S')
		print(now)
		func(*args, **kwargs)
	return inner
#parameterized decorators
def param_log(fmt = '{%H-%M-%S}'):
	def decorate(func):
		@functools.wraps(func)
		def inner(*args, **kwargs):
			now = datetime.datetime.now().strftime(fmt)
			print(now)
			func(*args, **kwargs)
		return inner
	return decorate

import time
def clock(func):
	@functools.wraps(func)
	def clocked(*args, **kwargs):
		t0 = time.time()
		result = func(*args, **kwargs)
		elapsed = time.time() - t0
		name = func.__name__
		arg_lst = []
		if args:
			arg_lst.append(', '.join(repr(arg) for arg in args))
		if kwargs:
			pairs = ['%s=%r' % (k, w) for k, w in sorted(kwargs.items())]
			arg_lst.append(', '.join(pairs))
		arg_str = ', '.join(arg_lst)
		print_tab('[%0.8fs] %s(%s) -> %r ' % (elapsed, name, arg_str, result))
		return result
	return clocked
