# 3 - Escreva uma função que verifique se uma palavra ou frase é um palíndromo (pode ser lida da mesma maneira de trás para frente).


while True:
    try:
        entrada = input("Escreva uma palavra:\n")
        if entrada.isalpha():
            if entrada == entrada[::-1]:
                print(f"A palavra '{entrada}' é um palíndromo.")
            else:
                print(f"A palavra '{entrada}' não é um palíndromo.")
            break 
        else:
            raise ValueError("A entrada deve conter apenas letras.")
    except ValueError as e:
        print(e)

