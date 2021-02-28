class Solution:
    def reverseVowels(self, s: str) -> str:
        s_list = list(s)
        fwd_ind = 0
        rev_ind = -1
        char_set = set("AaEeIiOoUu")
        while fwd_ind < len(s) + rev_ind:
            fwd_char = s_list[fwd_ind]
            rev_char = s_list[rev_ind]
            if {fwd_char, rev_char}.issubset(char_set):
                s_list[fwd_ind], s_list[rev_ind] = rev_char, fwd_char
                fwd_ind += 1
                rev_ind -= 1
            elif fwd_char in char_set:
                rev_ind -= 1
            else:
                fwd_ind += 1

        return "".join(s_list)
