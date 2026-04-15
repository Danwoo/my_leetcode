class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n = len(words)
        min_dist = float('inf')
        
        for i, word in enumerate(words):
            # 타겟을 발견할 때마다 양방향 거리 중 짧은 것을 계산
            if word == target:
                dist = abs(i - startIndex)
                shortest = min(dist, n - dist)
                min_dist = min(min_dist, shortest)
                
        # 한 번도 갱신되지 않았다면 타겟이 없는 것이므로 -1 리턴
        return min_dist if min_dist != float('inf') else -1