class Solution:
    def encode(self, strs: List[str]) -> str:
        ss = ""
        for s in strs:
            l = len(s)
            curr = str(l) + "#" + s
            ss += curr
        return ss


    def decode(self, s: str) -> List[str]:
        print(s)
        num = ""
        pfx = True
        curr_str = ""
        l = 0
        ans = []
        for ch in s:
            if pfx:
                if ch != "#":
                    num += ch
                else:
                    print(num)
                    l = int(num)
                    pfx = False

                    if l==0:
                        ans.append("")
                        pfx = True
                        curr_str = ""
                        num = ""
                        l = 0
            else:
                if l > 0:
                    curr_str += ch
                    l -= 1
                if l == 0:
                    ans.append(curr_str)
                    pfx = True
                    curr_str = ""
                    num = ""
                    l = 0

        return ans
