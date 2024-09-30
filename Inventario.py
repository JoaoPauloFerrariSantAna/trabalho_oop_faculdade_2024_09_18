class Inventario:
	def __init__(self) -> None:
		# aparentemente esse "_" mostra que não é para
		# usar "_inventario" fora da classe
		self._inventario = []

	def adicionarMercadoria(self, item: dict[str, str | float]) -> None:
		self._inventario.append(item)

	def mostrarInventario(self) -> None:
		print("Items no inventário:")

		# vai loopar por todo o inventário
		for item in range(len(self._inventario)):
			nome_merc = self._inventario[item].nome
			tipo_merc = self._inventario[item].tipo
			peso_merc = self._inventario[item].peso
			preco_merc = self._inventario[item].preco

			print(f"- {nome_merc} ({tipo_merc}): R${preco_merc}, {peso_merc} gramas")
