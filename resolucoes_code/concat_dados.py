"""
Manipular strings no Python é uma tarefa comum e há várias maneiras de fazê-lo. Aqui estão algumas das operações mais comuns que você pode fazer:

1. **Concatenação de Strings**: Use o operador `+` para juntar duas ou mais strings.

```python
s1 = "Olá"
s2 = " mundo"
s3 = s1 + s2
print(s3)  # Saída: "Olá mundo"
```

2. **Indexação de Strings**: Você pode acessar caracteres individuais de uma string usando índices.

```python
s = "Python"
print(s[0])   # Saída: "P"
print(s[-1])  # Saída: "n"
```

3. **Fatiamento de Strings**: Você pode obter substrings usando a sintaxe `[start:stop:step]`.

```python
s = "Python"
print(s[0:2])   # Saída: "Py"
print(s[2:])    # Saída: "thon"
print(s[:4])    # Saída: "Pyth"
print(s[::2])   # Saída: "Pto"
```

4. **Métodos de String**: O Python possui muitos métodos embutidos para manipulação de strings, como `split()`, `strip()`, `upper()`, `lower()`, `replace()`, etc.

```python
s = "   Olá, mundo!   "
print(s.strip())         # Remove espaços em branco do início e do fim
print(s.split(", "))     # Divide a string em uma lista usando ", " como delimitador
print(s.upper())         # Converte a string em maiúsculas
print(s.lower())         # Converte a string em minúsculas
print(s.replace("Olá", "Oi"))  # Substitui "Olá" por "Oi"
```

5. **Formatação de Strings**: Use formatação de strings para inserir valores em uma string.

```python
nome = "Maria"
idade = 30
mensagem = "Olá, meu nome é {} e eu tenho {} anos.".format(nome, idade)
print(mensagem)  # Saída: "Olá, meu nome é Maria e eu tenho 30 anos."
```

Estas são apenas algumas das maneiras de manipular strings no Python. Há muitas outras operações e métodos disponíveis, dependendo do que você precisa fazer.

Resposta a pergunta realizada ao chatGPT sobre manipulação de strings.
"""

# Vamos receber dois dados diferentes do usuário e concatena-los em uma única string?!

# Solicita ao usuário que insira seu nome e armazena a entrada em uma variável
nome = input("Por favor, digite seu nome: ")
sobre_nome = input("Por favor, digite seu sobrenome: ") 

# Imprime uma mensagem de boas-vindas usando o nome fornecido pelo usuário
print("Oi,", nome + ' ' + sobre_nome, "! Bem-vindo ao Python!")
