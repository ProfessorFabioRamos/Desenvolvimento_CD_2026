from veiculos.Veiculo import Veiculo

class Aereo(Veiculo):
    def __init__(self, nome):
        super().__init__(nome)
        self.altitude = 0
    
    def ganharAltitude(self, incremento):
        self.altitude += incremento

    def perderAltitude(self, decremento):
        self.altitude -= decremento
