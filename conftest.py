"""
Pytest configuration for LeetCode problems.

Enables imports like `from solution import Solution` by adding each test
file's directory to sys.path before it's collected.
"""

import sys
from pathlib import Path


def pytest_collection_modifyitems(session, config, items):
    """Add each test file's directory to sys.path for proper imports."""
    dirs_added = set()
    for item in items:
        test_dir = str(Path(item.fspath).parent)
        if test_dir not in dirs_added:
            if test_dir not in sys.path:
                sys.path.insert(0, test_dir)
            dirs_added.add(test_dir)


# Override import mode to allow relative imports
def pytest_configure(config):
    """Configure pytest to handle imports correctly."""
    # Clear cached solution modules
    for mod_name in list(sys.modules.keys()):
        if 'solution' in mod_name:
            del sys.modules[mod_name]


def pytest_collectstart(collector):
    """Add test directory to sys.path before collection starts."""
    if hasattr(collector, 'path') and collector.path:
        test_dir = str(collector.path.parent)
        # Insert at front to prioritize local solution.py
        if test_dir not in sys.path:
            sys.path.insert(0, test_dir)

        # Clear cached modules to force reimport
        for mod_name in list(sys.modules.keys()):
            if mod_name in ('solution', 'test_solution'):
                del sys.modules[mod_name]
    elif hasattr(collector, 'fspath') and collector.fspath:
        test_dir = str(Path(collector.fspath).parent)
        # Insert at front to prioritize local solution.py
        if test_dir not in sys.path:
            sys.path.insert(0, test_dir)

        # Clear cached modules to force reimport
        for mod_name in list(sys.modules.keys()):
            if mod_name in ('solution', 'test_solution'):
                del sys.modules[mod_name]
