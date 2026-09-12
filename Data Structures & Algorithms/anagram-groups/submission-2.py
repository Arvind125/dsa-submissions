class Solution:
    def get_freq(self, s: str) -> str:
        f = [0] * 26
        for ch in s:
            f[ord(ch) - 97] += 1
        return str(f)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        fs = {}
        for s in strs:
            cur_f = self.get_freq(s)
            if cur_f not in fs:
                fs[cur_f] = [s]
            else:
                fs[cur_f].append(s)

        ans = []

        for _, val in fs.items():
            ans.append(val)
            
        return ans

        