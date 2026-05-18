class Universidad:
    def __init__(self, logo, oferta_educativa, localidad, sistema_informatico, 
                 modalidad, servicios, ubicacion, talleres, cantidad_salones, 
                 rector):
        self.logo = logo
        self.oferta_educativa = oferta_educativa
        
        print(f"Logotipo de la Universidad: {self.logo}")
        print(f"Oferta educativa: {self.oferta_educativa}")

ipn = Universidad(
    "escudo_ipn.png", 
    "Ingeniería, Ciencias Médico-Biológicas, Sociales", 
    "CDMX", 
    "SAES", 
    "Presencial, Virtual y Mixta", 
    "Bibliotecas, Canal 11, Planetario", 
    "Unidad Zacatenco", 
    "Fútbol Americano, Robótica, Danza", 
    "Miles", 
    "Arturo Reyes Sandoval"
)