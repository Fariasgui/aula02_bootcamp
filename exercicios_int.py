# #### Inteiros (`int`)

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.
a = int(input("Digite um número: "))
b = int(input("Digite um número: "))
soma = a + b
print(f"A soma dos dois números é: {soma}")
# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
numero = int(input("Digite um número: "))
rest_div = numero % 5
print(f"O resto da divisão é: {rest_div}") 
# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
mult_1 = int(input("Digite um número: "))
mult_2 = int(input("Digite um número: "))
multi = mult_1 * mult_2
print(f"A multiplicação dos dois números é: {multi}")
# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
div_1 = int(input("Digite um número: "))
div_2 = int(input("Digite um número: "))
divi = div_1 // div_2
print(f"A divisão dos dois números é: {divi}")
# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
exp_1 = int(input("Digite um número: "))
expo = exp_1 ** 2
print(f"O quadrado do número é: {expo}")