class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_num = 0
        t_num = 0

        while t_num < len(t) and s_num < len(s):
            if t[t_num] == s[s_num]:
                s_num += 1
            t_num += 1

        return s_num == len(s)