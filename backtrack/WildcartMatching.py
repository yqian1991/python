class Solution:
    # @param s, an input string
    # @param p, a pattern string
    # @return a boolean
    def isMatch(self, s, p):
        sindex = 0
        pindex = 0
        star = -1
        mark = 0
        while sindex < len(s):
            print sindex, pindex, star, mark
            if pindex < len(p) and (s[sindex] == p[pindex] or p[pindex] == "?"):
                sindex += 1
                pindex += 1
            elif pindex < len(p) and p[pindex] == "*":
                star = pindex
                mark = sindex
                pindex += 1
            elif star != -1:
                pindex = star + 1
                mark += 1
                sindex = mark
            else:
                return False

        while pindex < len(p) and p[pindex] == "*":
            pindex += 1

        return pindex == len(p)

if __name__ == "__main__":
    sol = Solution()
    print sol.isMatch("acedbabd", "a*bd")

