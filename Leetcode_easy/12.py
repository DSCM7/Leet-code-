class Solution:
    def intToRoman(self, num: int) -> str:
        
        L = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
        st = ""
        for v, s in L: 
            while num >= v: 
                st += s
                num -= v
        return st