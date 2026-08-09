class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        t = sorted(arr)

        rank = {}
        r = 1

        for x in t:
            if x not in rank:
                rank[x] = r
                r += 1

        ans = []

        for x in arr:
            ans.append(rank[x])

        return ans