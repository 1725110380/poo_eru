class Silla:
    def __init__(self, forma, cantidad_patas, color, altura, anchura, material, 
                 tipo, peso_max, marca, movilidad):
        
        self.forma = forma
        self.cantidad_patas = cantidad_patas
        self.color = color
        self.altura = altura
        self.anchura = anchura
        self.material = material
        self.tipo = tipo
        self.peso_max = peso_max
        self.marca = marca
        self.movilidad = movilidad
        
        print(f" Forma : {self.forma}")
        print(f" Cantidad de patas : {self.cantidad_patas}")
        print(f" Color : {self.color}")
        print(f" Altura : {self.altura}")
        print(f" Anchura : {self.anchura}")
        print(f" Material : {self.material}")
        print(f" Tipo : {self.tipo}")
        print(f" Peso maximo : {self.peso_max}")
        print(f" Marca : {self.marca}")
        print(f" Movilidad : {self.movilidad}")

    def mover_silla(self):
        print("La silla se esta moviendo de lugar.")

    def limpiar_silla(self):
        print("La silla ha sido limpiada.")

    def girar_silla(self):
        print("La silla esta girando sobre su propio eje.")

    def soportar_peso(self):
        print("La silla esta soportando el peso del usuario de forma segura.")

    def plegar_silla(self):
        print("La silla ha sido plegada para transportarla facilmente.")


silla_ruedas = Silla(
    forma="Ergonomica",
    cantidad_patas="0 (Tiene 4 ruedas)",
    color="Negro con detalles cromados",
    altura="90 cm",
    anchura="65 cm",
    material="Aluminio ultraligero y tela de nylon",
    tipo="Silla de ruedas manual",
    peso_max="115 kg",
    marca="Drive Medical",
    movilidad="Alta (ruedas de traccion manual traseras)"
)

silla_ruedas.mover_silla()
silla_ruedas.limpiar_silla()
silla_ruedas.girar_silla()
silla_ruedas.soportar_peso()
silla_ruedas.plegar_silla()