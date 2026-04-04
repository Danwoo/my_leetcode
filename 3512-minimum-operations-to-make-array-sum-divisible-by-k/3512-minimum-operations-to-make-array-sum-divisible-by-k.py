class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        # 총합을 k로 나눈 나머지가 곧 최소 조작 횟수
        return sum(nums) % k