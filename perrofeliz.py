class Perrofeliz:
    def __init__(self, edad, nombre, color_ojos):
        self.edad = edad
        self.nombre = nombre
        self.color_ojos = color_ojos
    def comer(self):
        print("El perro come concentrado")
    def acariciar(self):
        print("El perro lo acarician todo el dia")
    def pasear(self):
        print("El perro pasea")
mi_perro=Perrofeliz(5,"Tito", "Negros")
mi_perro.comer()
mi_perro.acariciar()
mi_perro.pasear()

print("Mi perro es feliz")

