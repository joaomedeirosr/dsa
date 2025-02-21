class Node:
    def __init__(self, valor):
        self.valor = valor
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
    
    def add_to_start(self, valor):    
        new_node = Node(valor)
        new_node.next = self.head
        self.head = new_node

    def print_linked_list(self):
        current = self.head
        while current:
            print(f"{current.valor},", end="")
            current = current.next


    def remove_from_start(self):
        pass

    def remove_from_end(self):
        pass


ll = LinkedList()
ll.add_to_start(1)
ll.add_to_start(2)
ll.add_to_start(3)

print(ll.print_linked_list())