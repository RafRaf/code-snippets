# For python >= 3.11
# from typing import Self
# or
from typing import TypeVar

Self = TypeVar("Self", bound="LinkedListItem")


class LinkedListItem:
    value: int
    next: Self | None

    def __init__(self, value: int, *, next: Self | None = None):
        self.value = value
        self.next = next


class LinkedList:
    @staticmethod
    def from_list(numbers: list[int]) -> LinkedListItem:
        length = len(numbers)
        index = length - 1
        head = None

        for index in range(length - 1, -1, -1):
            head = LinkedListItem(numbers[index], next=head)

        return head

    @staticmethod
    def print(head: LinkedListItem):
        current = head

        while current:
            print(current.value)
            current = current.next

    @staticmethod
    def invert(head: LinkedListItem) -> LinkedListItem:
        current = head
        prev_head = None

        while current:
            next = current.next
            current.next = prev_head
            prev_head = current
            current = next

        return prev_head


if __name__ == '__main__':
    linked_list = LinkedList.from_list([1, 7, 9, 4, 100])
    LinkedList.print(linked_list)

    inverted_linked_list = LinkedList.invert(linked_list)
    LinkedList.print(inverted_linked_list)
