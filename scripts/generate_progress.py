"""
Script to generate a progress report showing completed problems
Usage: python scripts/generate_progress.py
"""

import json
from pathlib import Path
from collections import defaultdict
from typing import Dict, List
import importlib.util


def load_problem_metadata(problem_dir: Path) -> Dict:
    """Load metadata from a problem's solution.py"""
    solution_file = problem_dir / "solution.py"
    if not solution_file.exists():
        return None

    try:
        # Load module
        spec = importlib.util.spec_from_file_location("solution", solution_file)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        if hasattr(module, "PROBLEM_METADATA"):
            return module.PROBLEM_METADATA
    except Exception as e:
        print(f"Error loading {solution_file}: {e}")

    return None


def generate_progress_report():
    """Generate a comprehensive progress report"""

    problems_dir = Path("problems")
    if not problems_dir.exists():
        print("Error: problems/ directory not found")
        return

    # Collect all problems
    problems_by_pattern = defaultdict(list)
    problems_by_difficulty = defaultdict(list)
    all_problems = []

    for pattern_dir in sorted(problems_dir.iterdir()):
        if not pattern_dir.is_dir() or pattern_dir.name.startswith("__"):
            continue

        pattern_name = pattern_dir.name

        for problem_dir in sorted(pattern_dir.iterdir()):
            if not problem_dir.is_dir() or problem_dir.name.startswith("__"):
                continue

            metadata = load_problem_metadata(problem_dir)
            if metadata:
                problems_by_pattern[pattern_name].append(metadata)
                problems_by_difficulty[metadata.get("difficulty", "Unknown")].append(metadata)
                all_problems.append(metadata)

    # Generate report
    print("=" * 70)
    print("LEETCODE PROGRESS REPORT")
    print("=" * 70)

    # Summary
    print(f"\nSUMMARY")
    print(f"{'-' * 70}")
    print(f"Total Problems Solved: {len(all_problems)}")
    print(f"Easy: {len(problems_by_difficulty['Easy'])}")
    print(f"Medium: {len(problems_by_difficulty['Medium'])}")
    print(f"Hard: {len(problems_by_difficulty['Hard'])}")

    # By Pattern
    print(f"\nPROBLEMS BY PATTERN")
    print(f"{'-' * 70}")
    for pattern, problems in sorted(problems_by_pattern.items()):
        print(f"\n{pattern.replace('_', ' ').title()} ({len(problems)} problems)")
        for p in sorted(problems, key=lambda x: x['number']):
            difficulty_emoji = {"Easy": "Easy", "Medium": "Med", "Hard": "Hard"}.get(p['difficulty'], "?")
            print(f"  [{difficulty_emoji:4}] #{p['number']}: {p['name']}")

    # Recent problems
    if all_problems:
        print(f"\nRECENT PROBLEMS")
        print(f"{'-' * 70}")
        recent = sorted(all_problems, key=lambda x: x['number'], reverse=True)[:10]
        for p in recent:
            difficulty_emoji = {"Easy": "Easy", "Medium": "Med", "Hard": "Hard"}.get(p['difficulty'], "?")
            print(f"  [{difficulty_emoji:4}] #{p['number']}: {p['name']} ({p['pattern']})")

    print(f"\n{'=' * 70}\n")


if __name__ == "__main__":
    generate_progress_report()
