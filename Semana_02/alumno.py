class Alumno:
    def __init__(self, matricula, nombre, correo, carrera, grado, promedio, 
                 asistencia, grupo, horario, estatus_academico):
        
        self.matricula = matricula
        self.nombre = nombre
        self.correo = correo
        self.carrera = carrera
        self.grado = grado
        self.promedio = promedio
        self.asistencia = asistencia
        self.grupo = grupo
        self.horario = horario
        self.estatus_academico = estatus_academico
        
        print(f" Matricula : {self.matricula}")
        print(f" Nombre : {self.nombre}")
        print(f" Correo : {self.correo}")
        print(f" Carrera : {self.carrera}")
        print(f" Grado : {self.grado}")
        print(f" Promedio : {self.promedio}")
        print(f" Asistencia : {self.asistencia}")
        print(f" Grupo : {self.grupo}")
        print(f" Horario : {self.horario}")
        print(f" Estatus academico : {self.estatus_academico}")

    def IncribirMateria(self):
        print("El alumno ha inscrito una nueva materia.")

    def DarDeBajaMateria(self):
        print("El alumno ha dado de baja una materia.")

    def EntregarTarea(self):
        print("El alumno ha entregado su tarea en la plataforma.")

    def PresentarExamen(self):
        print("El alumno esta presentando su examen.")

    def VerHorario(self):
        print("El alumno esta consultando su horario de clases.")


alumno_utt = Alumno(
    matricula="25UTT0894",
    nombre="Emmanuel Rivera Uribe",
    correo="emmanuel.ru@alumnos.utt.edu.mx",
    carrera="Tecnologias de la Informacion e Innovacion Digital",
    grado="Tercer Cuatrimestre",
    promedio="9.2",
    asistencia="95%",
    grupo="TIC-32",
    horario="Matutino",
    estatus_academico="Regular"
)

alumno_utt.IncribirMateria()
alumno_utt.DarDeBajaMateria()
alumno_utt.EntregarTarea()
alumno_utt.PresentarExamen()
alumno_utt.VerHorario()