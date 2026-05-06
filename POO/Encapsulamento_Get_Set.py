class Carro:
    def __init__(self,marca,modelo,ano):
        self.marca = marca      # public
        self._modelo = modelo   # private fraco
        self.__ano = ano        # private forte   
        self.velocidade = 0

    def showInfo(self):
        print(f"{self.marca} {self._modelo} do ano {self.__ano}")

    def getMarca(self):
        return self.marca
    
    def setMarca(self, novaMarca):
        if novaMarca != "":
            self.marca = novaMarca
        else:
            print("Marca inválida!")

    def getModelo(self):
        upper = str.upper(self._modelo)
        return upper
    
    def setModelo(self, novoModelo):
        if novoModelo != "":
            self._modelo = novoModelo
        else:
            print("Modelo inválido!")

    def getAno(self):
        return self.__ano
    
    def setAno(self, novoAno):
        if novoAno > 2000 and novoAno <= 2027:
            self.__ano = novoAno
        else:
            print("Ano fora do intervalo permitido!")


carro_1 = Carro("BYD","Seal",2023)
carro_1.showInfo()
carro_1.setMarca("Lamborghini")
carro_1.setModelo("")   # Inválido
carro_1.setAno(1985)    # Inválido
carro_1.setModelo("Aventador")
carro_1.setAno(2025)

print(carro_1.getMarca())
print(carro_1.getModelo())
print(carro_1.getAno())


# Más práticas
# print(carro_1._modelo)        # Acessar private fraco - GET
# print(carro_1.__ano)          # Acessar private forte - GET - ERRO
# carro_1._modelo = "Opala"     # Modificar private fraco - SET
# carro_1.__ano = 1985          # Modificar private forte - SET - Bug de duplicadade
# print(carro_1._Carro__ano)    # Forçar o GET de private forte
# carro_1._Carro__ano = 1985    # Forçar o SET de private forte

    
