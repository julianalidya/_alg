def min_edit_distance(s1, s2):
    m, n = len(s1), len(s2)
    
    # 建立 DP 矩陣
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # 初始化第一行與第一列
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    # 填充矩陣
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(
                    dp[i-1][j],    # Deletion
                    dp[i][j-1],    # Insertion
                    dp[i-1][j-1]   # Substitution
                )
    
    return dp[m][n]

# 測試案例
test_cases = [
    ("kitten", "sitting"),
    ("flaw", "lawn"),
    ("intention", "execution"),
    ("hello", "hello")
]

print("| String 1 | String 2 | Min Edit Distance |")
print("|----------|----------|-------------------|")
for s1, s2 in test_cases:
    dist = min_edit_distance(s1, s2)
    print(f"| {s1:<8} | {s2:<8} | {dist:<17} |")
