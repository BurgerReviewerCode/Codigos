import math
class buckets:
    lista:list
    dimension:int
    bucket:list
    # overflow:list
    # overdim:int

    # def __init__(self, dimension):
    #     self.dimension=dimension
    #     self.lista=[None]*((dimension*dimension)+dimension)
    #     self.overdim=((20/100)*dimension)
    #     self.overflow=[None]*((20/100)*dimension)
    #     self.iniciar()

    def __init__(self, dimension):
        self.dimension=(dimension)*(dimension*(20/100))
        self.lista=[None]*self.dimension
        bucket=[dimension]*dimension
    #     self.iniciar()

    # def iniciar(self):
    #     pos=math.sqrt(self.dimension)
    #     i=0
    #     for i in range(1, self.dimension, pos):
    #         self.lista[i]=pos-1

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
        elif tipo=="halfcube":
            indice=self.hash_halfcube(dato)
        elif tipo=="alfa":
            indice=self.hash_alfa(dato)
        if self.bucket[indice]!=0:
            enc=False
            i=0
            j=math.sqrt(self.dimension)
            while enc==False and i!=j:
                if self.lista[indice+i]==None:
                    enc=True
                    self.lista[indice+i]=dato
                    self.bucket[indice]-=1
                else:
                    i+=1
        else:
            indice+=1
            self.desbordado(dato, indice)

    def desbordado(self,dato,indice):
        if self.bucket[indice]!=0:
            enc=False
            i=0
            j=math.sqrt(self.dimension)
            while enc==False and i!=j:
                if self.lista[indice+i]==None:
                    enc=True
                    self.lista[indice+i]=dato
                    self.bucket[indice]-=1
                else:
                    i+=1
        else:
            indice+=1
            self.desbordado(dato, indice)

    def mostrar(self, valor, tipo):
        if tipo=="halfcube":
            indice=self.hash_halfcube(valor)
        elif tipo=="alfa":
            indice=self.hash_alfa(valor)
        i=0
        if self.lista[indice+i]==valor:
            print(self.lista[indice+i])
            print("Encontrado!")

if __name__=="__main__":
    listado=buckets(67)
    listado.insertar("E010-267","alfa")
    listado.mostrar("E010-267","alfa")
    listado.insertar(45212557,"halfcube")
    listado.mostrar(45212557,"halfcube")