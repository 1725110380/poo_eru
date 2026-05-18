class Telefono:
    def __init__(self, marca, modelo, almacenamiento, ram, sistema_operativo, 
                 bateria, pantalla, camara_principal, color, precio):
     
        self.marca = marca
        self.modelo = modelo
        self.almacenamiento = almacenamiento
        self.ram = ram
        self.sistema_operativo = sistema_operativo
        self.bateria = bateria
        self.pantalla = pantalla
        self.camara_principal = camara_principal
        self.color = color
        self.precio = precio
        
        print(f"Marca del Teléfono: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Almacenamiento: {self.almacenamiento}")
        print(f"Memoria RAM: {self.ram}")
        print(f"Sistema Operativo: {self.sistema_operativo}")
        print(f"Capacidad de Batería: {self.bateria}")
        print(f"Tamaño de Pantalla: {self.pantalla}")
        print(f"Cámara Principal: {self.camara_principal}")
        print(f"Color del equipo: {self.color}")
        print(f"Precio aproximado: {self.precio}")

mi_telefono = Telefono(
    "Apple",
    "iPhone 15",
    "128 GB",
    "6 GB",
    "iOS 17",
    "3349 mAh",
    "6.1 pulgadas OLED",
    "48 MP",
    "Negro",
    "$19,499 MXN"
)
