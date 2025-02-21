# Pilha - Utilizando array dinamico (Python List)
"""
 O que eu quero em filas:
    1 - Adicionar Elemento
    2 - Remover Elemento
    3 - Verificar quem está no topo da pilha
    4 - Verificar se a pilha está vazia
"""
class Stack:
    def __init__(self, array):
        self.array = array

    # Append to top of stack - O(1)
    def append_element(self,n):
        self.array.append(n)
        print(self.array)

    # Pop from stack - O(1)
    def pop_element(self):
        if self.array:
            removed_element = self.array.pop()
            print(f"Elemento removido: {removed_element}")
            print(f"Novo array após remocao do elemento: {self.array} \n")

        else:
            print("Array já está vazio nao é possível remover mais nenhum elemento")

    # Peek Top of stack - O(1)        
    def check_top_stack(self):
        print(f"O elemento no topo da pilha é: {self.array[-1]}\n")
    
    # Check is stack is empty - O(1)
    def stack_is_empty(self):
        if self.array:
            return "Array have elements: " + f"{self.array}"
        
        else:
            return "Array is empty"


element = Stack([])
print(element.stack_is_empty())
element.append_element(5)
element.append_element(6)
element.check_top_stack()
element.pop_element()
element.pop_element()
element.pop_element()