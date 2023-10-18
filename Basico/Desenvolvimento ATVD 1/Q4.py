# Questão 4 - Escreva um programa em Python que calcule o fatorial de um
# número inteiro não negativo fornecido pelo usuário.

# Fatorial é uma operação matemática que consiste em multiplicar todos os números existente entre 1 e n

# Recebendo o número do usuário
n = int(input("Digite um número: "))

# Relacionando a variavel fat com n
fat = n

# Percorrendo todos os numeros existentes entre 1 e n
for i in range(n-1, 0, -1):
   fat = fat * i # Multiplicando os números

print(f"{n}! = {fat}")