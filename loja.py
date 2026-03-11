/*
Imagine que você abriu uma loja:
1) Crie o nome de 8 produtos e armazene em uma lista;
2) Crie outra lista para armazenar o preço de cada produto.
3) Crie uma função para mostrar o estoque, mostrando o nome da cada produto e o seu preço.
4) Crie uma função que adiciona um novo produto (e consequentemente um novo preço)
5) Crie uma função que remove um produto da lista recebendo seu índice.
6) EXECUTE AS FUNÇÕES CRIADAS NA SEGUINTE ORDEM:
    - mostra estoque
    - adiciona produto
    - mostra estoque
    - remove um elemento pelo índice
    - mostra estoque
*/

const produtos = ["Mouse", "Teclado", "Monitor", "Fone", "Pendrive", "Cabo HDMI", "Mousepad", "Webcam"]
const precos = [50, 120, 800, 150, 30, 25, 40, 200]

function mostrarEstoque() {
    let contador = 0
    console.log("--- ESTOQUE ATUAL ---")
    while (contador < produtos.length) {
        console.log(produtos[contador] + " - R$ " + precos[contador])
        contador++
    }
    console.log("--------------------")
}

function adicionarProduto(nome, preco) {
    produtos.push(nome)
    precos.push(preco)
    console.log("Produto adicionado: " + nome + " | Valor: R$ " + preco)
}

function removerProduto(indice) {
    console.log("Removido o item: " + produtos[indice])
    produtos.splice(indice, 1)
    precos.splice(indice, 1)
}

mostrarEstoque()

adicionarProduto("Microfone", 180)

mostrarEstoque()

removerProduto(4)

mostrarEstoque()
