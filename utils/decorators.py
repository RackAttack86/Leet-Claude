"""
Useful decorators for LeetCode solutions
"""

import functools
import time
from typing import Callable


def memoize(func: Callable) -> Callable:
    """Simple memoization decorator for DP problems"""
    cache = {}

    @functools.wraps(func)
    def wrapper(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result

    return wrapper


def timing(func: Callable) -> Callable:
    """Print execution time of function"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"{func.__name__} executed in {(end - start) * 1000:.4f}ms")
        return result
    return wrapper


def validate_input(validator: Callable) -> Callable:
    """Validate function inputs before execution"""
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if not validator(*args, **kwargs):
                raise ValueError("Invalid input")
            return func(*args, **kwargs)
        return wrapper
    return decorator
