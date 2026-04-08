class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        MOD = 10**9 + 7
        
        # 1. Process each query
        for l, r, k, v in queries:
            # Update elements from 'l' to 'r' with step 'k'
            for i in range(l, r + 1, k):
                # Apply modulo (10^9 + 7) immediately after multiplication to prevent integer overflow and keep numbers within limits
                nums[i] = (nums[i] * v) % MOD
                
        # 2. Calculate the final XOR sum
        result = 0
        for num in nums:
            result ^= num
            
        return result