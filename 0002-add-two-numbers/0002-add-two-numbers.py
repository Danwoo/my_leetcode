# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy
        carry = 0
        
        # l1, l2 중 하나라도 노드가 남아있거나, 넘겨줄 올림수가 남아있다면 반복
        while l1 or l2 or carry:
            # 노드가 끝났다면 0으로 계산
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # 현재 자리의 합 및 새로운 올림수 계산
            total = val1 + val2 + carry
            carry = total // 10
            
            # 새로운 노드를 만들어 결과 리스트에 연결
            curr.next = ListNode(total % 10)
            curr = curr.next
            
            # 다음 노드로 이동
            if l1: l1 = l1.next
            if l2: l2 = l2.next
            
        # dummy 노드의 다음 노드가 실제 결과 리스트의 시작점
        return dummy.next