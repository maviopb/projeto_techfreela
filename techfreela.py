#Você foi contratado para criar um programa em Python para ajudar um designer freelancer a calcular rapidamente o valor de um trabalho.

#Crie um programa chamado TechFreela.

"""
O sistema deverá perguntar ao usuário:
-Nome do cliente
-Nome do projeto
-Quantidade de artes que serão produzidas
-Valor cobrado por cada arte
-Quantidade de horas previstas para o trabalho
-Valor cobrado por hora

Depois, o programa deverá calcular:
-Valor das artes
-Valor das horas trabalhadas
-Valor total do projeto

"""
print("TECHFREELA")

nome = input("Digite seu nome: ")
print(f"Seja Bem-vindo, {nome}")

print("Calculo Rapido:")
nome_cliente = input("Digite o nome do cliente: ")
nome_projeto = input("Digite o nome do projeto: ")
qnt_artes = float(input("Digite a quantidade de artes que serão produzidas: "))
cobraca_artes = float(input("Digite o valor cobrado por cada arte: "))
qnt_horas = float(input("Digite a quantidade de horas prevista para finalizar o projeto: "))
cobraca_horas =  float(input("Digite o valor cobrado por hora: "))

print("Calculando!!")


valor_arte = (qnt_artes * cobraca_artes)
valor_horas = (qnt_horas * cobraca_horas)

valor_total = (valor_arte + valor_horas)

print(f"Em nosso calculo, seu valor cobrado por arte é: {valor_arte}, e o valor de horas trabalhadas é: {valor_horas}")
print(f"Consequentemente o valor total do projeto é: {valor_total}")

print("SUCESSO NO PROJETO!")