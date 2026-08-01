class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        max_diagonal = -1
        max_area = 0

        for a, b in dimensions:
            diagonal = a * a + b * b
            area = a * b

            if diagonal > max_diagonal:
                max_diagonal = diagonal
                max_area = area
            elif diagonal == max_diagonal:
                max_area = max(max_area, area)

        return max_area