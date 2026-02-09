"""
Tests for LeetCode Problem #146: LRU Cache
"""

import pytest
from solution import LRUCache, PROBLEM_METADATA




class TestLruCache:
    """Test cases for LRU Cache problem"""


    def test_example_1(self):
        """Example 1 from problem description"""
        # LRUCache lRUCache = new LRUCache(2);
        cache = LRUCache(2)

        # lRUCache.put(1, 1); // cache is {1=1}
        cache.put(1, 1)

        # lRUCache.put(2, 2); // cache is {1=1, 2=2}
        cache.put(2, 2)

        # lRUCache.get(1);    // return 1
        assert cache.get(1) == 1

        # lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
        cache.put(3, 3)

        # lRUCache.get(2);    // returns -1 (not found)
        assert cache.get(2) == -1

        # lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
        cache.put(4, 4)

        # lRUCache.get(1);    // return -1 (not found)
        assert cache.get(1) == -1

        # lRUCache.get(3);    // return 3
        assert cache.get(3) == 3

        # lRUCache.get(4);    // return 4
        assert cache.get(4) == 4


    def test_edge_case_capacity_one(self):
        """Test with capacity of 1"""
        cache = LRUCache(1)

        cache.put(1, 1)
        assert cache.get(1) == 1

        cache.put(2, 2)  # Evicts key 1
        assert cache.get(1) == -1
        assert cache.get(2) == 2


    def test_update_existing_key(self):
        """Test updating an existing key's value"""
        cache = LRUCache(2)

        cache.put(1, 1)
        cache.put(2, 2)
        cache.put(1, 10)  # Update value of key 1

        assert cache.get(1) == 10
        assert cache.get(2) == 2


    def test_get_nonexistent_key(self):
        """Test getting a key that doesn't exist"""
        cache = LRUCache(2)

        assert cache.get(1) == -1

        cache.put(1, 1)
        assert cache.get(2) == -1


    def test_lru_order_with_get(self):
        """Test that get() updates the LRU order"""
        cache = LRUCache(2)

        cache.put(1, 1)
        cache.put(2, 2)
        cache.get(1)      # Access key 1, making key 2 the LRU
        cache.put(3, 3)   # Should evict key 2 (not key 1)

        assert cache.get(1) == 1
        assert cache.get(2) == -1
        assert cache.get(3) == 3


    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
