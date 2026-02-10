"""
Generate template.py files from solution.py files.

Templates contain only:
- Import statements
- Helper classes (ListNode, TreeNode, etc.)
- Solution class with method signatures and 'pass' body
"""

import ast
import os
import re
from pathlib import Path


def extract_imports(source: str) -> list[str]:
    """Extract import statements from source code."""
    imports = []
    for line in source.split('\n'):
        stripped = line.strip()
        if stripped.startswith('from ') or stripped.startswith('import '):
            imports.append(line)
    return imports


def extract_helper_classes(tree: ast.Module) -> list[ast.ClassDef]:
    """Extract helper classes (non-Solution classes)."""
    helpers = []
    for node in ast.iter_child_nodes(tree):
        if isinstance(node, ast.ClassDef) and node.name != 'Solution':
            helpers.append(node)
    return helpers


def get_solution_class(tree: ast.Module) -> ast.ClassDef | None:
    """Get the Solution class from the AST."""
    for node in ast.iter_child_nodes(tree):
        if isinstance(node, ast.ClassDef) and node.name == 'Solution':
            return node
    return None


def create_method_signature(method: ast.FunctionDef) -> str:
    """Create a method signature with 'pass' body."""
    # Get the source for the def line including decorators
    args = []

    # Handle self
    for i, arg in enumerate(method.args.args):
        arg_str = arg.arg
        if arg.annotation:
            arg_str += f': {ast.unparse(arg.annotation)}'
        args.append(arg_str)

    # Handle *args
    if method.args.vararg:
        args.append(f'*{method.args.vararg.arg}')

    # Handle **kwargs
    if method.args.kwarg:
        args.append(f'**{method.args.kwarg.arg}')

    # Return type
    returns = ''
    if method.returns:
        returns = f' -> {ast.unparse(method.returns)}'

    return f'    def {method.name}({", ".join(args)}){returns}:\n        pass\n'


def create_helper_class_source(cls: ast.ClassDef) -> str:
    """Create source for a helper class."""
    lines = [f'class {cls.name}:']

    for node in cls.body:
        if isinstance(node, ast.FunctionDef):
            # Get method signature
            args = []
            for arg in node.args.args:
                arg_str = arg.arg
                # Check for default values
                defaults_offset = len(node.args.args) - len(node.args.defaults)
                arg_index = node.args.args.index(arg)
                if arg_index >= defaults_offset:
                    default = node.args.defaults[arg_index - defaults_offset]
                    arg_str += f'={ast.unparse(default)}'
                args.append(arg_str)

            lines.append(f'    def {node.name}({", ".join(args)}):')

            # For __init__, include the body
            if node.name == '__init__':
                for stmt in node.body:
                    if isinstance(stmt, ast.Expr) and isinstance(stmt.value, ast.Constant):
                        continue  # Skip docstrings
                    lines.append(f'        {ast.unparse(stmt)}')
            else:
                lines.append('        pass')

    return '\n'.join(lines)


def generate_template(solution_path: Path) -> str:
    """Generate template content from a solution file."""
    source = solution_path.read_text(encoding='utf-8')

    try:
        tree = ast.parse(source)
    except SyntaxError as e:
        print(f"  Syntax error in {solution_path}: {e}")
        return None

    lines = []

    # Add imports
    imports = extract_imports(source)
    if imports:
        lines.extend(imports)
        lines.append('')

    # Add helper classes
    helpers = extract_helper_classes(tree)
    for helper in helpers:
        lines.append(create_helper_class_source(helper))
        lines.append('')

    # Add Solution class
    solution_class = get_solution_class(tree)
    if solution_class:
        lines.append('class Solution:')

        for node in solution_class.body:
            if isinstance(node, ast.FunctionDef):
                # Skip private methods and alternative implementations
                if node.name.startswith('_') and node.name != '__init__':
                    continue
                if '_bruteforce' in node.name or '_alternative' in node.name:
                    continue

                lines.append(create_method_signature(node))

    return '\n'.join(lines)


def main():
    problems_dir = Path(__file__).parent.parent / 'problems'

    if not problems_dir.exists():
        print(f"Problems directory not found: {problems_dir}")
        return

    count = 0
    errors = 0

    for solution_path in problems_dir.rglob('solution.py'):
        template_path = solution_path.parent / 'template.py'

        print(f"Processing: {solution_path.parent.name}")

        template_content = generate_template(solution_path)

        if template_content:
            template_path.write_text(template_content, encoding='utf-8')
            count += 1
        else:
            errors += 1

    print(f"\nGenerated {count} templates, {errors} errors")


if __name__ == '__main__':
    main()
