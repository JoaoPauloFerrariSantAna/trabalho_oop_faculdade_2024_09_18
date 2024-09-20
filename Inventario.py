class Inventario:
	def __init__(self) -> None:
		# aparentemente esse "_" mostra que não é para
		# usar "_inventario" fora da classe
		self._inventario = []
	
	def adicionarMercadoria(self, item: dict[str, str | float]) -> None:
		self._inventario.append(item)
	
	def mostrarInventario(self) -> None:
		print(self.inventario)
