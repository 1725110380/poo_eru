class Transporte:
    def __init__(self, tipo_transporte, modelo, peso_maximo, tipo_combustible, 
                 kilometraje, matricula, num_puertas, num_llantas, velocidad_max, color):
        
        self.tipo_transporte = tipo_transporte
        self.modelo = modelo
        self.peso_maximo = peso_maximo
        self.tipo_combustible = tipo_combustible
        self.kilometraje = kilometraje
        self.matricula = matricula
        self.num_puertas = num_puertas
        self.num_llantas = num_llantas
        self.velocidad_max = velocidad_max
        self.color = color
        
        print(f" Tipo de transporte : {self.tipo_transporte}")
        print(f" Modelo : {self.modelo}")
        print(f" Peso máximo : {self.peso_maximo}")
        print(f" Tipo de combustible : {self.tipo_combustible}")
        print(f" Kilometraje : {self.kilometraje}")
        print(f" Matrícula : {self.matricula}")
        print(f" Número de puertas : {self.num_puertas}")
        print(f" Número de llantas : {self.num_llantas}")
        print(f" Velocidad máxima : {self.velocidad_max}")
        print(f" Color : {self.color}")

    def acelerar(self):
        print("El transporte está acelerando...")

    def frenar(self):
        print("El transporte ha aplicado los frenos.")

    def cargar(self):
        print("Subiendo pasajeros al transporte.")

    def descargar(self):
        print("Bajando pasajeros del transporte.")

    def recargar_combustible(self):
        print("Recargando combustible en la estación.")


autobus = Transporte(
    tipo_transporte="Autobus urbano",
    modelo="Mercedes-Benz Marcopolo",
    peso_maximo="16,000 kg",
    tipo_combustible="Diesel",
    kilometraje="145,000 km",
    matricula="874-JZ-2",
    num_puertas="2",
    num_llantas="6",
    velocidad_max="110 km/h",
    color="Blanco con franjas verdes"
)

autobus.acelerar()
autobus.frenar()
autobus.cargar()
autobus.descargar()
autobus.recargar_combustible()