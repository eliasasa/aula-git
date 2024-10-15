# 4 - Faça um programa que verifique se um número fornecido é primo.

while True:
    try:
        quant = int(input("Escreva a quantidade de números que deseja inserir:\n"))
        for i in range(quant):
            num = i + 1
            print(num)
    except ValueError:
        print("Não é um valor inteiro.")