class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        min_len = min(len(s) for s in strs)
        n = len(strs)
        ans = ""

        for j in range(min_len):
            ch = strs[0][j]

            common  = True
            for i in range(1, n):
                if ch != strs[i][j]:
                    common = False
                    break
            
            if common:
                ans += ch
            else:
                break
            
        return ans
        