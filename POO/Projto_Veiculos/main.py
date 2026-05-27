from veiculos.Veiculo import Veiculo
from veiculos.terrestre.Terrestre import Terrestre
from veiculos.terrestre.Carro import Carro

veiculo_1 = Veiculo("Patinete")
veiculo_1.acelerar(10)
veiculo_1.mostrarInfo()

terrestre = Terrestre("Trator",4)
terrestre.acelerar(5)
print(terrestre._nome)
terrestre.mostrarInfo()

carro = Carro("Opala",4,"Gasolina")
carro.acelerar(80)
carro.desacelerar(20)
carro.mostrarInfo()
