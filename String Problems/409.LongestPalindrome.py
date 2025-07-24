class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = {}
        for c in s:
            d[c] = d.get(c,0) + 1
        
        res = 0
        odd_frequency = False
        for freq in d.values():
            if freq % 2 == 0:
                res+= freq
            else:
                res += freq - 1
                odd_frequency = True
        if odd_frequency:
            return res + 1
        
        return res
