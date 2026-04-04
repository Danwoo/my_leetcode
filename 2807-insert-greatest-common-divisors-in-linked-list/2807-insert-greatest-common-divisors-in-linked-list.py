# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional['ListNode']) -> Optional['ListNode']:
        # 유클리드 호제법을 이용한 최대공약수(GCD) 계산 헬퍼 함수
        def get_gcd(a: int, b: int) -> int:
            while b > 0:
                a, b = b, a % b
            return a
            
        curr = head
        
        # 현재 노드와 다음 노드가 모두 존재하는 동안 연결 리스트 순회
        while curr and curr.next:
            # 1. 인접한 두 노드의 값(val)을 바탕으로 최대공약수 도출
            gcd_val = get_gcd(curr.val, curr.next.val)
            
            # 2. 도출된 최대공약수를 값으로 갖는 새로운 노드 생성
            # 새 노드의 next 포인터를 기존의 다음 노드(curr.next)로 바로 연결
            new_node = ListNode(gcd_val, curr.next)
            
            # 3. 현재 노드의 next 포인터를 방금 생성한 새 노드로 변경하여 리스트 중간에 삽입
            curr.next = new_node
            
            # 4. 다음 위치 탐색을 위해 포인터를 삽입된 노드의 다음(원래 순서의 다음 노드)으로 이동
            curr = new_node.next
            
        return head