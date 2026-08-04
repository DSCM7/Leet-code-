class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        count = Counter(digits)
        ans = []

        for num in range(100, 1000, 2):   # only even 3-digit numbers
            need = Counter(map(int, str(num)))

            valid = True
            for d in need:
                if need[d] > count[d]:
                    valid = False
                    break

            if valid:
                ans.append(num)

        return ans