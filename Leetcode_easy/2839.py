class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        c = 0

        if s1 == s2:
            c += 1

        t = list(s1)
        t[0], t[2] = t[2], t[0]
        if "".join(t) == s2:
            c += 1

        t = list(s1)
        t[1], t[3] = t[3], t[1]
        if "".join(t) == s2:
            c += 1

  
        t = list(s1)
        t[0], t[2] = t[2], t[0]
        t[1], t[3] = t[3], t[1]
        if "".join(t) == s2:
            c += 1

        if c > 0:
            return True
        else:
            return False