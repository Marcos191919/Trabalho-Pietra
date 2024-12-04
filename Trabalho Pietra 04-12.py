tabela_fipe = {
    "Fusca 1976": 18000, "Civic 2020": 85000, "Gol 2015": 35000, "Hilux 2022": 150000, "Fiesta 2018": 43000}

veiculos_disponiveis = [
    {"marca": "Fusca 1976", "modelo": "Fusca", "valor": 18000},
    {"marca": "Civic 2020", "modelo": "Civic", "valor": 85000},
    {"marca": "Gol 2015", "modelo": "Gol", "valor": 35000},
    {"marca": "Hilux 2022", "modelo": "Hilux", "valor": 150000},
    {"marca": "Fiesta 2018", "modelo": "Fiesta", "valor": 43000}
]

def vender_veiculo(cliente):
    print("Informe o veículo que deseja vender (marca e modelo):")
    marca_modelo = input().strip()
    
    if marca_modelo in tabela_fipe:
        valor_veiculo = tabela_fipe[marca_modelo]
        valor_oferta = valor_veiculo * 0.88
        print(f"Avaliamos seu veículo em R${valor_oferta:.2f}. Deseja vender? (S/N)")

        if input().strip().upper() == 'S':
            cliente['saldo'] += valor_oferta
            veiculos_disponiveis.append({"marca": marca_modelo, "modelo": marca_modelo.split()[0], "valor": valor_oferta})
            print(f"Venda concluida. Seu novo saldo é R${cliente['saldo']:.2f}.")
        else:
            print("Venda cancelada ! ")
    else:
        print("Veículo não encontrado na tabela FIPE.")

def alugar_veiculo(cliente):
    print("Escolha o veículo que deseja alugar: ")
    for idx, veiculo in enumerate(veiculos_disponiveis):
        print(f"{idx + 1}. {veiculo['marca']} - R$77/dia")

    opcao = int(input("Escolha o número do veículo (ou 0 para cancelar): ")) - 1
    if opcao == -1:
        print("Aluguel cancelado ! ")
        return

    veiculo_escolhido = veiculos_disponiveis[opcao]
    print("Informe o número de dias que deseja ter o carro alugado: ")
    dias = int(input())
    custo_total = dias * 77

    if cliente['saldo'] >= custo_total:
        cliente['saldo'] -= custo_total
        veiculos_disponiveis.pop(opcao)
        print(f"Aluguel realizado com sucesso. Seu novo saldo é R${cliente['saldo']:.2f}.")
    else:
        print("Saldo insuficiente para o aluguel.")

def comprar_veiculo(cliente):
    print("Escolha o veículo que deseja comprar: ")
    for idx, veiculo in enumerate(veiculos_disponiveis):
        print(f"{idx + 1}. {veiculo['marca']} - R${veiculo['valor'] * 1.25:.2f}")

    opcao = int(input("Escolha o número do veículo (ou 0 para cancelar): ")) - 1
    if opcao == -1:
        print("Compra cancelada ! ")
        return

    veiculo_escolhido = veiculos_disponiveis[opcao]
    valor_comprado = veiculo_escolhido["valor"] * 1.25

    if cliente['saldo'] >= valor_comprado:
        cliente['saldo'] -= valor_comprado
        veiculos_disponiveis.pop(opcao)
        print(f"Compra realizada com sucesso! Seu novo saldo é R${cliente['saldo']:.2f}.")
    else:
        print("Saldo insuficiente para a compra.")

def menu():

    nome = input("Informe seu nome: ")
    telefone = input("Informe seu telefone: ")
    saldo = float(input("Informe seu saldo disponível R$"))

    cliente = {"nome": nome, "telefone": telefone, "saldo": saldo}

    while True:
        print("\n----BEM-VINDO AO MENU DE COMPRA----")

        print("\nOPÇÃO 1 - VENDER VEÍCULO \nOPÇÃO 2 - ALUGAR VEÍCULO \nOPÇÃO 3 - COMPRAR VEÍCULO \nOPÇÃO 4 - SAIR ")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            vender_veiculo(cliente)
        elif opcao == '2':
            alugar_veiculo(cliente)
        elif opcao == '3':
            comprar_veiculo(cliente)
        elif opcao == '4':
            print("Obrigado por usa o menu da loja...")
            break
        else:
            print("Opção inválida. Tente novamente.")
menu()
