#!/usr/bin/env python3
"""
Script to reorganize problems by difficulty within each pattern folder.
Creates easy/medium/hard subdirectories and moves problem folders accordingly.
"""

import os
import shutil
import re
from pathlib import Path

def extract_difficulty(solution_file):
    """Extract difficulty from PROBLEM_METADATA in solution.py"""
    try:
        with open(solution_file, 'r', encoding='utf-8') as f:
            content = f.read()
            # Look for difficulty in PROBLEM_METADATA
            match = re.search(r'"difficulty":\s*"(\w+)"', content)
            if match:
                return match.group(1).lower()
    except Exception as e:
        print(f"Error reading {solution_file}: {e}")
    return None

def reorganize_problems():
    """Main function to reorganize all problems by difficulty"""
    problems_dir = Path('problems')

    # Get all pattern directories
    pattern_dirs = [d for d in problems_dir.iterdir()
                   if d.is_dir() and not d.name.startswith('_')]

    moves = []  # Track all moves to perform

    for pattern_dir in pattern_dirs:
        print(f"\nProcessing pattern: {pattern_dir.name}")

        # Get all problem directories (start with p followed by digits)
        problem_dirs = [d for d in pattern_dir.iterdir()
                       if d.is_dir() and re.match(r'^p\d+_', d.name)]

        for problem_dir in problem_dirs:
            solution_file = problem_dir / 'solution.py'
            if solution_file.exists():
                difficulty = extract_difficulty(solution_file)
                if difficulty:
                    moves.append((problem_dir, pattern_dir, difficulty))
                    print(f"  {problem_dir.name} -> {difficulty}")
                else:
                    print(f"  WARNING: Could not extract difficulty from {problem_dir.name}")
            else:
                print(f"  WARNING: No solution.py in {problem_dir.name}")

    print(f"\n{'='*60}")
    print(f"Total problems to reorganize: {len(moves)}")
    print(f"{'='*60}\n")

    # Create difficulty directories and move problems
    for problem_dir, pattern_dir, difficulty in moves:
        difficulty_dir = pattern_dir / difficulty
        difficulty_dir.mkdir(exist_ok=True)

        new_location = difficulty_dir / problem_dir.name
        print(f"Moving {problem_dir.relative_to(problems_dir)} -> {new_location.relative_to(problems_dir)}")
        shutil.move(str(problem_dir), str(new_location))

    print(f"\n{'='*60}")
    print("Reorganization complete!")
    print(f"{'='*60}")

if __name__ == '__main__':
    reorganize_problems()
