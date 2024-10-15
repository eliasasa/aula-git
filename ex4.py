# 4 - Faça um programa que verifique se um número fornecido é primo.

while True:
    try:
        num = int(input("Escreva um número:\n"))
        cont=1
        primo=0
        while cont <= num:
            if num % cont == 0:
                primo+=1
            cont+=1
        if primo == 2:
            print("É primo")
            break
        else:
            print("Não é primo")
            break
    except ValueError:
        print("Não é um valor inteiro.")