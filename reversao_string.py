
from pilha import Pilha  


def reverter_string(s):
    pilha = Pilha()
    
    
    for char in s:
        pilha.push(char)
    
    
    string_revertida = ""
    while not pilha.is_empty():
        string_revertida += pilha.pop()
    
    return string_revertida


entrada = input("Digite a string para reverter: ")


resultado = reverter_string(entrada)
print("String revertida:", resultado)
