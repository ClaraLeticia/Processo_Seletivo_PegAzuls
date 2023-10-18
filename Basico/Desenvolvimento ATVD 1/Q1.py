# Quesão 1 - Escreva um programa em Python que receba um número inteiro do usuário
# e determine se esse número é primo ou não.


# Recebendo um número inteiro
num = int(input("Digite um número inteiro: "))


# Para ele ser primo ele tem que ser divisivel apenas por dois números, 1 e ele mesmo
# É preciso verificar se de 1 até o número digitado existe apenas dois números que
# dividem "num" inteiramente (ou seja, que o resto da divisão seja zero)

# Variavel para armazenar quantos numeros dividem "num"
cont = 0

for i in range(1, num+1): # O "+1 adicionado serve para a estrutura percorrer até o número digitado, caso contrário só iria até o número anterior
   if(num%i == 0): #Verificando se o resto da divisão é igual a 0
       cont+= 1 # Caso seja, é somado 1 a variável


if(cont == 2): # Caso a variavel tenha valor 2
   print(f"{num} é um número primo")
else:
   print(f"{num} não é um número primo")
