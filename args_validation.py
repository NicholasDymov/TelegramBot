#!/usr/bin/env python

from functools import wraps

def args_validation(req_types=None, /, **kwargs): #annotate the decorator
    """
    Function takes a dictionary of the form {<name_of_argument>: <type>} as positional-only argument.
    If not provided, takes named arguments in the form <name_of_argument>=<type>
    """
    if req_types is None:
        req_types = kwargs
    def _validation(func): 
        @wraps(func)
        def _wrapper(*args, **kwargs):
            for arg, req_type in req_types.items():
                if not isinstance(kwargs[arg], req_type):
                    raise TypeError(f'{arg} must be of type consistent with {req_type.__name__}')
            else:
                return func(*args, **kwargs)
        return _wrapper
    return _validation