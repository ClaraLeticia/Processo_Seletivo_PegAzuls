# Questão 5 -Um número palíndromo é aquele que permanece o mesmo
# quando lido de trás para frente. Por exemplo, 121, 1331 e 555 são números
# palíndromos. Escreva um programa em Python que encontre o maior número
# palíndromo que é o produto de dois números de 3 dígitos.

# Criando uma lista vazia para armazenar os palindromos
palindromo = []
for i in range(100, 1000): # Para percorrer todos os numeros de tres digitos, 100 a 999
    for j in range(100, 1000): # Para percorrer todos os numeros de tres digitos, 100 a 999
        mult = i * j # Realizando a multiplicação
        res = str(mult) # Transformando o resultado da multiplicação (inteiro) em string
        contrario = res[::-1] # Invertendo o valor
        if (res == contrario): # Verificando se a string da multiplicação é igual ao seu inverso
            palindromo.append(mult) # Caso seja igual, o valor da multiplicação sera adicionado a lista de palindromos

# Imprimindo o valor mais alto
print(f"o maior número palíndromo que é o produto de dois números de 3 dígitos é: {max(palindromo)}")

