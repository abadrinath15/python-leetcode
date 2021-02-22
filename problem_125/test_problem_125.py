import pytest
from problem_125 import Solution


class TestCase:
    def test_1(self, get_sln):
        input_str = "A man, a plan, a canal: Panama"
        assert get_sln.isPalindrome(input_str) == True

    def test_2(self, get_sln):
        input_str = "race a car"
        assert get_sln.isPalindrome(input_str) == False

    def test_3(self, get_sln):
        input_str = ""
        assert get_sln.isPalindrome(input_str) == True


@pytest.fixture
def get_sln():
    return Solution()
