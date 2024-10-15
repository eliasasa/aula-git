#2 - Desenvolva um programa que mostre a tabuada de um número informado pelo usuário.

while True:
    try:
        num = int(input("Escreva um número:\n"))
        tab = 1
        for i in range(10):
            print(f'{num} X {tab} = {num*tab}')
            if tab >= 10:
                break
            else: tab+=1
            
    except ValueError:
        print("Não é um valor inteiro.")