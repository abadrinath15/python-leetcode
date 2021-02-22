import pytest
import sys

sys.path.append(r"/Users/aditya/Documents/Python/Leetcode/")
import helpers.linked_list as ll
from solutions_200s import Solution


class TestIsHappy:
    def test_ih_1(self, get_sln):
        assert get_sln.isHappy(1) == True

    def test_ih_2(self, get_sln):
        assert get_sln.isHappy(2) == False

    def test_ih_3(self, get_sln):
        assert get_sln.isHappy(19) == True


class TestRemoveElements:
    def test_re_1(self, get_sln):
        input_ll = ll.list_to_linked_list([1, 2, 6, 3, 4, 5, 6])
        output_ll = ll.list_to_linked_list([1, 2, 3, 4, 5])
        assert get_sln.removeElements(input_ll, 6) == output_ll

    def test_re_2(self, get_sln):
        input_ll = ll.list_to_linked_list([1, 1])
        output_ll = ll.list_to_linked_list([])
        assert get_sln.removeElements(input_ll, 1) == output_ll

    def test_re_3(self, get_sln):
        input_ll = ll.list_to_linked_list([1, 2, 2, 1])
        output_ll = ll.list_to_linked_list([1, 1])
        assert get_sln.removeElements(input_ll, 2) == output_ll


class TestCountPrimes:
    def test_cp_1(self, get_sln):
        assert get_sln.countPrimes(1) == 0

    def test_cp_2(self, get_sln):
        assert get_sln.countPrimes(2) == 0

    def test_cp_3(self, get_sln):
        assert get_sln.countPrimes(0) == 0

    def test_cp_4(self, get_sln):
        assert get_sln.countPrimes(10) == 4

    def test_cp_5(self, get_sln):
        assert get_sln.countPrimes(4) == 2

    def test_cp_6(self, get_sln):
        assert get_sln.countPrimes(7) == 3

    def test_cp_7(self, get_sln):
        assert get_sln.countPrimes(11) == 4


class TestIsIsomorphic:
    def test_is_1(self, get_sln):
        input_s = "egg"
        input_t = "add"
        assert get_sln.isIsomorphic(input_s, input_t) == True

    def test_is_2(self, get_sln):
        input_s = "foo"
        input_t = "bar"
        assert get_sln.isIsomorphic(input_s, input_t) == False

    def test_is_3(self, get_sln):
        input_s = "paper"
        input_t = "title"
        assert get_sln.isIsomorphic(input_s, input_t) == True


class TestReverseList:
    def test_rl_1(self, get_sln):
        input_tree = ll.list_to_linked_list([1, 2, 3, 4, 5])
        output_tree = ll.list_to_linked_list([5, 4, 3, 2, 1])
        assert get_sln.reverseList(input_tree) == output_tree


class TestContainsDuplicates:
    def test_cd_1(self, get_sln):
        input_list = []
        assert get_sln.containsDuplicate(input_list) == False

    def test_cd_2(self, get_sln):
        input_list = [1, 2, 3, 1]
        assert get_sln.containsDuplicate(input_list) == True

    def test_cd_3(self, get_sln):
        input_list = [1, 2, 3, 4]
        assert get_sln.containsDuplicate(input_list) == False


class TestContainsNearbyDuplicate:
    def test_cnd_1(self, get_sln):
        input_list = []
        k = 1
        assert get_sln.containsNearbyDuplicate(input_list, k) == False

    def test_cnd_2(self, get_sln):
        input_list = [1, 2, 3, 1]
        k = 3
        assert get_sln.containsNearbyDuplicate(input_list, k) == True

    def test_cnd_3(self, get_sln):
        input_list = [1, 0, 1, 1]
        k = 1
        assert get_sln.containsNearbyDuplicate(input_list, k) == True

    def test_cnd_4(self, get_sln):
        input_list = [1, 2, 3, 1, 2, 3]
        k = 2
        assert get_sln.containsNearbyDuplicate(input_list, k) == False


class TestSummaryRanges:
    def test_sr_1(self, get_sln):
        input_list = []
        assert get_sln.summaryRanges(input_list) == []

    def test_sr_2(self, get_sln):
        input_list = [1]
        assert get_sln.summaryRanges(input_list) == ["1"]

    def test_sr_3(self, get_sln):
        input_list = [1, 2]
        assert get_sln.summaryRanges(input_list) == ["1->2"]

    def test_sr_4(self, get_sln):
        input_list = [1, 2, 4, 5]
        assert get_sln.summaryRanges(input_list) == ["1->2", "4->5"]

    def test_sr_5(self, get_sln):
        input_list = [0, 1, 2, 4, 5, 7]
        assert get_sln.summaryRanges(input_list) == ["0->2", "4->5", "7"]

    def test_sr_6(self, get_sln):
        input_list = [0, 2, 4, 6]
        assert get_sln.summaryRanges(input_list) == ["0", "2", "4", "6"]

    def test_sr_7(self, get_sln):
        input_list = [0, 2, 3, 4, 6, 8, 9]
        assert get_sln.summaryRanges(input_list) == ["0", "2->4", "6", "8->9"]

    def test_sr_8(self, get_sln):
        input_list = [0]
        assert get_sln.summaryRanges(input_list) == ["0"]


class TestIsPalindrome:
    def test_ip_1(self, get_sln):
        input_list = [1, 2]
        assert get_sln.isPalindrome(ll.list_to_linked_list(input_list)) == False

    def test_ip_2(self, get_sln):
        input_list = []
        assert get_sln.isPalindrome(ll.list_to_linked_list(input_list)) == True

    def test_ip_3(self, get_sln):
        input_list = [1, 2, 1]
        assert get_sln.isPalindrome(ll.list_to_linked_list(input_list)) == True

    def test_ip_4(self, get_sln):
        input_list = [1, 2, 2, 1]
        assert get_sln.isPalindrome(ll.list_to_linked_list(input_list)) == True

    def test_ip_5(self, get_sln):
        input_list = [1, 2, 1, 2]
        assert get_sln.isPalindrome(ll.list_to_linked_list(input_list)) == False


class TestMoveZeros:
    def test_mz_1(self, get_sln):
        input_list = [0, 1, 0, 3, 12]
        output_list = [1, 3, 12, 0, 0]
        get_sln.moveZeros(input_list)
        assert input_list == output_list

    def test_mz_2(self, get_sln):
        input_list = [0, 0, 1]
        output_list = [1, 0, 0]
        get_sln.moveZeros(input_list)
        assert input_list == output_list


@pytest.fixture
def get_sln():
    return Solution()
