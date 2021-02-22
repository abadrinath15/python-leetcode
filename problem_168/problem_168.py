class Solution:
    def convertToTitle(self, n: int) -> str:
        char_int_map = {
            val: chr(letter)
            for letter, val in zip(range(ord("A"), ord("Z") + 1), range(1, 27))
        }
        print(char_int_map)
