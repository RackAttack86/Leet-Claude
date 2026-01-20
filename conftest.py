"""
Pytest configuration for LeetCode problems.

Enables imports like `from solution import Solution` by adding each test
file's directory to sys.path before it's collected.
"""

import sys
from pathlib import Path


def pytest_collectstart(collector):
    """Add test directory to sys.path before collection starts."""
    if hasattr(collector, 'fspath') and collector.fspath:
        test_dir = str(Path(collector.fspath).parent)
        # Insert at front to prioritize local solution.py
        if test_dir in sys.path:
            sys.path.remove(test_dir)
        sys.path.insert(0, test_dir)

        # Clear cached modules to force reimport
        for mod_name in list(sys.modules.keys()):
            if mod_name in ('solution', 'test_solution'):
                del sys.modules[mod_name]
