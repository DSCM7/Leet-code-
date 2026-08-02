from typing import List
class Solution:
    def reverseString(self, s: List[str]):
        s[:] = s[::-1]