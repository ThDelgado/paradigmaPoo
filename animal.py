class Animal: 
    def __init__(self, nombre:str, raza:str, edad:str, peso:str, especie:str) ->None: 
        self.nombre = nombre 
        self.raza = raza 
        self.edad =  edad 
        self.peso = peso 
        self.especie = especie
     
    def caminar(self):          
        return f"{self.nombre} esta caminando" 

    def comer(self): 
        return f"{self.nombre} esta comiendo"
  
    def dormir(self): 
        return f"{self.nombre} esta durmiendo" 


perro = Animal("Brando", "San Bernardo", "3 años","30 kg", "Perro") 
gato = Animal("Roll", "Persa", "4 años", "3 kg", "Gato") 

  

print(perro.comer())
print(gato.comer())
