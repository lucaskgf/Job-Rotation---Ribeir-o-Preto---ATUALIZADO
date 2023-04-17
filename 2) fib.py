num = int(input("Informe um número inteiro: "))

fibonacci = [0, 1]  # iniciando a sequência com 0 e 1

while fibonacci[-1] < num:
    # adicionando os próximos valores da sequência
    next_val = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(next_val)

if num in fibonacci:
    print(f"{num} pertence à sequência de Fibonacci!")
else:
    print(f"{num} não pertence à sequência de Fibonacci.")