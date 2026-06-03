from veiculos.Veiculo import Veiculo
from veiculos.terrestre.Terrestre import Terrestre
from veiculos.terrestre.Carro import Carro
from veiculos.aereo.Aereo import Aereo
from veiculos.aereo.JatoGuerra import JatoGuerra
from veiculos.aquatico.Aquatico import Aquatico
from veiculos.aquatico.Jetski import Jetski

# Será transformada com abstrata
veiculo_1 = Veiculo("Patinete")
veiculo_1.acelerar(10)
veiculo_1.mostrarInfo()

# Será transformada com abstrata
terrestre = Terrestre("Trator",4)
terrestre.acelerar(5)
print(terrestre._nome)
terrestre.mostrarInfo()

carro = Carro("Opala",4,"Gasolina")
carro.acelerar(80)
carro.desacelerar(20)
carro.mostrarInfo()

jato = JatoGuerra("F-16",20)
jato.acelerar(2000)
jato.ganharAltitude(5000)
jato.mostrarInfo()

for i in range(10):
    jato.atirarMissel()
jato.mostrarInfo()

jetski_1 = Jetski("Yamaha FX", True,2)
jetski_1.embarcar(2)
jetski_1.acelerar(50)
jetski_1.mostrarInfo()
jetski_1.desacelerar(50)
jetski_1.desembarcar(2)
jetski_1.mostrarInfo()
