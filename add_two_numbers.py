from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __int__(self):
        return sum(digit * (10 ** n) for n, digit in enumerate(self))

    def __add__(self, other) -> 'ListNode':
        value = int(self) + int(other)
        return create_node_from_number(value)

    def __iter__(self):
        node = self
        while node:
            yield node.val
            node = node.next

    def __eq__(self, other):
        return list(self) == list(other)

    def __repr__(self):
        return str(int(self))


def create_node_from_number(num: int) -> ListNode:
    if num == 0:
        return ListNode(0)

    head_node = None
    previous_node = None
    value = num
    while value:
        num_mod = value % 10
        value //= 10
        new_node = ListNode(val=num_mod)
        if previous_node:
            previous_node.next = new_node
        if head_node is None:
            head_node = new_node
        previous_node = new_node

    return head_node


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        return l1 + l2


class AlternativeSolution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        value = self.node_to_int(l1) + self.node_to_int(l2)
        return create_node_from_number(value)

    def get_node_values(self, node: ListNode):
        while node:
            yield node.val
            node = node.next

    def node_to_int(self, node: ListNode) -> int:
        digits = self.get_node_values(node)
        return sum(digit * (10 ** n) for n, digit in enumerate(digits))


if __name__ == '__main__':
    solution = AlternativeSolution()
    expected_node = create_node_from_number(807)
    for l1, l2, expectation in (
        (342, 465, 807),
        (0, 0, 0),
        (9999999, 9999, 10009998),
    ):
        ex = create_node_from_number(expectation)
        assert solution.addTwoNumbers(
            create_node_from_number(l1),
            create_node_from_number(l2)
        ) == ex

    print('All good!')
