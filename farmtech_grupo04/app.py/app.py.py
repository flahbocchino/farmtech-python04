import math
import csv
import os

# Definição das culturas e estrutura de dados
culturas = ["Laranja", "Café"]
dados_plantio = []

def calcular_area(tipo_area, medida1, medida2=None):
    if tipo_area == "retangular":
        return medida1 * medida2
    elif tipo_area == "circular":
        return math.pi * (medida1 ** 2)
    else:
        return None

def inserir_dados():
    print("\nOpções de culturas disponíveis:", culturas)
    cultura = input("Escolha a cultura: ").capitalize()

    if cultura not in culturas:
        print("Cultura inválida.")
        return

    tipo_area = input("Digite o tipo de área (retangular/circular): ").lower()
    if tipo_area == "retangular":
        largura = float(input("Informe a largura (m): "))
        comprimento = float(input("Informe o comprimento (m): "))
        area = calcular_area(tipo_area, largura, comprimento)
    elif tipo_area == "circular":
        raio = float(input("Informe o raio (m): "))
        area = calcular_area(tipo_area, raio)
    else:
        print("Tipo de área inválido.")
        return

    dados_plantio.append({"cultura": cultura, "tipo_area": tipo_area, "area": area})
    print("\n✅ Dados inseridos com sucesso!")

def listar_dados():
    if not dados_plantio:
        print("\n📌 Nenhum dado cadastrado.")
        return
    print("\n📋 Lista de áreas cadastradas:")
    for i, d in enumerate(dados_plantio):
        print(f"ID {i}: Cultura: {d['cultura']}, Tipo de Área: {d['tipo_area']}, Área: {d['area']:.2f} m²")

def salvar_csv():
    if not os.path.exists("data"):
        os.makedirs("data")
    with open("data/plantio.csv", "w", newline="") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(["Cultura", "Tipo de Área", "Área"])
        for d in dados_plantio:
            escritor.writerow([d["cultura"], d["tipo_area"], d["area"]])
    print("\n📂 Dados salvos em data/plantio.csv para análise no R!")

# Menu principal
while True:
    print("\n🌱 MENU PRINCIPAL 🌱")
    print("1 - Inserir dados de plantio")
    print("2 - Listar dados cadastrados")
    print("3 - Salvar dados para análise no R")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        inserir_dados()
    elif opcao == "2":
        listar_dados()
    elif opcao == "3":
        salvar_csv()
    elif opcao == "4":
        print("\n🚪 Saindo do programa...")
        break
    else:
        print("\n❌ Opção inválida. Tente novamente.")
