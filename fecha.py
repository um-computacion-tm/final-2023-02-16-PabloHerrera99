import datetime

class Fecha:
    def __init__(self, año=2023, mes=2, dia=16) -> None:
        self.año = año
        self.mes = mes
        self.dia = dia
    
    def __str__(self) -> str:
        return f'{self.año}-{self.mes}-{self.dia}'
    
    def compare_to(self,fecha2):
        fecha_1 = datetime.date(self.año,self.mes,self.dia)
        fecha_2 = datetime.date(fecha2.año, fecha2.mes, fecha2.dia)
        if fecha_1 < fecha_2:
            return -1
        elif fecha_1 == fecha_2:
            return 0 
        elif fecha_1 > fecha_2:
            return 1

if __name__ == '__main__':
    f1 = Fecha(2000,1,16)
    f2 = Fecha(1999, 1, 16)
    print(f1.compare_to(f2))