# Herança
class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def emitirSom(self):
        print("Animal disse:",self.nome)

    def mostrarInfo(self):
        print("Nome:",self.nome)
        print("Idade:",self.idade)


class Cachorro(Animal):
    def __init__(self, nome, idade, raca):
        super().__init__(nome, idade)
        self.raca = raca

    # Override do método da classe super
    def emitirSom(self):
        print("AU AU")

    # Override do método da classe super
    def mostrarInfo(self):
        super().mostrarInfo()  # Reaproveitamento do método da classe super
        print("Raça:",self.raca)

animal_1 = Animal("Ovelha", 5)
animal_1.emitirSom()
animal_1.mostrarInfo()

cachorro_1 = Cachorro("Totó",2,"Caramelo")
cachorro_1.emitirSom()
cachorro_1.mostrarInfo()

