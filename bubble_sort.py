
class bubbleSort:
    def __init__(self) -> None:
        pass
    def bubble_sort(self, lista: list) -> list:
        list_length = len(lista) - 1
        for _ in range(list_length):
            no_swaps = True
            for i in range(list_length):
                if lista[i] > lista[i+1]:
                    lista[i] , lista[i+1] = lista[i+1], lista[i]
                    no_swaps = False

            if no_swaps:
                return lista
       
        return lista
    def reverse_sort(self, lista: list) -> list:
        list_length = len(lista) - 1

        for _ in range(list_length):
            for i in range(list_length):
                if lista[i] < lista[i+1]:
                    lista[i] , lista[i+1] = lista[i], lista[i+1]
        
        return lista

ordernando = bubbleSort()

print(ordernando.bubble_sort([5,4,3,2,1]))
print(ordernando.reverse_sort([5,4,3,2,1]))
