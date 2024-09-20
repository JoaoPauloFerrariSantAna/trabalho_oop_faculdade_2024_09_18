from Mercadoria import Mercadoria

def main() -> int:

	while(True):
		nome = input("Nome do produto: ")
		tipo = input("Tipo do produto: ")
		peso = float(input("Peso do produto (gramas): "))
		custo = float(input("Qual é o preço do produto? "))

		mercadoria: Mercadoria = Mercadoria(nome, tipo, peso, custo)


	return 0

if(__name__ == "__main__"):
	main()
