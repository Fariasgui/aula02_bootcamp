# #### try-except e if

# 21: Conversor de Temperatura
try:
    temperatura = float(input("Digite a temperatura em Celsius: "))
    conversao = (temperatura * 9/5) + 32
    print(f"A temperatura em Fahrenheit é de: {conversao:.2f}°F")
except ValueError:
    print("Erro: Por favor, digite um valor numérico válido para a temperatura.\n")
# 22: Verificador de Palíndromo
entrada = input("Digite sua frase aqui: ")
if isinstance(entrada, str):
    formatado = entrada.replace(" ", "").lower()
    if formatado == formatado[::-1]:
        print("É um palíndromo")
    else:
        print("Não é um palíndromo")
else:
    print("Entrada inválida. Por favor, digite uma palavra ou frase.")
# 23: Calculadora Simples
try:
    num_1 = float(input("Digite o primeiro número: "))
    num_2 = float(input("Digite o segundo número: "))
    ope = input("Escolha uma operação(+, -, *, /): ")
    if ope == "+":
        resultado = num_1 + num_2
    elif ope == "-":
        resultado = num_1 - num_2
    elif ope == "*":
        resultado = num_1 * num_2
    elif ope == "/":
        resultado = num_1 / num_2
    else:
        print("Digite uma operação válida ou divisão por zero")
    print("Resultado:", resultado)
except ValueError:
    print("Erro: Entrada inválida. Certifique-se de inserir números.")
# 24: Classificador de Números
try:
    numero = int(input("Digite um número: "))
    if numero > 0:
        print("Positivo")
    elif numero < 0:
        print("Negativo")
    else:
        print("Zero")
    if numero % 2 == 0:
        print("Par")
    else:
        print("Ímpar")
except ValueError:
    print("Por favor, digite um número inteiro válido.")
# 25: Conversão de Tipo com Validação
entrada_lista = input("Digite uma lista de números separados por vírgula: ")
numeros_str = entrada_lista.split(",")
numeros_int = []
try:
    for num in numeros_str:
        numeros_int.append(int(num.strip()))
    print("Lista de inteiros:", numeros_int)
except ValueError:
    print("Erro: certifique-se de que todos os elementos são números inteiros válidos.")