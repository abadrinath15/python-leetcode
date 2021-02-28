import pytest
from problem_345 import Solution


@pytest.fixture
def get_sln():
    return Solution()


class TestReverseVowels:
    def test_rv_1(self, get_sln):
        s = "hello"
        assert get_sln.reverseVowels(s) == "holle"

    def test_rv_3(self, get_sln):
        s = "leetcode"
        assert get_sln.reverseVowels(s) == "leotcede"
