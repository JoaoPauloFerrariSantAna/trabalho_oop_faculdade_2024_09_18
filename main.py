from Inventario import Inventario
from Mercadoria import Mercadoria

def main() -> int:
	inventario: Inventario = Inventario()

	while(True):
		op = input("Gostaria de [v]er items ou [a]dicionar? ")

		if(op == 'a'):
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
