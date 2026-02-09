"""
LeetCode Problem #71: Simplify Path
Difficulty: Medium
Pattern: Stacks Queues
Link: https://leetcode.com/problems/simplify-path/

Problem:
--------
Given a string path, which is an absolute path (starting with a slash '/') to a file or directory in a Unix-style file system, convert it to the simplified canonical path.

In a Unix-style file system, a period '.' refers to the current directory, a double period '..' refers to the directory up a level, and any multiple consecutive slashes (i.e. '//') are treated as a single slash '/'. For this problem, any other format of periods such as '...' are treated as file/directory names.

The canonical path should have the following format:

The path starts with a single slash '/'.
Any two directories are separated by a single slash '/'.
The path does not end with a trailing '/'.
The path only contains the directories on the path from the root directory to the target file or directory (i.e., no period '.' or double period '..')

Return the simplified canonical path.

Constraints:
-----------
- 1 <= path.length <= 3000
- path consists of English letters, digits, period '.', slash '/' or '_'
- path is a valid absolute Unix path

Examples:
---------
Input: path = "/home/"
Output: "/home"
Explanation: Note that there is no trailing slash after the last directory name.

Input: path = "/../"
Output: "/"
Explanation: Going one level up from the root directory is a no-op, as the root level is the highest level you can go.

Input: path = "/home//foo/"
Output: "/home/foo"
Explanation: In the canonical path, multiple consecutive slashes are replaced by a single one.
"""

from typing import List, Optional


class Solution:
    """
    Solution to LeetCode Problem #71: Simplify Path

    Approach: Stack
    Time Complexity: O(n)
    Space Complexity: O(n)

    Key Insights:
    - Split path by '/'
    - Use stack to track directories
    - '..' pops from stack
    - Ignore '.' and empty strings
    """

    def simplifyPath(self, path: str) -> str:
        """
        Simplify Unix-style path using a stack.

        Split path by '/', then process each component:
        - '..' -> pop from stack (go up one directory)
        - '.' or '' -> skip (current directory or empty)
        - other -> push to stack (valid directory name)

        Finally, join stack with '/' and prepend root '/'.
        """
        stack = []
        components = path.split('/')

        for component in components:
            if component == '..':
                if stack:
                    stack.pop()
            elif component == '.' or component == '':
                # Skip current directory reference and empty strings
                continue
            else:
                # Valid directory or file name
                stack.append(component)

        return '/' + '/'.join(stack)


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 71,
    "name": "Simplify Path",
    "difficulty": "Medium",
    "pattern": "Stacks Queues",
    "topics": ['String', 'Stack'],
    "url": "https://leetcode.com/problems/simplify-path/",
    "companies": ['Amazon', 'Microsoft', 'Facebook', 'Google'],
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
}
