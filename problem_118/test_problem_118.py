import pytest
from problem_118 import Solution


class TestCase:
    def test_1(self, get_sln):
        assert get_sln.generate(0) == []

    def test_2(self, get_sln):
        assert get_sln.generate(1) == [[1]]

    def test_3(self, get_sln):
        assert get_sln.generate(2) == [[1], [1, 1]]

    def test_4(self, get_sln):
        assert get_sln.generate(3) == [[1], [1, 1], [1, 2, 1]]


@pytest.fixture
def get_sln():
    return Solution()
