# 연결 리스트(Linked List)

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def init_list():
    global node_A
    node_A = Node("A")
    node_B = Node("B")
    node_C = Node("C")
    node_D = Node("D")
    node_A.next = node_B
    node_B.next = node_C
    node_C.next = node_D


def print_list():
    global node_A
    node = node_A
    while node:
        print(node.data)
        node = node.next
    print()


if __name__ == '__main__':
    init_list()
    print_list()
