from veiculos.aereo.Aereo import Aereo

class JatoGuerra(Aereo):
    def __init__(self, nome, quantidadeMisseis):
        super().__init__(nome)
        self.quantidadeMisseis = quantidadeMisseis

    def atirarMissel(self):
        if self.quantidadeMisseis <=0:
            print("Não há mais misseis no Jato")
        else:
            self.quantidadeMisseis -= 1
            print("Missil atirado. Misseis restantes:",self.quantidadeMisseis)
    
    def ganharAltitude(self, incremento):
        if self._velocidade >= 1000:
            super().ganharAltitude(incremento)
        else:
            print("E necessario mais velocidade para ganhar altitude")

    def perderAltitude(self, decremento):
        super().perderAltitude(decremento)   
        if self.altitude < 0:
            self.altitude = 0

    def mostrarInfo(self):
        super().mostrarInfo()
        print("Altitude:",self.altitude)
        print("Misseis:",self.quantidadeMisseis)
