class Node:
    def __init__(self, valor):
        self.valor = valor
        self.next = None # Ponteiro apontando para proximo elemento
        self.prev = None # Ponteiro apontando para elemento anterior

class DoubleLinkedList:
    def __init__(self):
        self.head = None # Ponteiro apontando para head
        self.tail = None # Ponteiro apontando para tail
    
    def add_to_start(self, valor):
        new_node = Node(valor)

        if not self.head:
            self.head = self.tail = new_node # New_node quando add vai ser tanto head quanto tail.
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def add_to_end(self, valor):
        new_node = Node(valor)
        
        if not self.tail:
            self.head = self.tail = new_node
        
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node


    def remove_from_start(self):
        if not self.head:  # Se nao exitir Head, isso é uma LinkedList vazia entao return None
            return None
        removed_value = self.head.valor # Quem vai ser removido é quem é o valor do atual head
        
        if self.head == self.tail: # É porque existe apenas 1 elemento entao ao ser removido head e tail vai apontar pra None.
            self.head = self.tail = None
        
        else:
            self.head = self.head.next # Quem vai ser o novo head é elemento que estiver na frente do antigo head
            self.head.prev = None # Como será removido irá apontar para o vazio
        
        return removed_value
    
    def remove_from_end(self):
        if not self.tail:
            return None
        
        removed_value = self.tail.valor # Quem vai ser removide é o valor do atual tail

        if self.head == self.tail: # Quanto tenho apenas 1 elemento
            self.head = self.tail = None
        
        else:
            self.tail = self.tail.prev # Quem vai ser o novo Tail é o valor anterior ao atual tail
            self.prev = None # Vai apontar para o vazio.
        
        return removed_value


dll = DoubleLinkedList()

print(dll.add_to_start(3))
print(dll.add_to_start(2))
print(dll.add_to_start(1))
dll.add_to_end(4)
dll.add_to_end(5)

print(dll.remove_from_start())
print(dll.remove_from_end())