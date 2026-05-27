from veiculos.terrestre.Terrestre import Terrestre

class Carro(Terrestre):
    def __init__(self, nome, numeroRodas, tipoCombustivel):
        super().__init__(nome, numeroRodas)
        self._tipoCombustivel = tipoCombustivel

    def mover(self):
        print(f"O carro {self._nome} está se movendo com a velocidade de {self._velocidade} km/h.")

    def mostrarInfo(self):
        super().mostrarInfo()
        print("Número de rodas:",self._numeroRodas)
        print("Tipo de combustível:",self._tipoCombustivel)
