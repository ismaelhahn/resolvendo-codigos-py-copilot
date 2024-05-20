# Vamos solicitar uma string e um número inteiro como entrada e depois vamos realizar uma operação simples entre eles, em python

# ChatGPT: Claro! Aqui está um exemplo simples em Python de como solicitar uma string e um número inteiro como entrada do usuário e realizar uma operação simples entre eles:

# Solicitar uma string do usuário
string = input("Digite uma string: ")

# Solicitar um número inteiro do usuário
numero = int(input("Digite um número inteiro: "))

# Realizar uma operação simples entre a string e o número
resultado = string * numero

# Imprimir o resultado
print("Resultado da operação:", resultado)
# Neste exemplo, a operação simples é a multiplicação da string pelo número inteiro, o que resulta na repetição da string a quantidade de vezes especificada pelo número.

# mais exemplos
# ChatGPT: Claro! Aqui estão alguns exemplos adicionais de operações simples que você pode realizar com uma string e um número inteiro em Python:

# Concatenação da string com ela mesma um número específico de vezes:

string = input("Digite uma string: ")
numero = int(input("Digite um número inteiro: "))
resultado = string * numero
print("Resultado da concatenação:", resultado)

# Repetição da string um número específico de vezes, cada vez com um espaço entre elas:

string = input("Digite uma string: ")
numero = int(input("Digite um número inteiro: "))
resultado = (string + " ") * numero
print("Resultado da repetição com espaços:", resultado)

# Formatação de uma frase com a string repetida um número específico de vezes:
 
string = input("Digite uma string: ")
numero = int(input("Digite um número inteiro: "))
resultado = "Eu gosto de " + (string + " ") * numero
print("Frase formatada:", resultado)
# Estes são apenas alguns exemplos simples, mas você pode realizar uma variedade de operações diferentes dependendo dos requisitos específicos do seu programa.

# mais exemplos
# ChatGPT: Claro, aqui estão mais alguns exemplos de operações simples que você pode realizar com uma string e um número inteiro em Python:

#Imprimir a string um número específico de vezes, cada vez em uma nova linha:

string = input("Digite uma string: ")
numero = int(input("Digite um número inteiro: "))
for _ in range(numero):
    print(string)

# Imprimir cada caractere da string repetido um número específico de vezes:

string = input("Digite uma string: ")
numero = int(input("Digite um número inteiro: "))
for char in string:
    print(char * numero)

# Criar uma lista contendo a string repetida um número específico de vezes:

string = input("Digite uma string: ")
numero = int(input("Digite um número inteiro: "))
lista_repetida = [string] * numero
print("Lista com a string repetida:", lista_repetida)

# Estes exemplos demonstram algumas maneiras de manipular uma string e um número inteiro em Python para realizar diferentes tipos de operações simples.

# mais exemplos
# ChatGPT: Claro, aqui estão mais alguns exemplos de operações simples que você pode realizar com uma string e um número inteiro em Python:

# Substituir um caractere específico da string por um símbolo especial, repetindo o processo para cada ocorrência desse caractere:

string = input("Digite uma string: ")
caractere = input("Digite o caractere a substituir: ")
simbolo = input("Digite o símbolo especial para substituição: ")

# Contando o número de ocorrências do caractere na string
num_ocorrencias = string.count(caractere)

# Substituindo o caractere pelo símbolo especial e imprimindo o resultado
resultado = string.replace(caractere, simbolo)
print("Resultado da substituição:", resultado)

# Criar uma nova string que contenha a string original repetida um número específico de vezes, mas com uma formatação especial:

string = input("Digite uma string: ")
numero = int(input("Digite um número inteiro: "))

# Formatar a string com números crescentes separados por vírgula
nova_string = ', '.join([string] * numero)
print("Nova string formatada:", nova_string)

# Realizar uma operação de slicing na string com base no número inteiro fornecido pelo usuário:

string = input("Digite uma string: ")
numero = int(input("Digite um número inteiro (índice de slicing): "))

# Realizar slicing na string com base no número inteiro
substring = string[:numero]
print("Substring resultante:", substring)

# Esses exemplos demonstram algumas operações adicionais que você pode realizar com uma string e um número inteiro em Python. Existem várias maneiras de manipular strings e números para atender às necessidades específicas do seu programa.
