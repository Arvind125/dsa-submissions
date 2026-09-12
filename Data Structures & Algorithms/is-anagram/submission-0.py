class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        f = [0] * 26
        for i in range(len(s)):
            # f[s[i] - 'a']+= 1
            # f[t[i] - 'a']+= 1
            f[ord(s[i]) - ord('a')] += 1
            f[ord(t[i]) - ord('a')] -= 1


        for i in range(26):
            if f[i] != 0:
                return False
        return True

