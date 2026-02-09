"""
LeetCode Problem #125: Valid Palindrome
Difficulty: Easy
Pattern: Two Pointers
Link: https://leetcode.com/problems/valid-palindrome/

Problem:
--------
A phrase is a palindrome if, after converting all uppercase letters into lowercase
letters and removing all non-alphanumeric characters, it reads the same forward and
backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Constraints:
-----------
- 1 <= s.length <= 2 * 10^5
- s consists only of printable ASCII characters

Examples:
---------
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Input: s = " "
Output: true
Explanation: After removing non-alphanumeric characters, s is an empty string.
Since an empty string reads the same forward and backward, it is a palindrome.
"""


class Solution:
    """
    Solution to LeetCode Problem #125: Valid Palindrome

    Approach: Two Pointers (Optimal)
    Time Complexity: O(n)
    Space Complexity: O(1)

    Key Insights:
    - Use two pointers starting from both ends
    - Skip non-alphanumeric characters
    - Compare characters in lowercase
    - No need to create a filtered string (saves space)
    """
    def isPalindrome(self, s: str) -> bool:
        """
        Check if string is a valid palindrome.

        Args:
            s: Input string

        Returns:
            True if palindrome, False otherwise
        """
        pass

    def isPalindrome_filter(self, s: str) -> bool:
        """
        Alternative approach: Filter then compare.
        Time: O(n), Space: O(n)
        """
        pass



PROBLEM_METADATA = {
    "number": 125,
    "name": "Valid Palindrome",
    "difficulty": "Easy",
    "pattern": "Two Pointers",
    "topics": ["String", "Two Pointers"],
    "url": "https://leetcode.com/problems/valid-palindrome/",
    "companies": ["Facebook", "Microsoft", "Amazon", "Apple"],
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
}