#!/usr/bin/env python

from itertools import repeat
from functools import wraps

def args_validation(*, req_types): #annotate the decorator
    def _validation(func): 
        @wraps(func)
        def _wrapper(*args, **kwargs):
            n = args[0]
            if not isinstance(n, req_type):
                raise TypeError(f'n must be of type consistent with {req_type.__name__}')
            elif n < 0:
                raise ValueError('n must be non-negative')
            else:
                return func(*args, **kwargs)
        return _wrapper
    return _validation


@args_validation({'n': int})
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
            print(dummy_function(i))
        except Exception as inst:
            print(f'i = {i} raised {type(inst).__name__} with args: {inst}')
    gen = dummy_generator()
    print(*[next(gen) for _ in repeat(None, 10)])
    print(dummy_function())
    