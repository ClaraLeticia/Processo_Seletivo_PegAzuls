# Questão 3 - Escreva um programa em Python que receba uma lista de
# números do usuário e imprima na tela apenas os números únicos da lista (ou
# seja, números que aparecem uma única vez).


# Pergutando quantos números o usuario deseja colocar na lista
qtd = int(input("Quantos números você deseja colocar na lista: "))


# Criando a lista vazia
lista = []


# Adicionando números a lista
for i in range(0, qtd):
   num = int(input("Digite um número: "))
   lista.append(num)


# Criando uma nova lista para armazenar apenas o valores não repetidos
nova_lista = []


for i in lista: # Acessando os valores existentes na lista fornecida pelo o usuário
   # A função "count" realiza a quantidade de vezes que um elemento a aparece na lista
   if lista.count(i) == 1: # Dessa forma se o valor for igual a 1 então esse valor só apareceu uma vez
       nova_lista.append(i) # Adicionando o valor a nova lista


# Imprimindo a nova lista
print(f"Os números não repetidos foram: {nova_lista}")
