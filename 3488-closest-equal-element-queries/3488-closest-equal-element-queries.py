class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        # Group indices by their corresponding values in the array
        positions = defaultdict(list)
        for i, num in enumerate(nums):
            positions[num].append(i)
            
        # Initialize the minimum distance array with -1
        min_dist = [-1] * n
        
        for val, idxs in positions.items():
            k = len(idxs)
            # Skip if there is no identical element
            if k == 1:
                continue
                
            # Calculate the shortest distance to adjacent nodes in the group
            for i in range(k):
                curr = idxs[i]
                
                # Identify the previous and next adjacent nodes (Circular logic)
                prev_idx = idxs[(i - 1) % k]
                next_idx = idxs[(i + 1) % k]
                
                # Calculate circular distance to the previous node
                d1 = abs(curr - prev_idx)
                d1 = min(d1, n - d1)
                
                # Calculate circular distance to the next node
                d2 = abs(curr - next_idx)
                d2 = min(d2, n - d2)
                
                # Store the minimum of the two distances
                min_dist[curr] = min(d1, d2)
                
        # Retrieve and return the precomputed results for each query
        return [min_dist[q] for q in queries]