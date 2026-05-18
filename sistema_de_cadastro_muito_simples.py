cadastros = []
print("=== SISTEMA DE CADASTRO ===")
print("1. Cadastrar pessoa")
print("2. Listar cadastros")
print("3. Sair")

x = int(input("Escolha uma opção: "))


while x != 3:
    if x == 1:
        nome = input("Nome: ")
        idade = input("Idade: ")
        cidade = input("Cidade: ")
        pessoa = f"{nome} | {idade} anos | {cidade}"
        cadastros.append(pessoa)
        print("Cadastro efetuado! ")
        
    elif x == 2:
        if len(cadastros) == 0:
            print("Nenhum cadastro encontrado")
        else:    
            print("\n=== Cadastros ===")
            for cadastro in (cadastros):
                print(f"- {cadastro}")
    else:
        print("Número inválido tente novamente")

    print("=== SISTEMA DE CADASTRO ===")
    print("1. Cadastrar pessoa")
    print("2. Listar cadastros")
    print("3. Sair")
    x = int(input("Escolha uma opção: "))            

print("Adeus volte sempre")