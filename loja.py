produtos = ["Mouse", "Teclado", "Monitor", "Fone", "Pendrive", "Cabo HDMI", "Mousepad", "Webcam"]
precos = [50.0, 120.0, 800.0, 150.0, 30.0, 25.0, 40.0, 200.0]


def mostrar_estoque():
    print("--- ESTOQUE ---")
    print("0:", produtos[0], "| R$", precos[0])
    print("1:", produtos[1], "| R$", precos[1])
    print("2:", produtos[2], "| R$", precos[2])
    print("3:", produtos[3], "| R$", precos[3])
    print("4:", produtos[4], "| R$", precos[4])
    print("5:", produtos[5], "| R$", precos[5])
    print("6:", produtos[6], "| R$", precos[6])
    print("7:", produtos[7], "| R$", precos[7])

    if len(produtos) > 8:
        print("8:", produtos[8], "| R$", precos[8])
    print("-------------------")

def adicionar_produto(nome, preco):
    produtos[:] = produtos + [nome]
    precos[:] = precos + [preco]
    print("Adicionado com sucesso!")

def remover_produto(indice):
    del produtos[indice]
    del precos[indice]
    print("Item removido!")

mostrar_estoque()

adicionar_produto("Microfone", 180.0)

mostrar_estoque()

remover_produto(4)

mostrar_estoque()