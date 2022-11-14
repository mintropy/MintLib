"""Linked List
추상적 자료형 리스트 구현
"""

from typing import Optional, Union, List, Tuple

Seq = Union[None, int, List[int], Tuple[int]] 


class Node:
    def __init__(self, value: int) -> None:
        self.value = value
        self.next_node = None


class LinkedList:
    def __init__(self, seq: Union[None, List[int], Tuple[int]]) -> None:
        self.head: Optional[Node] = None
        self.length: int = 0
        if seq is not None:
            self.append(seq)

    def get_list(self) -> list[int]:
        linked_list: list[int] = []
        node: Optional[Node] = self.head
        while node is not None:
            linked_list.append(node.value)
            node= node.next_node
        return linked_list

    def append(self, seq: Union[int, List[int], Tuple[int]]) -> None:
        if self.head is None:
            self.head = Node(seq[0])
        node = self.head
        while node.next_node is not None:
            node = node.next_node
        for x in seq[1:]:
            node.next_node = Node(x)
            node = node.next_node
        self.length += len(seq)

    def add(self, before_node_value: int, new_value: int) -> None:
        node: Optional[Node] = self.head
        while node is None:
            if node.value == before_node_value:
                next_node = node.next_node
                node.next_node = Node(new_value)
                node.next_node.next_node= next_node
                return
            node = node.next_node
        raise Exception(f"before node value : {before_node_value} does not exist")


if __name__ == "__main__":
    linked_list = LinkedList()
