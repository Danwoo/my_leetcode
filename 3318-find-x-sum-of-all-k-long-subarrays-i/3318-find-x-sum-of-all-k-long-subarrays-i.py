class Solution:
    def findXSum(self, nums: list[int], k: int, x: int) -> list[int]:
        n = len(nums)
        answer = []
        
        for i in range(n - k + 1):
            # 1. 윈도우 내 요소 빈도수 계산
            counts = Counter(nums[i : i + k])
            
            # 2. 빈도수 내림차순, 값 내림차순 다중 조건 정렬
            items = sorted(counts.items(), key=lambda item: (item[1], item[0]), reverse=True)
            
            # 3. 상위 x개 요소의 (값 * 빈도) 합계를 누적하여 추가
            current_sum = sum(val * freq for val, freq in items[:x])
            answer.append(current_sum)
            
        return answer