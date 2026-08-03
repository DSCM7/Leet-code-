class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        c = 0
        for fruit in fruits:
            for i in range(len(baskets)):
                if baskets[i] >= fruit:
                    baskets[i] = -1      
                    c += 1
                    break

        return len(fruits) - c