#Calculadora de Bônus
print("Olá, bem vindo ao cálculo de bônus 2024")
try:
    nome = str(input("Digite seu nome: "))
    if len(nome) == 0:
        raise ValueError("O nome não pode estar vazio")
    elif any(char.isdigit() for char in nome):
        raise ValueError("O nome não deve conter números")
    else:
        print("Nome válido:", nome)
except ValueError as e:
    print(e)

try:
    salario = float(input("Digite seu salário: "))
    if salario < 0:
        print("Por favor, digite um salário com valor positivo")
except ValueError:
    print("Entrada inválida para o salário. Digite um número.")

try:
    porc_bonus = float(input("Qual a porcentagem do bônus: "))
    if porc_bonus < 0:
        print("Por favor, digite um valor positivo para o bônus")
except ValueError:
    print("Entrada inválida. Por gentileza, digite um número percentual de bônus.")

kpi_bonus = 1000 + salario * porc_bonus
print(f"Olá {nome}, o seu bônus em 2024 foi de {kpi_bonus}")
