class Universidad:
    def __init__(self, logo, oferta_educativa, localidad, sistema_informatico, 
                 modalidad, servicios, ubicacion, talleres, cantidad_salones, 
                 rector):
        
        
        self.logo = logo
        self.oferta_educativa = oferta_educativa
        self.localidad = localidad
        self.sistema_informatico = sistema_informatico
        self.modalidad = modalidad
        self.servicios = servicios
        self.ubicacion = ubicacion
        self.talleres = talleres 
        self.cantidad_salones = cantidad_salones
        self.rector = rector




        print(f"Logotipo de la Universidad: {self.logo}")
        print(f"Oferta educativa: {self.oferta_educativa}")
        print(f"Se ubica en :{self.localidad}")
        print(f"Su sistema es:{self.sistema_informatico}")
        print(f"Su modalidad es:{self.modalidad}")
        print(f"sus servicios son:{self.servicios}")
        print(f"esta ubicada en :{self.ubicacion}")
        print(f"cuenta con estos talleres:{self.talleres}")
        print(f"tiene esta cantidad de salones:{self.cantidad_salones}")
        print(f"el rector es:{self.rector}")
    

    def MatricularAlumnos ():
        print(f"La matricula del alumno es")
    def EvaluarRendimiento ():
        print(f"El nivel de rendimiento es")
    def ContratarProfesores (): 
        print(f"Abre convocatoria para profesores")
    def EventoUniversitario ():
        print(f"Organiza evento para los alumnos")
    def AsignarHorario():
        print ("Asigna horario a alumno y docente")

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

ipn.MatricularAlumnos()
ipn.EvaluarRendimiento()
ipn.ContratarProfesores()
ipn.EventoUniversitario()
ipn.AsignarHorario()