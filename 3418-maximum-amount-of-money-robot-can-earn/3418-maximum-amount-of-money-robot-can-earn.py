class Solution:
    def maximumAmount(self, coins: list[list[int]]) -> int:
        m, n = len(coins), len(coins[0])
        INF = float('-inf')
        
        # dp[i][j][k]: (i, j) 칸에 도달하며 능력을 k번 사용했을 때의 최대 이익
        dp = [[[INF] * 3 for _ in range(n)] for _ in range(m)]
        
        # 1. 시작점(0, 0) 초기화
        dp[0][0][0] = coins[0][0]
        if coins[0][0] < 0:
            dp[0][0][1] = 0  # 첫 칸부터 도둑이 있으면 능력 1회 사용 가능
            
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                    
                val = coins[i][j]
                
                for k in range(3):
                    # 2. 이전 위치(위쪽, 왼쪽)에서 k번 능력을 쓰고 온 경우의 최댓값 탐색
                    prev_val = INF
                    if i > 0: prev_val = max(prev_val, dp[i-1][j][k])
                    if j > 0: prev_val = max(prev_val, dp[i][j-1][k])
                    
                    if prev_val != INF:
                        # 선택 1: 현재 칸에서 능력을 사용하지 않음 (값 그대로 획득/상실)
                        dp[i][j][k] = max(dp[i][j][k], prev_val + val)
                        
                    # 선택 2: 현재 칸에서 능력을 새로 사용함 (음수일 때만 가능, k > 0)
                    if val < 0 and k > 0:
                        prev_val_k_minus_1 = INF
                        if i > 0: prev_val_k_minus_1 = max(prev_val_k_minus_1, dp[i-1][j][k-1])
                        if j > 0: prev_val_k_minus_1 = max(prev_val_k_minus_1, dp[i][j-1][k-1])
                        
                        if prev_val_k_minus_1 != INF:
                            dp[i][j][k] = max(dp[i][j][k], prev_val_k_minus_1)
                            
        # 목적지에서 능력을 0번, 1번, 2번 쓴 경우 중 가장 큰 값 반환
        return max(dp[m-1][n-1])