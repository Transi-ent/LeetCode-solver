"""
Reverse the linkedList
"""

class ListNode:

    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def reverseList(head: ListNode):

    prev = None


    while head:

        next = head.next # if head!=null, thus head.next exists

        # 三个指针的位置都已经就绪，可以翻转了
        head.next = prev

        prev = head

        head = next

    return prev


def createLinkedList(arr: list, n):

    if not n:
        return None

    cur = ListNode(arr[0])

    for i in range(1, n):

        cur.next = ListNode(arr[i])

        cur = cur.next


if __name__=="__main__":
    main()
