import random

class TablaHash:
    dimension=int
    items=list

    def __init__(self,dimension=67):
        self.dimension=dimension
        self.items=[None]*dimension
    
    def hash_division(self, valor):
        return valor%self.dimension
    
    def hash_extraccion(self, valor):
        valorx=int(valor) / 100
        valorx=int(valorx) % 1000
        valorx=int(valorx)
        return valorx%self.dimension

    def hash_plegado(self, valor):
        valorx=str(valor)
        longitud=len(valorx)
        acum=0
        i=0
        for i in range(0, longitud, 2):
            acum+=int(valorx[i]+valorx[i+1])
        return acum%self.dimension

    def hash_halfcube(self, valor):
        valorx=valor*valor
        valorx=int(valorx)/10000000
        valorx=int(valorx)%100
        return valorx%self.dimension
    
    def hash_alfa(self, valor):
        valorx="".join(str(ord(c)) for c in valor)
        valorfinal=int(valorx)%self.dimension
        return valorfinal      

    def insertar(self, dato, tipo):
        if tipo=="plegado":
            indice=self.hash_plegado(dato)
        elif tipo=="division":
            indice=self.hash_division(dato)
        elif tipo=="extraccion":
            indice=self.hash_extraccion(dato)
        if self.items[indice] is None:
            self.items[indice]=dato
            print("Colisiones detectadas: 0")
        else:
            i=0
            while self.items[(indice+1)%self.dimension]!=None and i<self.dimension:
                i+=1
            if i>self.dimension:
                print("Tabla llena")
            else:
                self.items[(indice+1)%self.dimension]=dato
                print("Colisiones detectadas:",i)