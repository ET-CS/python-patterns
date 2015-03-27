#!/usr/bin/env python

# Decorator example

# from decorator import decorator
# read more at http://pypi.python.org/pypi/decorator
# required: pip install decorator

# simple decorator that print *args **kwargs before running function
def print_args(function):
    def wrapper(*args, **kwargs):
	print 'Arguments:', args, kwargs
	return function(*args, **kwargs)
    return wrapper

# define function with 'print_args' as decorator
@print_args
def write(text):
    print text

# call write() and which will run the print_args decorator
write('foo')