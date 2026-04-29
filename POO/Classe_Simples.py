class Item:
    def __init__(self, name, value=0, rarity="Comum"):
        self.name = name
        self.value = value
        self.rarity = rarity

    def showInfo(self):
        print(f"Nome do item: {self.name}, Valor:{self.value}, Raridade: {self.rarity}")

item_1 = Item("Espada",200,"Comum")
item_1.showInfo()
#print(item_1.value)

item_2 = Item("Escudo",500,"Incomum")
item_2.showInfo()

item_3 = Item("Machado")
item_3.value = 650
item_3.rarity = "Raro"
item_3.showInfo()

item_1.value = 100
item_1.showInfo()

item_1.category = "Arma"
print(item_1.category)
