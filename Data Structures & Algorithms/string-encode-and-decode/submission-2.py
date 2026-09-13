class Solution:
    def encode(self, strs: List[str]) -> str:
        ss = ""
        for s in strs:
            l = len(s)
            curr = str(l) + "#" + s
            ss += curr
        return ss


    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1

            l = int(s[i:j])

            start = j + 1   # j is pointing to #
            ans.append(s[start:start + l])

            i = start + l

        return ans
