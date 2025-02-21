   # Dada uma lista de palavras em ordem alfabética, escreva uma funcao que execute
   # uma busca binária de uma palavra e retorne se ela está na lista.

def find_word(word_array: list[str], word: str) -> bool:
    start_pointer = 0
    end_pointer = len(word_array) - 1

    while start_pointer < end_pointer:
        mid = (start_pointer + end_pointer) // 2

        if word_array[mid] == word:
            return True
        
        elif word_array[mid] < word:
            start_pointer = mid + 1
        
        else:
            end_pointer = mid - 1
    
    return False



print(find_word(['abacaxi','banana','caju','damasco'], 'melancia'))