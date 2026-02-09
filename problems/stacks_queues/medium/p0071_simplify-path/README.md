# Problem 71: Simplify Path

**Difficulty:** Medium
**Pattern:** Stacks Queues
**Link:** [LeetCode](https://leetcode.com/problems/simplify-path/)

## Problem Description

Given a string path, which is an absolute path (starting with a slash '/') to a file or directory in a Unix-style file system, convert it to the simplified canonical path.

In a Unix-style file system:
- A period '.' refers to the current directory
- A double period '..' refers to the directory up a level
- Multiple consecutive slashes (i.e. '//') are treated as a single slash '/'

For this problem, any other format of periods such as '...' are treated as file/directory names.

The canonical path should have the following format:
- The path starts with a single slash '/'
- Any two directories are separated by a single slash '/'
- The path does not end with a trailing '/'
- The path only contains the directories on the path from the root directory to the target file or directory (i.e., no period '.' or double period '..')

Return the simplified canonical path.

### Constraints

- 1 <= path.length <= 3000
- path consists of English letters, digits, period '.', slash '/' or '_'
- path is a valid absolute Unix path

### Examples

**Example 1:**
```
Input: path = "/home/"
Output: "/home"
Explanation: Note that there is no trailing slash after the last directory name.
```

**Example 2:**
```
Input: path = "/../"
Output: "/"
Explanation: Going one level up from the root directory is a no-op, as the root level is the highest level you can go.
```

**Example 3:**
```
Input: path = "/home//foo/"
Output: "/home/foo"
Explanation: In the canonical path, multiple consecutive slashes are replaced by a single one.
```

## Approaches

### 1. Stack

**Time Complexity:** O(n)
**Space Complexity:** O(n)

```python
def simplifyPath(self, path: str) -> str:
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
```

**Why this works:**

We split the path by '/' to get individual components. For each component:
- '..' means go up one directory, so we pop from the stack (if not empty)
- '.' or empty string means stay in current directory, so we skip
- Any other string is a valid directory name, so we push to the stack

Finally, we join the stack with '/' and prepend the root '/'.

## Key Insights

- Split path by '/'
- Use stack to track directories
- '..' pops from stack
- Ignore '.' and empty strings

## Common Mistakes

- Not handling multiple consecutive slashes
- Not handling '..' at root level (should stay at root)
- Forgetting to prepend '/' to the result

## Related Problems

- Valid Parentheses
- Basic Calculator

## Tags

String, Stack
