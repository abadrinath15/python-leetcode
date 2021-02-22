import math


class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True
        s_filt = list(map(str.lower, filter(str.isalnum, s)))
        mid = math.ceil(len(s_filt) / 2)
        for letter, letter_rev in zip(s_filt[:mid], reversed(s_filt)):
            if letter != letter_rev:
                return False
        return True
