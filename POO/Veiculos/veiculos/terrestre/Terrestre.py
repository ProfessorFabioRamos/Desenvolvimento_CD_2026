from veiculos.Veiculo import Veiculo

class Terrestre(Veiculo):
    def __init__(self, nome, numeroRodas):
        super().__init__(nome)
        self._numeroRodas = numeroRodas
