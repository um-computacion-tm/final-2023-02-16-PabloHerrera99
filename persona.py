class Persona:
    def __init__(self, id, apellido, nacimiento) -> None:
        self.id = id
        self.apellido = apellido
        self.nacimineto = nacimiento 
    
    def __repr__(self) -> str:
        return f'{self.apellido} / {self.nacimineto}, {self.id}'
         

if __name__ == '__main__':
    a = Persona(1, 'herrera', 1234)
    print(a.id)