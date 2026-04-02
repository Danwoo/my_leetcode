class Solution:
    def kLengthApart(self, nums: list[int], k: int) -> bool:
        last_idx = -1
        
        for i, num in enumerate(nums):
            if num == 1:
                # 이전 1과의 거리가 k보다 작으면 False
                if last_idx != -1 and i - last_idx - 1 < k:
                    return False
                # 현재 1의 인덱스 갱신
                last_idx = i
                
        return True