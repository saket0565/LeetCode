'''
    Time: O(m*n)
    Space: O(m*n)
'''
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = [[False] * n] * m

        dp[0][0] = True
        for j in range(1,n + 1):
            if p[j-1] == '*' or (j < n and p[j] == '*'):
                dp[0][j] = True
            else:
                break
        for i in range(1,m + 1):
            for j in range(1,n + 1):
                if p[ j - 1] == '*':
                    dp[i][j] = (dp[i - 1][j] or dp[i][j - 2]) if (s[i - 1] == p[j - 2] or p[j - 2] == '.') else dp[i][j - 2]
                else
                    dp[i][j] = dp[i - 1][j - 1] if (s[i - 1] == p[j - 1] or p[j - 1] == '.') else False

        return dp[m][n]
