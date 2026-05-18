# --- CLASE PADRE ---
class Transporte:
    def __init__(self, medio, capacidad):
        self.medio = medio
        self.capacidad = capacidad
        print(f"Vehículo listo para operar en medio: {self.medio}")

    def moverse(self):
        print("El transporte inició su marcha...")

# --- CLASE HIJA (HERENCIA) ---
class Coche(Transporte):
    def __init__(self, medio, capacidad, marca, modelo):
        # Aquí se heredan los atributos del padre
        super().__init__(medio, capacidad)
        self.marca = marca
        self.modelo = modelo
        print(f"Instancia de Coche: {self.marca} {self.modelo} creada con éxito.")

    def sonar_claxon(self):
        print("¡Sonando claxon: Beep Beep!")

# --- PRUEBA DEL CÓDIGO ---
mi_auto = Coche("Terrestre", 5, "Honda", "Civic")
mi_auto.moverse()        # Llama al método heredado
mi_auto.sonar_claxon()   # Llama al método propio