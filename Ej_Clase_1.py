print("Introduccion a clases")
class Animal:
    edad=3
    raza="pastor aleman"
    comida="croquetas"
    def come(self):
        print(f"El perro come "+self.comida)

print(Animal)
print("Creando objetos de la clase Animal")
perra=Animal()
print(f"La edad del perro es: {perra.edad}")
print(f"La raza del perro es: {perra.raza}")
perra.come()
