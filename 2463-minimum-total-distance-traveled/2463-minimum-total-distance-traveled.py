class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        # 1. 경로 꼬임 방지를 위해 위치 기준 오름차순 정렬
        robot.sort()
        factory.sort()
        
        # 2. 공장 평탄화 (각 공장의 limit만큼 위치를 복사해서 슬롯으로 만듦)
        # 로봇 수보다 많은 limit은 의미 없으므로 min으로 잘라냄
        slots = []
        for pos, limit in factory:
            slots.extend([pos] * min(limit, len(robot)))
            
        n = len(robot)
        m = len(slots)
        
        # 3. DP 배열 세팅 (메모리 최적화를 위해 1차원 배열 사용)
        # 이전 로봇까지의 최소 거리 상태를 저장
        dp = [0] * (m + 1)
        
        for i in range(1, n + 1):
            # 현재 로봇에 대한 새로운 DP 배열 (초기값은 무한대)
            next_dp = [float('inf')] * (m + 1)
            
            for j in range(1, m + 1):
                # skip: 현재 슬롯을 안 쓰고 넘어감
                # assign: 현재 슬롯에 지금 로봇을 배정함
                skip = next_dp[j - 1]
                assign = dp[j - 1] + abs(robot[i - 1] - slots[j - 1])
                
                next_dp[j] = min(skip, assign)
            
            # 다음 로봇을 위해 상태 업데이트
            dp = next_dp
            
        return dp[m]