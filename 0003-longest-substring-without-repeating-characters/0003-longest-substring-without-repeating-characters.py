class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}  # 문자의 최근 위치를 저장할 해시맵
        max_len = 0
        left = 0
        
        for right, char in enumerate(s):
            # 문자가 이미 Window 내부에 존재한다면 left 포인터 이동
            if char in char_index and char_index[char] >= left:
                left = char_index[char] + 1
            
            # 현재 문자의 위치 갱신
            char_index[char] = right
            
            # 최대 길이 갱신
            max_len = max(max_len, right - left + 1)
            
        return max_len