from Inventario import Inventario
from Mercadoria import Mercadoria

def main() -> int:
	inventario: Inventario = Inventario()

	while(True):
		op = input("Gostaria de [v]er itens que estão no inventário u [i]nseri-los? ")

		if(op == 'i'):
			nome = input("Nome do produto: ")
			tipo = input("Tipo do produto: ")
			peso = float(input("Peso do produto (gramas): "))
			custo = float(input("Qual é o preço do produto? "))

			mercadoria: Mercadoria = Mercadoria(nome, tipo, peso, custo)
			inventario.adicionarMercadoria(mercadoria)

		if(op == 'v'):
			inventario.mostrarInventario()

	return 0

if(__name__ == "__main__"):
	main()
