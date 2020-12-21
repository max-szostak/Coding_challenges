""" Given a string s, return the last substring of s in lexicographical order. """



class Solution:
    def lastSubstring(self, s: str) -> str:
        n = len(s)
        mi = n - 1
        for i in range(n - 2, -1, -1):
            if s[i] > s[mi]:
                mi = i
            elif s[i] == s[mi]:
                if s[i:mi] >= s[mi:2*mi-i]: # mi+(mi-i)=2*mi-i
                    mi = i         
        return s[mi:]

sol = Solution()
print(sol.lastSubstring("leetcode"))