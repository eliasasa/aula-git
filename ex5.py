# 5  - Desenvolva uma função que mostre os n primeiros termos da sequência de Fibonacci, onde n é informado pelo usuário.

while True:
    fib = [1, 1]
    try:
        quant = int(input("Escreva a quantidade de termos que deseja da sequêncua de Fibonacci:\n"))
        for i in range(2, quant):
            alfa = fib[i - 1] + fib[i - 2]
            fib.append(alfa)
        print(fib)
    except ValueError:
        print("Não é um valor inteiro.")