import datetime


cliente1 = {'nombre': 'pepe',
            'apellido' : 'honguito'}
cliente2 = {"nombre": 'pepa',
            "apellido" : 'fernandez'}
class Fecha:
    def __init__(self, anho:int = 2023, mes:int=5, dia:int = 2 )-> None:
        self.anho= anho 
        self.mes= mes 
        self.dia= dia 
    def __repr__(self) -> str:
            return f"{self.dia} / {self.mes} / {self.anho}"
    def to_datetime(self):
        return datetime.datetime(self.anho, self.mes, self.dia)

class Persona:
    def __init__(self, nombre:str= None, apellido:str= None, nacimiento:Fecha= None,diccionario:dict= None):
        
        if not diccionario is None:
            self.apellido = diccionario.get('apellido')
            self.nombre = diccionario.get('nombre')
            

        if not nombre is None:
            self.nombre = nombre

        if not apellido is None:
            self.apellido = apellido

        
        self.nacimiento = nacimiento.to_datetime()

    def __repr__(self) -> str:
            return f" Persona [nombre] = {self.nombre} [apellido] = {self.apellido} nacimiento = {self.nacimiento.strftime('%d/%m/%Y')}" 


class Ordenador:
    
    def porNacimiento(self, personas):
        return sorted(personas, key=lambda persona: persona.nacimiento)
    
    

if __name__ == '__main__':
    persona_1 = Persona(diccionario = cliente1)
    persona_2 = Persona(nombre = 'pepa', apellido ='pig', nacimiento=Fecha(dia=31, mes=12,anho= 1999))
    p1 = persona_1
    p2 = persona_2

    print(p1)
    print(p2)

