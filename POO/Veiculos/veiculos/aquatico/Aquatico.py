from veiculos.Veiculo import Veiculo

class Aquatico(Veiculo):
    def __init__(self, nome, possuiHelice):
        super().__init__(nome)
        # Boolean True/False
        self.possuiHelice = possuiHelice
