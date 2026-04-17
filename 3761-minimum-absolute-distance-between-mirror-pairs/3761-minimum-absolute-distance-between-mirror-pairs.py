class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        # Helper function to reverse the digits of an integer
        def reverse_num(x: int) -> int:
            res = 0
            while x > 0:
                res = res * 10 + x % 10
                x //= 10
            return res
            
        # Dictionary to store the latest index of a reversed number
        recent_idx = {}
        min_dist = float('inf')
        
        for i, num in enumerate(nums):
            # If the current number matches a previously stored reversed number
            if num in recent_idx:
                dist = i - recent_idx[num]
                min_dist = min(min_dist, dist)
                
            # Reverse the current number and store its index for future lookups
            # Overwriting naturally keeps the latest index (minimizing the distance)
            rev = reverse_num(num)
            recent_idx[rev] = i
            
        return min_dist if min_dist != float('inf') else -1