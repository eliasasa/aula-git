#1 - Crie uma função que calcule o fatorial de um número dado pelo usuário.

# 4 > 3 > 2 

while True:
    try: 
        num = int(input("Escreva um número:\n"))
        total = num
        for i in range(num):
            total *= (num - 1)
            num-=1
            if num <= 2:
                break
        print(total)
        break
    except ValueError:
        print("Não é um valor inteiro.")
