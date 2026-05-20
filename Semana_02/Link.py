class Link:
    def __init__(self, barra_resistencia, rupias, arma_equipada, ropa_equipada, corazones_actuales, 
                 escudo_equipado, objetos, orbes, habilidad, posicion):
        
        self.barra_resistencia = barra_resistencia
        self.rupias = rupias
        self.arma_equipada = arma_equipada
        self.ropa_equipada = ropa_equipada
        self.corazones_actuales = corazones_actuales
        self.escudo_equipado = escudo_equipado
        self.objetos = objetos
        self.orbes = orbes
        self.habilidad = habilidad
        self.posicion = posicion
        
        print(f" Barra de resistencia : {self.barra_resistencia}")
        print(f" Rupias : {self.rupias}")
        print(f" Arma equipada : {self.arma_equipada}")
        print(f" Ropa equipada : {self.ropa_equipada}")
        print(f" Corazones actuales : {self.corazones_actuales}")
        print(f" Escudo equipado : {self.escudo_equipado}")
        print(f" Objetos : {self.objetos}")
        print(f" Orbes : {self.orbes}")
        print(f" Habilidad : {self.habilidad}")
        print(f" Posicion : {self.posicion}")

    def atacar(self):
        print("Link realiza un ataque con su arma.")

    def bloquear(self):
        print("Link bloquea el daño usando su escudo.")

    def dispararFlecha(self):
        print("Link tensa su arco y dispara una flecha.")

    def escalar(self):
        print("Link comienza a escalar consumiendo resistencia.")

    def esquivar(self):
        print("Link realiza una voltereta para esquivar.")


link_botw = Link(
    barra_resistencia="2 circulos",
    rupias="1540",
    arma_equipada="Espada Maestra",
    ropa_equipada="Tunica del Campeon",
    corazones_actuales="13",
    escudo_equipado="Escudo Hyliano",
    objetos="Manzanas asadas, Elixir vigorizante",
    orbes="4",
    habilidad="Modulo Magnetico",
    posicion="Meseta de los Albores"
)

link_botw.atacar()
link_botw.bloquear()
link_botw.dispararFlecha()
link_botw.escalar()
link_botw.esquivar()