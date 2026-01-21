"""
LeetCode GraphQL API Client

Fetches problem data from LeetCode's GraphQL endpoint with rate limiting
and error handling.
"""

import time
import requests
from typing import Optional, Dict, Any, List


# GraphQL query to fetch complete problem details
PROBLEM_QUERY = """
query questionData($titleSlug: String!) {
    question(titleSlug: $titleSlug) {
        questionId
        questionFrontendId
        title
        titleSlug
        difficulty
        content
        topicTags {
            name
            slug
        }
        codeSnippets {
            langSlug
            code
        }
        exampleTestcaseList
        sampleTestCase
        hints
        stats
    }
}
"""

# GraphQL query to fetch paginated problem list
PROBLEM_LIST_QUERY = """
query problemsetQuestionList($categorySlug: String, $limit: Int, $skip: Int, $filters: QuestionListFilterInput) {
    problemsetQuestionList: questionList(
        categorySlug: $categorySlug
        limit: $limit
        skip: $skip
        filters: $filters
    ) {
        total: totalNum
        questions: data {
            questionFrontendId
            title
            titleSlug
            difficulty
            paidOnly: isPaidOnly
            acRate
            topicTags {
                name
                slug
            }
        }
    }
}
"""


class LeetCodeClient:
    """Client for interacting with LeetCode's GraphQL API."""

    BASE_URL = "https://leetcode.com/graphql"

    def __init__(self, rate_limit_delay: float = 1.5):
        """
        Initialize the LeetCode API client.

        Args:
            rate_limit_delay: Seconds to wait between requests (default 1.5s)
        """
        self.session = requests.Session()
        self.session.headers.update({
            "Content-Type": "application/json",
            "Referer": "https://leetcode.com",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Origin": "https://leetcode.com",
        })
        self.rate_limit_delay = rate_limit_delay
        self._last_request_time = 0.0

    def _rate_limit(self) -> None:
        """Enforce rate limiting between requests."""
        elapsed = time.time() - self._last_request_time
        if elapsed < self.rate_limit_delay:
            time.sleep(self.rate_limit_delay - elapsed)
        self._last_request_time = time.time()

    def _make_request(
        self,
        query: str,
        variables: Dict[str, Any],
        max_retries: int = 3
    ) -> Optional[Dict[str, Any]]:
        """
        Make a GraphQL request with retry logic.

        Args:
            query: GraphQL query string
            variables: Query variables
            max_retries: Maximum number of retry attempts

        Returns:
            Response data or None if request failed
        """
        self._rate_limit()

        for attempt in range(max_retries):
            try:
                response = self.session.post(
                    self.BASE_URL,
                    json={"query": query, "variables": variables},
                    timeout=30
                )

                if response.status_code == 429:
                    # Rate limited - exponential backoff
                    wait_time = 2 ** attempt * 5
                    print(f"Rate limited. Waiting {wait_time}s...")
                    time.sleep(wait_time)
                    continue

                response.raise_for_status()
                data = response.json()

                if "errors" in data:
                    print(f"GraphQL errors: {data['errors']}")
                    return None

                return data.get("data")

            except requests.Timeout:
                print(f"Request timed out (attempt {attempt + 1}/{max_retries})")
                time.sleep(2 ** attempt)
            except requests.RequestException as e:
                print(f"Request error: {e}")
                if attempt < max_retries - 1:
                    time.sleep(2 ** attempt)

        return None

    def fetch_problem(self, title_slug: str) -> Optional[Dict[str, Any]]:
        """
        Fetch complete problem data by slug.

        Args:
            title_slug: The URL slug of the problem (e.g., "two-sum")

        Returns:
            Problem data dictionary or None if not found
        """
        data = self._make_request(PROBLEM_QUERY, {"titleSlug": title_slug})
        if data:
            return data.get("question")
        return None

    def fetch_problem_list(
        self,
        skip: int = 0,
        limit: int = 50,
        difficulty: Optional[str] = None,
        tags: Optional[List[str]] = None,
        paid_only: Optional[bool] = None
    ) -> List[Dict[str, Any]]:
        """
        Fetch paginated list of problems with optional filters.

        Args:
            skip: Number of problems to skip (for pagination)
            limit: Maximum number of problems to fetch
            difficulty: Filter by difficulty ("EASY", "MEDIUM", "HARD")
            tags: Filter by topic tags
            paid_only: Filter by premium status (True/False/None)

        Returns:
            List of problem summaries
        """
        filters: Dict[str, Any] = {}
        if difficulty:
            filters["difficulty"] = difficulty.upper()
        if tags:
            filters["tags"] = tags

        data = self._make_request(
            PROBLEM_LIST_QUERY,
            {
                "categorySlug": "",
                "skip": skip,
                "limit": limit,
                "filters": filters
            }
        )

        if data:
            questions = data.get("problemsetQuestionList", {}).get("questions", [])
            # Filter by paid status if specified
            if paid_only is not None:
                questions = [q for q in questions if q.get("paidOnly") == paid_only]
            return questions
        return []

    def fetch_all_problems(
        self,
        difficulty: Optional[str] = None,
        exclude_premium: bool = True,
        min_acceptance: float = 0.0
    ) -> List[Dict[str, Any]]:
        """
        Fetch all problems matching criteria (handles pagination).

        Args:
            difficulty: Filter by difficulty
            exclude_premium: If True, exclude premium problems
            min_acceptance: Minimum acceptance rate (0.0 to 100.0)

        Returns:
            List of all matching problems
        """
        all_problems = []
        skip = 0
        batch_size = 100

        while True:
            print(f"Fetching problems {skip} to {skip + batch_size}...")
            batch = self.fetch_problem_list(
                skip=skip,
                limit=batch_size,
                difficulty=difficulty
            )

            if not batch:
                break

            # Apply filters
            for problem in batch:
                if exclude_premium and problem.get("paidOnly"):
                    continue
                if problem.get("acRate", 0) < min_acceptance:
                    continue
                all_problems.append(problem)

            if len(batch) < batch_size:
                break

            skip += batch_size

        return all_problems

    def get_slug_from_number(self, problem_number: int) -> Optional[str]:
        """
        Find a problem's slug by its number.

        Args:
            problem_number: The problem ID (e.g., 1 for Two Sum)

        Returns:
            The problem slug or None if not found
        """
        # Fetch in batches to find the problem
        skip = 0
        batch_size = 100

        while skip < 3000:  # LeetCode has ~3000 problems
            batch = self.fetch_problem_list(skip=skip, limit=batch_size)

            if not batch:
                break

            for problem in batch:
                if int(problem.get("questionFrontendId", 0)) == problem_number:
                    return problem.get("titleSlug")

            skip += batch_size

        return None
