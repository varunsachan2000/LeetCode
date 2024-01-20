class Solution:
    def myAtoi(self, s: str) -> int:
        if not s:
            return 0

        # remove leading and trailing whitespace
        s = s.strip()

        # save sign if one exists
        pos = True
        if s and s[0] == '-':
            pos = False
            s = s[1:]
        elif s and s[0] == '+':
            s = s[1:]
        
        # ignore leading zeros
        i = 0
        while i < len(s) and s[i] == '0':
            i += 1

        # apply relevant digits
        res = None
        while i < len(s) and s[i] in '0123456789':
            if res is None:
                res = int(s[i])
            else:
                res = (res * 10) + int(s[i])
            i += 1
        res = 0 if res is None else res

        # apply sign
        res = res if pos else -res

        # clip result
        res = max(res, -2**31)
        res = min(res, (2**31)-1)

        return res
        