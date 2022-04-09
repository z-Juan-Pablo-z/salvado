# Una Clase Es un molde
#DECLARAR UNA CLASE (PONER ATRIBUTOS Y METODOS)
class Heroe:
    #CONSTRUCTOR DE LA CLASE
    #constructor=funcion especial
    #constructor=fuuncion que permite inicializar los atributos
    def __init__(self,name,height,life,heroe,can):
        #atributos=propiedades=datos
        #VARIABLES DEL LENGUAJE QUE YO ELIJA 
        #"Self" significa que es propio de el, referencia al "this"
        self.poder=can
        self.nombre=name
        self.estatura=height
        self.tipoHeroe=heroe
        self.cantidadVida=life 
        
    #metodos=acciones = ¿Que hace mi molde?
    #FUNCIONES DEL LENGUAJE QUE YO ELIJA 
    def saludar(self):
        print("Holaaaaaaaaaaaaaaaaaaaa")
#UTILIZANDO LA CLASE=CREAR UNA INSTANCIA
#SACAR FOTOCOPIA=CREAR UN OBJETO
#OBJETO SIN IMPORTAR EL LENGUAJE ES UNA VARIABLE ESPECIAL
goku=Heroe('goku',1.70,100,'SSJ',1200)
#con el objeto accedo a un atributo(Variable)
print(goku.nombre)
#Con el objeto accedo a un metodo(Funcion)
goku.saludar()
