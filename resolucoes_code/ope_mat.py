# como solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles em python

# Você pode solicitar como entrada dois números do usuário e realizar uma operação simples entre eles em Python usando a função `input()` para obter os números e depois realizar a operação desejada. Aqui está um exemplo:

# Solicita os números como entrada do usuário
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

# Realiza a operação desejada (por exemplo, soma)
soma = numero1 + numero2

# Exibe o resultado
print("A soma de {} e {} é igual a {}".format(numero1, numero2, soma))

# Neste exemplo, o usuário é solicitado a inserir dois números. Os números são então convertidos em `float` usando `float(input())` para garantir que possam ser tratados como números decimais. Depois, a soma dos dois números é calculada e exibida como saída. Você pode substituir `soma = numero1 + numero2` pela operação desejada, como subtração, multiplicação ou divisão.

# como montar um lógica, em python, para pedir ao usuário qual operação matemática simples ele deseja efetuar, a partir de dois números solicitados com entrada

# Você pode montar uma lógica em Python para solicitar ao usuário qual operação matemática simples ele deseja efetuar, a partir de dois números solicitados como entrada, usando uma estrutura condicional (`if`, `elif`, `else`). Aqui está um exemplo:


# Solicita os números como entrada do usuário
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

# Solicita a operação desejada ao usuário
print("Escolha a operação desejada:")
print("1. Soma")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")
operacao = input("Digite o número da operação: ")

# Converte a operação para inteiro
operacao = int(operacao)

# Realiza a operação escolhida e exibe o resultado
if operacao == 1:
    resultado = numero1 + numero2
    print("A soma de {} e {} é igual a {}".format(numero1, numero2, resultado))
elif operacao == 2:
    resultado = numero1 - numero2
    print("A subtração de {} por {} é igual a {}".format(numero1, numero2, resultado))
elif operacao == 3:
    resultado = numero1 * numero2
    print("A multiplicação de {} por {} é igual a {}".format(numero1, numero2, resultado))
elif operacao == 4:
    if numero2 != 0:  # Verifica se o segundo número não é zero para evitar divisão por zero
        resultado = numero1 / numero2
        print("A divisão de {} por {} é igual a {}".format(numero1, numero2, resultado))
    else:
        print("Não é possível dividir por zero!")
else:
    print("Opção inválida! Por favor, escolha uma opção válida de 1 a 4.")


# Neste exemplo, o usuário é solicitado a escolher a operação desejada digitando o número correspondente. Em seguida, o programa usa uma estrutura condicional para realizar a operação selecionada e exibir o resultado. Além disso, há uma verificação extra para evitar a divisão por zero.
