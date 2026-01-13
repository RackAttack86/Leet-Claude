"""
Helper functions for testing LeetCode solutions
"""

import time
import functools
from typing import Any, Callable, List


def assert_equal_unordered(result: List, expected: List) -> bool:
    """Compare two lists ignoring order"""
    return sorted(result) == sorted(expected)


def assert_lists_equal(list1: 'ListNode', list2: 'ListNode') -> bool:
    """Compare two linked lists"""
    while list1 and list2:
        if list1.val != list2.val:
            return False
        list1 = list1.next
        list2 = list2.next
    return list1 is None and list2 is None


def time_execution(func: Callable) -> Callable:
    """Decorator to time function execution"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"{func.__name__} took {(end - start) * 1000:.2f}ms")
        return result
    return wrapper


def compare_solutions(func1: Callable, func2: Callable, test_cases: List) -> None:
    """Compare outputs and timing of two solution functions"""
    for i, test_case in enumerate(test_cases):
        print(f"\nTest Case {i + 1}: {test_case}")

        # Run first solution
        start1 = time.perf_counter()
        result1 = func1(*test_case)
        time1 = (time.perf_counter() - start1) * 1000

        # Run second solution
        start2 = time.perf_counter()
        result2 = func2(*test_case)
        time2 = (time.perf_counter() - start2) * 1000

        print(f"  Solution 1: {result1} ({time1:.2f}ms)")
        print(f"  Solution 2: {result2} ({time2:.2f}ms)")
        print(f"  Match: {result1 == result2}")
