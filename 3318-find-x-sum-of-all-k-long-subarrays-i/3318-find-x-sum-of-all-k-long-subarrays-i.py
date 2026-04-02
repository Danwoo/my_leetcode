class Solution:
    def findXSum(self, nums: list[int], k: int, x: int) -> list[int]:
        n = len(nums)
        answer = []
        
        for i in range(n - k + 1):
            # 1. 고정 길이 배열을 이용한 해시 테이블 구현 (nums[i] <= 50 제약조건 활용)
            freq = [0] * 51
            for j in range(i, i + k):
                freq[nums[j]] += 1
                
            current_sum = 0
            
            # 2. 내장 sort() 대신 직접 X번 순회하며 최댓값 탐색 (Selection Sort 방식)
            for _ in range(x):
                max_freq = 0
                max_val = 0
                
                # 배열 전체를 순회하며 조건(빈도수, 값)에 맞는 최댓값 찾기
                for v in range(1, 51):
                    if freq[v] > max_freq or (freq[v] == max_freq and v > max_val):
                        max_freq = freq[v]
                        max_val = v
                
                # 더 이상 뽑을 값이 없으면 조기 종료
                if max_freq == 0:
                    break
                    
                # 3. 합계 누적 및 선택된 값의 빈도수 초기화 (중복 선택 방지)
                current_sum += max_val * max_freq
                freq[max_val] = 0
                
            answer.append(current_sum)
            
        return answer