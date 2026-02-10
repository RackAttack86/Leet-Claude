"""
Tests for LeetCode Problem #134: Gas Station
"""

import pytest
try:
    from user_solution import Solution
    from solution import PROBLEM_METADATA
except ImportError:
    from solution import Solution, PROBLEM_METADATA


class TestGasStation:
    """Test cases for Gas Station problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()

    def test_example_1(self, solution):
        """Example 1 from problem description"""
        gas = [1, 2, 3, 4, 5]
        cost = [3, 4, 5, 1, 2]
        assert solution.canCompleteCircuit(gas, cost) == 3

    def test_example_2(self, solution):
        """Example 2 from problem description - impossible"""
        gas = [2, 3, 4]
        cost = [3, 4, 3]
        assert solution.canCompleteCircuit(gas, cost) == -1

    # Edge cases
    def test_single_station_enough_gas(self, solution):
        """Single station with enough gas"""
        gas = [5]
        cost = [4]
        assert solution.canCompleteCircuit(gas, cost) == 0

    def test_single_station_not_enough(self, solution):
        """Single station without enough gas"""
        gas = [3]
        cost = [5]
        assert solution.canCompleteCircuit(gas, cost) == -1

    def test_single_station_exactly_enough(self, solution):
        """Single station with exactly enough gas"""
        gas = [5]
        cost = [5]
        assert solution.canCompleteCircuit(gas, cost) == 0

    def test_exactly_enough_gas_total(self, solution):
        """Total gas equals total cost exactly"""
        gas = [1, 2, 3]
        cost = [2, 2, 2]
        assert solution.canCompleteCircuit(gas, cost) == 2

    def test_all_equal(self, solution):
        """Gas and cost are equal at every station"""
        gas = [3, 3, 3]
        cost = [3, 3, 3]
        assert solution.canCompleteCircuit(gas, cost) == 0

    def test_start_from_last_station(self, solution):
        """Best to start from the last station"""
        gas = [3, 1, 1]
        cost = [1, 2, 2]
        assert solution.canCompleteCircuit(gas, cost) == 0

    def test_two_stations_possible(self, solution):
        """Two stations with possible solution"""
        gas = [2, 3]
        cost = [3, 2]
        assert solution.canCompleteCircuit(gas, cost) == 1

    def test_two_stations_impossible(self, solution):
        """Two stations with impossible solution"""
        gas = [1, 1]
        cost = [2, 2]
        assert solution.canCompleteCircuit(gas, cost) == -1

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
