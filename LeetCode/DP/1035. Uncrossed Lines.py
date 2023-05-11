class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        # Get the lengths of both input lists
        rows = len(nums1)
        columns = len(nums2)

        # Initialize a 2D array of size (rows+1)x(columns+1) with all elements set to 0
        # +1 because we will use the first row/column for empty values
        dp = [[0] * (columns+1) for _ in range(rows + 1)]

        # Iterate through each element in nums1 and nums2
        for i, val1 in enumerate(nums1, start=1):
            for j, val2 in enumerate(nums2, start=1):
                # If the values are the same,
                if val1 == val2:
                    # increment the value of the corresponding element in dp by
                    # 1 + the value of the element in the diagonal position
                    # (Previous Best Solution)
                    dp[i][j] = 1 + dp[i-1][j-1]
                # If the values are different
                else:
                    # take the maximum value of the element in the row above
                    # and the element in the column to the left
                    # ()
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])

        # Return the value in the bottom-right corner of the dp array
        return dp[rows][columns]
