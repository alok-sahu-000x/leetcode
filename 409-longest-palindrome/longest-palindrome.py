class Solution:
    def longestPalindrome(self, s: str) -> int:
        from collections import Counter

        count = Counter(s)
        length = 0
        has_odd = False

        for v in count.values():
            length += v // 2 * 2
            if v % 2 == 1:
                has_odd = True

        if has_odd:
            length += 1

        return length

        