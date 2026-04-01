class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
    
        # 첫 번째 문자열의 한 글자씩 확인
        for i in range(len(strs[0])):
            char = strs[0][i]
            
            # 나머지 문자열들과 비교
            for j in range(1, len(strs)):
                # 현재 인덱스 i가 다른 문자열의 길이를 넘어서거나 문자가 다르면 종료
                if i == len(strs[j]) or strs[j][i] != char:
                    return strs[0][:i]
                    
        return strs[0]