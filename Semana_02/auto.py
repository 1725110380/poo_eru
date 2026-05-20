class Auto:
    def __init__(self, placa, color, marca, modelo, tipo_transmision, 
                 kilometraje, num_puertas, tipo_carroceria, nivel_aceite, num_asientos):
        
        self.placa = placa
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.tipo_transmision = tipo_transmision
        self.kilometraje = kilometraje
        self.num_puertas = num_puertas
        self.tipo_carroceria = tipo_carroceria
        self.nivel_aceite = nivel_aceite
        self.num_asientos = num_asientos
        
        print(f" Placa : {self.placa}")
        print(f" Color : {self.color}")
        print(f" Marca : {self.marca}")
        print(f" Modelo : {self.modelo}")
        print(f" Tipo de transmision : {self.tipo_transmision}")
        print(f" Kilometraje : {self.kilometraje}")
        print(f" Numero de puertas : {self.num_puertas}")
        print(f" Tipo de carroceria : {self.tipo_carroceria}")
        print(f" Nivel de aceite : {self.nivel_aceite}")
        print(f" Numero de asientos : {self.num_asientos}")

    def encender(self):
        print("El auto se ha encendido.")

    def acelerar(self):
        print("El auto esta acelerando...")

    def frenar(self):
        print("El auto ha frenado.")

    def tocar_claxon(self):
        print("Suena el claxon.")

    def apagar(self):
        print("El auto se ha apagado.")


supra = Auto(
    placa="HGO-789-A",
    color="Blanco",
    marca="Toyota",
    modelo="Supra",
    tipo_transmision="Manual de 6 velocidades",
    kilometraje="85,000 km",
    num_puertas="2",
    tipo_carroceria="Coupe",
    nivel_aceite="Optimo",
    num_asientos="2"
)

supra.encender()
supra.acelerar()
supra.frenar()
supra.tocar_claxon()
supra.apagar()
