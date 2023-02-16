from base import Base
from persona import Persona
from fecha import Fecha

class Service:

    def __init__(self) -> None:
        self.base = {}

    def add(self, persona, base = None):
        base.data[persona.id] = persona

    def order_by_fecha(self, list):
        lista = []
        for persona in list.data.values():
            lista.append(persona)
        count = len(lista)
        for i in range(len(lista) - 1):
            for j in range(i + 1, len(lista)):
                if lista[i].nacimiento.compare_to(lista[j].nacimiento) > 0:
                    lista[i], lista[j] = lista[j], lista[i]
            
    
    def order_by_apellido(self,list):
        a =  []
        b = []
        for value in list.data.values():
            a.append(str(value))
        a.sort()    

        return a
    
        
if __name__ == '__main__':
    base = Base()
    print(base)
    fecha = Fecha(1999, 1, 16)
    fecha2 = Fecha(1998, 1, 16)
    persona1 = Persona(5, 'perez', fecha)

    p2 = Persona(3, 'aaa', fecha2)
    ser = Service()
    ser.add(persona1, base)
    ser.add(p2, base)
    print(base.data)
    b = ser.order_by_apellido(base)
    c = ser.order_by_apellido(base)
    print(b)
    print(c)
