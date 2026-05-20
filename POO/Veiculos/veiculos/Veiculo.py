class Veiculo:
    def __init__(self, nome):
        self._nome = nome
        self._velocidade = 0

    def acelerar(self, incremento):
        if incremento > 0:
            self._velocidade += incremento

    def desacelerar(self, decremento):
        if decremento > 0:
            self._velocidade -= decremento

    def mostrarInfo(self):
        print("Nome:",self._nome)
        print("Velocidade Atual:",self._velocidade)
