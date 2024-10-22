# 6 - Escreva um algoritmo que receba uma lista de números e retorne a lista ordenada de forma crescente (Bubble sort).

while True:
    num = []
    try:
        quant = int(input("Escreva a quantidade de termos que deseja ordenar:\n"))
        if quant <= 1:
            print('Valor menor que 1!')
        else:
            for i in range(quant):
                x = input(f'Número {i+1}:\n')
                num.append(x)
            for i in len(num):
                t = num[i]
                if t > num[i]:
                    i, t = t, i
        print(num)
    except ValueError:
        print("Não é um valor inteiro.")