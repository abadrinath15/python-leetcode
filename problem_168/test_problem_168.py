import pytest
from problem_168 import Solution


class TestCase:
    def test_1(self, get_sln: Solution) -> None:
        input_1 = 1
        assert get_sln.convertToTitle(input_1) == "A"


@pytest.fixture
def get_sln() -> Solution:
    return Solution()
