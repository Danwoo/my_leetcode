class Solution:
    def minimumDistance(self, word: str) -> int:
        # 키보드 상 두 알파벳 간의 맨해튼 거리 계산
        def dist(a, b):
            return abs(a // 6 - b // 6) + abs(a % 6 - b % 6)
            
        # dp[c]: 다른 손가락 하나가 알파벳 'c'에 있을 때 아낀 최대 거리
        dp = [0] * 26
        max_save = 0
        res = 0  # 1손가락으로 다 쳤을 때의 총 거리
        
        # 문자를 0~25 숫자로 매핑해서 시작
        prev = ord(word[0]) - 65
        
        for i in range(1, len(word)):
            curr = ord(word[i]) - 65
            d = dist(prev, curr)
            res += d  # 일단 원핑거 거리 누적
            
            # prev 자리에 메인 손가락을 두고, c에 놀고 있던 서브 손가락을 curr로 쏠 때의 절약분 계산
            save_if_c_moves = max(dp[c] + d - dist(c, curr) for c in range(26))
            
            # 서브 손가락이 prev에 남게 되는 상황 갱신
            dp[prev] = max(dp[prev], save_if_c_moves)
            max_save = max(max_save, dp[prev])
            
            # 메인 손가락 위치 업데이트
            prev = curr
            
        # (전체 거리) - (최대한으로 아낀 거리) = (최소 2핑거 거리)
        return res - max_save