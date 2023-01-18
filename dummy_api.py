#!/usr/bin/env python

from itertools import repeat
from args_validation import args_validation


@args_validation(n=int)
def dummy_function(n: int = 0) -> int:
    a, b = 0, 1
    for _ in repeat(None, n):
        a, b = b, a + b
    return a


#@args_validation
def dummy_generator(): #annotate the generator
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


if __name__ == '__main__':
    for i in (5, 0, -2, None, 1.2, -4.5, 'abc', list(), tuple()):
        try:
            print(dummy_function(n=i))
        except Exception as inst:
            print(f'i = {i} raised {type(inst).__name__} with args: {inst}')
    gen = dummy_generator()
    print(*[next(gen) for _ in repeat(None, 10)])
    print(dummy_function())
    