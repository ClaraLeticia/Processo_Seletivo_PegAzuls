# Questão 2 - Escreva um programa em Python que crie uma lista com os
# primeiros 20 números da sequência de Fibonacci e imprima essa lista
# A sequência de Fibonacci é uma sequência matemática que começa com 0 e 1,
# e os números subsequentes são a soma dos dois números anteriores.

fib = [0, 1] # Criando uma lista, que inicia com 0 e 1, para armazenar a sequência

# A primeira operação vai ser a soma dos dois primeiros números, já existentes na lista

for i in range(1, 20):
   soma = fib[i] + fib[i - 1] # Fazendo a soma do número atual, com seu antecessor
   fib.append(soma) # Adicionando o novo número, criado na soma, a lista

# Imprimindo a lista
for i in range(0,20):
   print(fib[i])
