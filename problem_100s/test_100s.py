import pytest
import sys

sys.path.append(r"/Users/aditya/Documents/Python/Leetcode")
from helpers.linked_list import ListNode, list_to_linked_list
from problem_100s import Solution


class TestAddTwoNumbers:
    def test_atn_1(self, get_sln):
        l1 = list_to_linked_list([2, 4, 3])
        l2 = list_to_linked_list([5, 6, 4])
        ans = list_to_linked_list([7, 0, 8])
        assert get_sln.addTwoNumbers(l1, l2) == ans

    def test_atn_2(self, get_sln):
        l1 = list_to_linked_list([0])
        l2 = list_to_linked_list([0])
        ans = list_to_linked_list([0])
        assert get_sln.addTwoNumbers(l1, l2) == ans

    def test_atn_3(self, get_sln):
        l1 = list_to_linked_list([9] * 7)
        l2 = list_to_linked_list([9] * 4)
        ans = list_to_linked_list([8] + [9] * 3 + [0] * 3 + [1])
        assert get_sln.addTwoNumbers(l1, l2) == ans

    def test_atn_4(self, get_sln):
        l1 = list_to_linked_list([2, 4, 9])
        l2 = list_to_linked_list([5, 6, 4, 9])
        ans = list_to_linked_list([7, 0, 4, 0, 1])
        assert get_sln.addTwoNumbers(l1, l2) == ans


class TestLongestPalindrome:
    def test_ip_1(self, get_sln):
        s = "babad"
        output = "bab"
        assert get_sln.longestPalindrome(s) == output

    def test_ip_2(self, get_sln):
        s = "cbbd"
        output = "bb"
        assert get_sln.longestPalindrome(s) == output

    def test_ip_3(self, get_sln):
        s = "a"
        output = "a"
        assert get_sln.longestPalindrome(s) == output

    def test_ip_4(self, get_sln):
        s = "ac"
        output = "a"
        assert get_sln.longestPalindrome(s) == output

    def test_ip_5(self, get_sln):
        s = "bb"
        output = "bb"
        assert get_sln.longestPalindrome(s) == output

    def test_ip_6(self, get_sln):
        s = "bbb"
        output = "bbb"
        assert get_sln.longestPalindrome(s) == output

    def test_ip_7(self, get_sln):
        s = "aaaa"
        output = "aaaa"
        assert get_sln.longestPalindrome(s) == output

    def test_ip_8(self, get_sln):
        s = "aacabdkacaa"
        output = "aca"
        assert get_sln.longestPalindrome(s) == output

    def test_ip_9(self, get_sln):
        s = "a" * 4 + "b" * 3
        output = "a" * 4
        assert get_sln.longestPalindrome(s) == output


class TestMaxArea:
    def test_ma_1(self, get_sln):
        height = [1, 1]
        output = 1
        assert get_sln.maxArea(height) == output

    def test_ma_2(self, get_sln):
        height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
        output = 49
        assert get_sln.maxArea(height) == output

    def test_ma_3(self, get_sln):
        height = [1, 2, 1]
        output = 2
        assert get_sln.maxArea(height) == output

    def test_ma_4(self, get_sln):
        height = [2, 3, 4, 5, 18, 17, 6]
        output = 17
        assert get_sln.maxArea(height) == output


class TestIntToRoman:
    def test_itr_1(self, get_sln):
        num = 3
        assert get_sln.intToRoman(num) == "III"

    def test_itr_2(self, get_sln):
        num = 4
        assert get_sln.intToRoman(num) == "IV"

    def test_itr_3(self, get_sln):
        num = 9
        assert get_sln.intToRoman(num) == "IX"

    def test_itr_4(self, get_sln):
        num = 58
        assert get_sln.intToRoman(num) == "LVIII"

    def test_itr_5(self, get_sln):
        num = 1994
        assert get_sln.intToRoman(num) == "MCMXCIV"

    def test_itr_6(self, get_sln):
        num = 10
        assert get_sln.intToRoman(num) == "X"


class TestLetterCombinations:
    def test_lc_1(self, get_sln):
        digits = "23"
        output = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
        assert get_sln.letterCombinations(digits) == output

    def test_lc_2(self, get_sln):
        digits = ""
        output = []
        assert get_sln.letterCombinations(digits) == output

    def test_lc_3(self, get_sln):
        digits = "2"
        output = ["a", "b", "c"]
        assert get_sln.letterCombinations(digits) == output

    def test_lc_4(self, get_sln):
        digits = "9"
        output = ["w", "x", "y", "z"]
        assert get_sln.letterCombinations(digits) == output


class TestThreeSums:
    def test_ts_1(self, get_sln):
        input_list = [-1, 0, 1, 2, -1, -4]
        output_lists = [[-1, -1, 2], [-1, 0, 1]]
        assert sorted(get_sln.threeSum(input_list)) == sorted(output_lists)


class TestGenerateParenthesis:
    def test_gp_1(self, get_sln):
        n = 1
        correct = sorted(["()"])
        assert sorted(get_sln.generateParenthesis(n)) == correct

    def test_gp_2(self, get_sln):
        n = 2
        correct = sorted(["(())", "()()"])
        assert sorted(get_sln.generateParenthesis(n)) == correct

    def test_gp_3(self, get_sln):
        n = 3
        correct = sorted(["((()))", "(()())", "(())()", "()(())", "()()()"])
        assert sorted(get_sln.generateParenthesis(n)) == correct


@pytest.fixture
def get_sln():
    return Solution()
