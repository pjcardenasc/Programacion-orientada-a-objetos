
class Estudiante:
    def __init__(self):
        self.nombre = input(("Cual es tu nombre?"))
        self.edad = input("Cual es tu edad?")
        self.numerotelefonico = input("Cual es tu numero telefonico?")
        self.carrera = input("Cual es tu carrera?")
    def mostrarInfo(self):
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)
        print("Carrera:", self.carrera)
        print("Numero telefonico:", self.numerotelefonico)
class Encuesta:
    def __init__(self, preguntas, respuestas):
        self.respuestas = respuestas
        self.preguntas = preguntas
    def ideaproyecto(self):
        self.respuesta1= input("¿Cual es tu idea de proyecto para POO?")
    def tiempo(self):
        self.respuesta2= input("Cuanto tiempo puedes dedicar al proyecto?")
    def limitaciones(self):
        self.respuesta3= input("¿Que limitaciones podrias tener en tu proyecto (actividades extracurriculares, trabajo, etc)?")
    def conocimiento(self):
        self.respuesta4= input("¿Que nivel de conocimiento del 1-10 consideras que tienes en python (ingrese solo un numero)?")            
    def experiencia(self):
        self.respuesta5= input("¿Que tan bien consideras que realizas trabajos en grupo?")
    def mostrarEncuesta(self):
        print("Idea proyecto:", self.respuesta1)
        print("Tiempo disponible:", self.respuesta2)
        print("Limitaciones:", self.respuesta3)
        print("Conocimiento en Python:", self.respuesta4)
        print("Experiencia en trabajos en grupo:", self.respuesta5)
def main():
    for i in range(1,11):
        preguntas ="a"
        respuestas="b"
        encuesta = Encuesta(preguntas, respuestas)
        estudiante = Estudiante()
        estudiante.mostrarInfo()
        encuesta.ideaproyecto()
        encuesta.tiempo()
        encuesta.limitaciones()
        encuesta.conocimiento()
        encuesta.experiencia()
        encuesta.mostrarEncuesta()
        print("------","Gracias por completar la encuesta", i,"------")
if __name__ == "__main__":
    main()