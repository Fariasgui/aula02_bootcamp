# #### Números de Ponto Flutuante (`float`)
import math
# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.
a = float(input("Digite um número: "))
b = float(input("Digite um número: "))
soma = a + b
print(f"A soma dos dois números é: {soma}")
# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
num_1 = float(input("Digite um número: "))
num_2 = float(input("Digite um número: "))
media = (num_1 + num_2) / 2
print(f"A média dos dois números é: {media}")
# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
num_3 = float(input("Digite um número: "))
num_4 = float(input("Digite um número: "))
expo = num_3 ** num_4
print(f"A potência dos dois números é: {expo}")
# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
temperatura = float(input("Digite a temperatura em Celsius: "))
conversao = (temperatura * (9/5)) + 32
print(f"A temperatura em Fahrenheit é de: {conversao}°F")
# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
raio = float(input("Digite o raio: "))
area_circulo = math.pi * raio ** 2
print(f"A área do círculo é: {area_circulo}")