class TwoPointers:
    def reverseWord(self, array_input):
        reverse_word = " " 
        pointer_init, pointer_end = 0 , 0

        while pointer_end < len(array_input): # Vai comparar 2 números
            if pointer_end != " ": # Equanto tiver palavra ele vai incrementar 1 para ir na proxima posicao
                pointer_end +=1
                # Até aqui pointer_end está em um espaco em branco != 0 e pointer_init = 0 (ínicio) 
            
            else:
                reverse_word += array_input[pointer_init : pointer_end + 1][::-1]
                pointer_end +=1 # Sai do espaco em branco, acha nova sub-string
                pointer_init = pointer_end
            
            reverse_word += " "
            reverse_word += array_input[pointer_init : pointer_end + 2][::-1]

        return reverse_word

reversed_string = TwoPointers()

# Case - Test
print(reversed_string.reverseWord("Car"))
print(reversed_string.reverseWord("Duck"))




