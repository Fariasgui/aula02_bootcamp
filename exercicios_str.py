# #### Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
nome = str(input("Digite seu primeiro nome: "))
nome_maiusculo = nome.upper()
print(nome_maiusculo)
# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
nome_completo = str(input("Digite seu primeiro nome: "))
nome_c_maiusculo = nome_completo.upper()
print(nome_c_maiusculo)
# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
frase = str(input("Digite uma frase: "))
frase_ajust = frase.strip()
print(frase_ajust)
# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
data = str(input("Digite uma data no formato DD/MM/AAAA: "))
dia, mes, ano = data.split("/")
print(f"Dia: {dia}")
print(f"Mês: {mes}")
print(f"Ano: {ano}")
# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.
str_1 = str(input("Digite uma palavra: "))
str_2 = str(input("Digite outra palavra: "))
concat = str_1 + str_2 
print(f"Texto concatenado: {concat}")