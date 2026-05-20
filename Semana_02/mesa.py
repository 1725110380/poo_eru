class Mesa:
    def __init__(self, forma, cantidad_patas, color, altura, anchura, largo, 
                 material, tipo, peso_max, marca):
        
        self.forma = forma
        self.cantidad_patas = cantidad_patas
        self.color = color
        self.altura = altura
        self.anchura = anchura
        self.largo = largo
        self.material = material
        self.tipo = tipo
        self.peso_max = peso_max
        self.marca = marca
        
        print(f" Forma : {self.forma}")
        print(f" Cantidad de patas : {self.cantidad_patas}")
        print(f" Color : {self.color}")
        print(f" Altura : {self.altura}")
        print(f" Anchura : {self.anchura}")
        print(f" Largo : {self.largo}")
        print(f" Material : {self.material}")
        print(f" Tipo : {self.tipo}")
        print(f" Peso maximo : {self.peso_max}")
        print(f" Marca : {self.marca}")

    def sostener_objetos(self):
        print("La mesa esta sosteniendo los objetos sobre su superficie.")

    def armar_mesa(self):
        print("La mesa ha sido armada correctamente.")

    def mover_mesa(self):
        print("La mesa se ha movido de lugar.")

    def limpiar_mesa(self):
        print("La superficie de la mesa ha sido limpiada.")

    def desplegar_mesa(self):
        print("La mesa se ha desplegado para tener mas espacio.")


mesa_comedor = Mesa(
    forma="Rectangular",
    cantidad_patas="4",
    color="Cafe",
    altura="75 cm",
    anchura="100 cm",
    largo="200 cm",
    material="Madera de roble",
    tipo="Comedor familiar",
    peso_max="150 kg",
    marca="Ashley Furniture"
)

mesa_comedor.sostener_objetos()
mesa_comedor.armar_mesa()
mesa_comedor.mover_mesa()
mesa_comedor.limpiar_mesa()
mesa_comedor.desplegar_mesa()