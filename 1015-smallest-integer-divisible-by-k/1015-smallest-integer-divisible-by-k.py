class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        # 2, 5의 배수는 안됨
        if k % 2 == 0 or k % 5 == 0:
            return -1
        
        remainder = 0
        
        # 최대 K번 안에는 무조건 사이클이 돌거나 0이 나옴
        for length in range(1, k + 1):
            # 나미지로 계산
            remainder = (remainder * 10 + 1) % k
            
            # 나누어 떨어지면 현재 자릿수(길이) 리턴
            if remainder == 0:
                return length
                
        return -1