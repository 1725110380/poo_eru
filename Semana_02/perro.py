class Perro:
    def __init__(self, nombre, raza, edad, color, peso, altura, vacunas, 
                 temperamento, estado_salud, num_hijos):
        
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.color = color
        self.peso = peso
        self.altura = altura
        self.vacunas = vacunas
        self.temperamento = temperamento
        self.estado_salud = estado_salud
        self.num_hijos = num_hijos
        
        print(f" Nombre : {self.nombre}")
        print(f" Raza : {self.raza}")
        print(f" Edad : {self.edad}")
        print(f" Color : {self.color}")
        print(f" Peso : {self.peso}")
        print(f" Altura : {self.altura}")
        print(f" Vacunas : {self.vacunas}")
        print(f" Temperamento : {self.temperamento}")
        print(f" Estado de salud : {self.estado_salud}")
        print(f" Numero de hijos : {self.num_hijos}")

    def comer(self):
        print("El perro esta comiendo su alimento.")

    def dormir(self):
        print("El perro esta durmiendo profundamente.")

    def jugar(self):
        print("El perro esta jugando con su pelota.")

    def correr(self):
        print("El perro esta corriendo por el parque.")

    def morder(self):
        print("El perro ha mordido su juguete.")


pastor_aleman = Perro(
    nombre="Max",
    raza="Pastor Aleman",
    edad="4 anos",
    color="Negro con fuego",
    peso="35 kg",
    altura="65 cm",
    vacunas="Completas",
    temperamento="Protector y leal",
    estado_salud="Excelente",
    num_hijos="0"
)

pastor_aleman.comer()
pastor_aleman.dormir()
pastor_aleman.jugar()
pastor_aleman.correr()
pastor_aleman.morder()