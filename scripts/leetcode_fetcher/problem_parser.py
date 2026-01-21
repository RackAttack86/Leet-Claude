"""
Problem Parser

Parses LeetCode problem data to extract function signatures, descriptions,
constraints, and examples.
"""

import re
import html
from typing import Dict, Any, List, Tuple, Optional


class ProblemParser:
    """Parses raw LeetCode problem data into structured format."""

    def parse(self, raw_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Parse raw API response into structured problem data.

        Args:
            raw_data: Raw response from LeetCode GraphQL API

        Returns:
            Structured problem data dictionary
        """
        # Extract Python3 code snippet for signature
        signature = self._extract_python_signature(
            raw_data.get("codeSnippets", [])
        )

        # Parse HTML content to text
        content = raw_data.get("content", "") or ""
        description = self._html_to_text(content)

        # Extract examples from description
        examples = self._extract_examples(description, raw_data)

        # Extract constraints
        constraints = self._extract_constraints(description)

        # Clean up description (remove examples and constraints sections)
        clean_description = self._clean_description(description)

        # Get topics
        topics = [t["name"] for t in raw_data.get("topicTags", [])]

        return {
            "number": int(raw_data.get("questionFrontendId", 0)),
            "title": raw_data.get("title", ""),
            "slug": raw_data.get("titleSlug", ""),
            "difficulty": raw_data.get("difficulty", "Medium"),
            "description": clean_description,
            "constraints": constraints,
            "examples": examples,
            "topics": topics,
            "signature": signature,
            "hints": raw_data.get("hints", []),
        }

    def _extract_python_signature(
        self,
        code_snippets: List[Dict[str, str]]
    ) -> Optional[Dict[str, Any]]:
        """Extract function signature from Python3 code template."""
        python_code = None

        for snippet in code_snippets:
            if snippet.get("langSlug") == "python3":
                python_code = snippet.get("code", "")
                break

        if not python_code:
            return None

        return self._parse_python_template(python_code)

    def _parse_python_template(self, code: str) -> Optional[Dict[str, Any]]:
        """Parse Python template to extract method info."""
        # Find all method definitions inside the class
        method_pattern = r'def\s+(\w+)\s*\(\s*self\s*(?:,\s*(.+?))?\s*\)\s*(?:->\s*(.+?))?\s*:'

        matches = list(re.finditer(method_pattern, code, re.DOTALL))

        if not matches:
            return None

        # For design problems (multiple methods), return all methods
        # For regular problems, return the first non-__init__ method
        methods = []
        primary_method = None

        for match in matches:
            method_name = match.group(1)
            params_str = match.group(2) or ""
            return_type = match.group(3)

            # Clean up params string (remove newlines, extra spaces)
            params_str = " ".join(params_str.split())

            # Parse parameters
            params = self._parse_params(params_str)

            # Clean return type
            if return_type:
                return_type = return_type.strip()

            method_info = {
                "method_name": method_name,
                "params": params,
                "return_type": return_type,
            }
            methods.append(method_info)

            # Primary method is the first non-__init__ method
            if method_name != "__init__" and primary_method is None:
                primary_method = method_info

        # If we only have __init__, use it as primary
        if primary_method is None and methods:
            primary_method = methods[0]

        if primary_method:
            primary_method["raw_code"] = code
            primary_method["all_methods"] = methods
            primary_method["is_design_problem"] = len(methods) > 1

        return primary_method

    def _parse_params(self, params_str: str) -> List[Tuple[str, str]]:
        """Parse parameter string into list of (name, type) tuples."""
        if not params_str.strip():
            return []

        params = []
        current_param = ""
        bracket_depth = 0

        for char in params_str + ",":
            if char in "[({":
                bracket_depth += 1
            elif char in "])}":
                bracket_depth -= 1

            if char == "," and bracket_depth == 0:
                if current_param.strip():
                    params.append(self._parse_single_param(current_param.strip()))
                current_param = ""
            else:
                current_param += char

        return params

    def _parse_single_param(self, param: str) -> Tuple[str, str]:
        """Parse 'name: Type' into (name, type) tuple."""
        if ":" in param:
            parts = param.split(":", 1)
            name = parts[0].strip()
            type_hint = parts[1].strip()
            return (name, type_hint)
        return (param.strip(), "Any")

    def _html_to_text(self, html_content: str) -> str:
        """Convert HTML content to plain text."""
        if not html_content:
            return ""

        # Unescape HTML entities
        text = html.unescape(html_content)

        # Replace common tags with appropriate text
        text = re.sub(r'<br\s*/?>', '\n', text)
        text = re.sub(r'<p>', '\n', text)
        text = re.sub(r'</p>', '\n', text)
        text = re.sub(r'<li>', '\n- ', text)
        text = re.sub(r'<code>', '`', text)
        text = re.sub(r'</code>', '`', text)
        text = re.sub(r'<pre>', '\n```\n', text)
        text = re.sub(r'</pre>', '\n```\n', text)
        text = re.sub(r'<strong>', '', text)  # Remove bold markers for cleaner parsing
        text = re.sub(r'</strong>', '', text)
        text = re.sub(r'<em>', '', text)
        text = re.sub(r'</em>', '', text)
        text = re.sub(r'<sup>', '^', text)
        text = re.sub(r'</sup>', '', text)

        # Remove remaining HTML tags
        text = re.sub(r'<[^>]+>', '', text)

        # Clean up whitespace
        text = re.sub(r'\n\s*\n\s*\n', '\n\n', text)
        text = text.strip()

        return text

    def _extract_examples(
        self,
        description: str,
        raw_data: Dict[str, Any]
    ) -> List[str]:
        """Extract examples from description."""
        examples = []

        # Pattern to find examples
        pattern = r'(?:\*\*)?Example\s*(\d+)(?:\*\*)?:?\s*(.*?)(?=(?:\*\*)?Example\s*\d|Constraints|$)'
        matches = re.findall(pattern, description, re.DOTALL | re.IGNORECASE)

        for num, content in matches:
            cleaned = content.strip()
            if cleaned:
                # Format example nicely
                example_text = f"Example {num}:\n{cleaned}"
                examples.append(example_text)

        # Fallback to test cases if no examples found
        if not examples:
            test_cases = raw_data.get("exampleTestcaseList", [])
            for i, tc in enumerate(test_cases, 1):
                examples.append(f"Example {i}:\nInput: {tc}\nOutput: [See LeetCode]")

        return examples

    def _extract_constraints(self, description: str) -> List[str]:
        """Extract constraints from description."""
        constraints = []

        # Find constraints section
        pattern = r'(?:\*\*)?Constraints(?:\*\*)?:?\s*(.*?)(?=\n\n|Follow|Note:|$)'
        match = re.search(pattern, description, re.DOTALL | re.IGNORECASE)

        if match:
            text = match.group(1).strip()
            # Split by bullet points, newlines, or list markers
            items = re.split(r'\n\s*[-•*]\s*|\n\s*`', text)

            for item in items:
                cleaned = item.strip().strip('`').strip()
                if cleaned and len(cleaned) > 2:
                    # Remove leading bullet markers
                    cleaned = re.sub(r'^[-•*]\s*', '', cleaned)
                    constraints.append(cleaned)

        return constraints

    def _clean_description(self, description: str) -> str:
        """Remove examples and constraints from description to get core problem statement."""
        # Remove everything from "Example 1" onwards
        text = re.split(r'(?:\*\*)?Example\s*1', description, flags=re.IGNORECASE)[0]

        # Clean up
        text = text.strip()

        return text


def get_required_imports(signature: Optional[Dict[str, Any]]) -> List[str]:
    """
    Determine which imports are needed based on types used.

    Args:
        signature: Parsed function signature dictionary

    Returns:
        List of required import names from typing module
    """
    if not signature:
        return ["List", "Optional"]

    all_types = [p[1] for p in signature.get("params", [])]
    return_type = signature.get("return_type", "") or ""
    all_types.append(return_type)

    type_str = " ".join(all_types)

    imports = set()
    if "List" in type_str:
        imports.add("List")
    if "Optional" in type_str:
        imports.add("Optional")
    if "Dict" in type_str:
        imports.add("Dict")
    if "Tuple" in type_str:
        imports.add("Tuple")
    if "Set" in type_str:
        imports.add("Set")

    # Always include these common ones
    imports.add("List")
    imports.add("Optional")

    return sorted(list(imports))


def needs_helper_class(signature: Optional[Dict[str, Any]], class_name: str) -> bool:
    """
    Check if a helper class (ListNode, TreeNode, etc.) is needed.

    Args:
        signature: Parsed function signature
        class_name: Name of helper class to check for

    Returns:
        True if the class is referenced in the signature
    """
    if not signature:
        return False

    type_str = str(signature)
    return class_name in type_str
