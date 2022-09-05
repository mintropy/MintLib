"""Linked List
Double Linked List
- 데이터의 주소와 노드가 한 줄로 연결된 구조
- 연결 구조에 따라 singly linked list, doubly linked list, circular linked list 등으로 구분

attributes
head, tail : 가장 앞, 뒤의 노드
node_count : 노드의 갯수

methods (python list method 참조)
append : 삽입
pop : tkrwp
"""

from typing import Union


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.before_node = None
        self.next_node = None


class DoublyLinkedList:
    def __init__(self) -> None:
        self.head: Union[None, Node] = None
        self.tail = None
        self.node_count: int = 0

    def append(self, node: Node) -> None:
        if self.head is None:
            self.head = node
            self.tail = node
            return
        node.before_node = self.tail
        self.tail.next_node = node
        self.tail = node
        self.node_count += 1

    def add(self, node: Node, before_node: Node):
        pass


if __name__ == "__main__":
    linked_list = DoublyLinkedList()
