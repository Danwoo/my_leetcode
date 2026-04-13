class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        n = len(nums)

        # start를 기준으로 거리(d)를 0부터 하나씩 늘려감
        for d in range(n):
            # 오른쪽 방향 체크 (인덱스 초과 방어)
            if start + d < n and nums[start + d] == target:
                return d

            # 왼쪽 방향 체크 (인덱스 음수 방어)
            if start - d >= 0 and nums[start - d] == target:
                return d

        return 0