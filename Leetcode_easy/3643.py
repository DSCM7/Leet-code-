class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        l = []

        
        for i in range(k):
            l.append(grid[x + i][y:y + k])

       
        l = l[::-1]

       
        for i in range(k):
            grid[x + i][y:y + k] = l[i]

        return grid