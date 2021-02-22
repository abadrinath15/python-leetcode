import pytest
from problem_119 import Solution


class TestCase:
    def test_1(self, get_sln):
        assert get_sln.getRow(0) == [1]

    def test_2(self, get_sln):
        assert get_sln.getRow(1) == [1, 1]

    def test_3(self, get_sln):
        assert get_sln.getRow(2) == [1, 2, 1]

    def test_4(self, get_sln):
        assert get_sln.getRow(3) == [1, 3, 3, 1]


@pytest.fixture
def get_sln():
    return Solution()
