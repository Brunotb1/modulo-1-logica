nome = input("Qual o seu nome? " )
idade = int(input("Qual a sua idade? " ))

ano_atual = 2026
ano_nascimento = ano_atual - idade

altura = float(input("Digite a sua altura(em metros): " ))
peso = float(input("Digite o seu peso(em kg): "))

imc = peso / (altura ** 2)
print("=== Seus dados ===")
print(f"Olá, {nome}!")
print(f"Você nasceu no ano de {ano_nascimento}.")
print(f"Daqui 10 anos você terá {idade + 10} anos.")
print (f"Seu IMC é {imc :.2f}")