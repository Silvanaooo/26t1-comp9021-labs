# ================= Explanation ================= #
"""
We use DP to solve the problem.

1. DP definition:
dp[i][j] = the length of the longest common subsequence between text1[:i] and text2[:j].

Here, i and j mean the first i characters of text1
and the first j characters of text2.

2. Transition:
We compare the current characters:

text1[i - 1] and text2[j - 1]

Case 1: They are the same
dp[i][j] = dp[i - 1][j - 1] + 1

This means the current matching character can extend
the previous best subsequence.

Case 2: They are different
dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

This means the current characters cannot be matched together,
so we keep the best previous result:
- dp[i - 1][j]: skip the current character in text1
- dp[i][j - 1]: skip the current character in text2

3. Initialization:
dp is created with one extra row and one extra column filled with 0.
If one string is empty, the longest common subsequence length is 0.

So:
dp[0][j] = 0
dp[i][0] = 0

4. Traversal order:
We fill the table from top-left to bottom-right.

For each dp[i][j], we need values from:
- dp[i - 1][j - 1]
- dp[i - 1][j]
- dp[i][j - 1]

These values have already been computed.

5. Result:
The final answer is dp[len(text1)][len(text2)],
because it represents the LCS length between the whole text1
and the whole text2.
"""

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Create a DP table.
        # dp[i][j] means:
        # the LCS length between text1[:i] and text2[:j].
        # We add 1 extra row and column to represent the empty string.
        dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]

        # i starts from 1 because row 0 means empty text1.
        for i in range(1, len(text1) + 1):

            # j starts from 1 because column 0 means empty text2.
            for j in range(1, len(text2) + 1):

                # Compare the current characters.
                # Since dp uses 1-based length,
                # the actual string index is i - 1 and j - 1.
                if text1[i - 1] == text2[j - 1]:

                    # If the two characters match,
                    # we can extend the previous LCS by 1.
                    dp[i][j] = dp[i - 1][j - 1] + 1

                else:
                    # If they do not match,
                    # we cannot use both current characters together.
                    # So we keep the best previous result:
                    # 1. skip current char in text1 -> dp[i - 1][j]
                    # 2. skip current char in text2 -> dp[i][j - 1]
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        # This cell represents the LCS length
        # between the whole text1 and the whole text2.
        return dp[len(text1)][len(text2)]