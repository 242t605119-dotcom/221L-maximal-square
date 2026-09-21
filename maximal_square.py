class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])

        dp = [0] * (cols + 1)
        max_side = 0
        prev = 0

        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                temp = dp[j]

                if matrix[i - 1][j - 1] == "1":
                    dp[j] = min(dp[j], dp[j - 1], prev) + 1
                    max_side = max(max_side, dp[j])
                else:
                    dp[j] = 0

                prev = temp

        return max_side * max_side
