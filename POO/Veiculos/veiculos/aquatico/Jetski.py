from veiculos.aquatico.Aquatico import Aquatico

class Jetski(Aquatico):
    def __init__(self, nome, possuiHelice, tripulantes):
        super().__init__(nome, possuiHelice)
        self.tripulantes = tripulantes

    def embarcar(self, quantidade):
        if quantidade > 2:
            print("Não é possível embarcar esta quantidade")
        else:
            self.tripulantes += quantidade
    
    def desembarcar(self, quantidade):
        self.tripulantes -= quantidade
        if self.tripulantes < 0:
            self.tripulantes = 0
