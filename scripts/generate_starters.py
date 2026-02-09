"""
Script to generate starter.py files for all problems.
The starter.py contains only method signatures without implementations.
Usage: python scripts/generate_starters.py
"""

import re
from pathlib import Path


def extract_starter_code(solution_content: str) -> str:
    """Extract class definition and method signatures from solution.py content."""
    lines = solution_content.split('\n')
    result = []
    in_docstring = False
    docstring_char = None
    in_class = False
    in_method = False
    method_indent = 0
    skip_implementation = False

    # First, extract the docstring and imports at the top
    i = 0
    while i < len(lines):
        line = lines[i]

        # Track docstrings
        if '"""' in line or "'''" in line:
            if not in_docstring:
                docstring_char = '"""' if '"""' in line else "'''"
                in_docstring = True
                # Check if docstring ends on same line
                if line.count(docstring_char) >= 2:
                    in_docstring = False
                result.append(line)
            else:
                result.append(line)
                in_docstring = False
            i += 1
            continue

        if in_docstring:
            result.append(line)
            i += 1
            continue

        # Stop at class definition
        if line.strip().startswith('class '):
            break

        result.append(line)
        i += 1

    # Now process the class
    in_class = False
    class_indent = 0
    in_method = False
    in_method_docstring = False
    method_docstring_char = None

    while i < len(lines):
        line = lines[i]
        stripped = line.rstrip()

        # Detect class start
        if stripped.startswith('class '):
            in_class = True
            class_indent = len(line) - len(line.lstrip())
            result.append(line)
            i += 1
            continue

        if not in_class:
            i += 1
            continue

        # Check if we've exited the class (less indentation)
        if stripped and not stripped.startswith('#'):
            current_indent = len(line) - len(line.lstrip())
            if current_indent <= class_indent and not line.strip().startswith('"""'):
                # We've exited the class
                break

        # Class docstring
        if '"""' in stripped and not in_method:
            result.append(line)
            if stripped.count('"""') == 1:
                # Multi-line docstring
                i += 1
                while i < len(lines) and '"""' not in lines[i]:
                    result.append(lines[i])
                    i += 1
                if i < len(lines):
                    result.append(lines[i])
            i += 1
            continue

        # Detect method definition
        if re.match(r'\s+def \w+\(', stripped):
            in_method = True
            method_indent = len(line) - len(line.lstrip())
            result.append(line)
            i += 1

            # Check for method docstring
            if i < len(lines):
                next_line = lines[i]
                next_stripped = next_line.strip()
                if next_stripped.startswith('"""') or next_stripped.startswith("'''"):
                    method_docstring_char = '"""' if '"""' in next_stripped else "'''"
                    result.append(next_line)
                    if next_stripped.count(method_docstring_char) == 1:
                        # Multi-line docstring
                        i += 1
                        while i < len(lines) and method_docstring_char not in lines[i]:
                            result.append(lines[i])
                            i += 1
                        if i < len(lines):
                            result.append(lines[i])
                    i += 1

            # Add pass statement
            result.append(' ' * (method_indent + 4) + 'pass')
            result.append('')

            # Skip the actual implementation
            while i < len(lines):
                next_line = lines[i]
                if not next_line.strip():
                    i += 1
                    continue
                next_indent = len(next_line) - len(next_line.lstrip())
                if next_indent <= method_indent:
                    break
                i += 1

            in_method = False
            continue

        i += 1

    # Add metadata section
    result.append('')
    result.append('')

    # Find and add PROBLEM_METADATA
    for j in range(len(lines)):
        if 'PROBLEM_METADATA' in lines[j]:
            while j < len(lines):
                result.append(lines[j])
                if lines[j].strip() == '}':
                    break
                j += 1
            break

    return '\n'.join(result)


def generate_starter_files():
    """Generate starter.py for all problems."""
    problems_dir = Path('problems')
    created = 0

    for solution_file in problems_dir.rglob('solution.py'):
        starter_file = solution_file.parent / 'starter.py'

        try:
            solution_content = solution_file.read_text(encoding='utf-8')
            starter_content = extract_starter_code(solution_content)
            starter_file.write_text(starter_content, encoding='utf-8')
            created += 1
            print(f'Created: {starter_file}')
        except Exception as e:
            print(f'Error processing {solution_file}: {e}')

    print(f'\nTotal starter files created: {created}')


if __name__ == '__main__':
    generate_starter_files()
