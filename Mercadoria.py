class Mercadoria:
	def __init__(self, nome: str, tipo: str, peso: float, preco: float) -> None:
		self.nome = nome
		self.tipo = tipo
		self.peso = peso
		self.preco = preco

	def gerarInformacao(self) -> dict:
		return {
			"nome" : self.nome,
			"tipo" : self.tipo,
			"peso" : self.peso,
			"preco" : self.preco
		}
