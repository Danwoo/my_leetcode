class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        count = 0
        while num1 > 0 and num2 > 0:
            if num1 >= num2:
                # 뺄셈을 여러 번 하는 대신 몫을 더함
                count += num1 // num2  
                # 뺀 후의 결과는 나머지
                num1 %= num2           
            else:
                count += num2 // num1
                num2 %= num1
                
        return count