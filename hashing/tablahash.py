import random
class TablaHash:
    dimension=int
    tabla=[]

    def __init__(self,dimension=67):
        self.dimension=dimension
        self.items=[None]*dimension

    def funhash(self, llave):
        return llave % self.dimension
    
    def insertar(self, dato):
        if self.items[self.funhash(dato)] is None:
            self.items[self.funhash(dato)]=dato
        else:
            i=0
            while self.items[(self.funhash(dato)+1)%self.dimension]!=None and i<self.dimension:
                i+=1
            if i>self.dimension:
                print("Tabla llena")
            else:
                self.items[(self.funhash(dato)+1)%self.dimension]=dato

    def buscar(self, dato):
        if self.items[self.funhash(dato)]==dato:
            return True
        else:
            i=0
            while self.items[(self.funhash(dato)+1)%self.dimension]!=dato and self.items[(self.funhash(dato)+1)%self.dimension]!=None and i<self.dimension:
                i+=1
            if self.items[(self.funhash(dato)+1)%self.dimension]==dato:
                return True
            else:
                return False  

if __name__=="__main__":

    tabla=TablaHash()
    valores=[]
    for _ in range(30):
        clave=random.randint(0,27)
        tabla.insertar(clave)
        valores.append(clave)
    i=0
    for i in range(30):
        if tabla.buscar(valores[i])==True:
            print("El valor",valores[i],"se encuentra en la tabla")
        else:
            print("El valor",valores[i],"no se encuentra en la tabla")
    
    # tabla=TablaHash()
    # for _ in range(1000):
    #     clave=random.randint(0,100000)
    #     tabla.insertar(clave, f"valor_{clave}")
    # clave=20
    # tabla.insertar(clave, f"valor_{clave}")

    # clave_buscar=random.randint(0,100000)
    # print(f"Valor para la clave {clave_buscar}: {tabla.buscar(clave_buscar)}")
    # clave_buscar=20
    # print(f"Valor para la clave {clave_buscar}: {tabla.buscar(clave_buscar)}")

    # def insertar(self,llave,valor):
    #     indice=self.funhash(llave)
    #     indiceog=indice
    #     while self.tabla[indice]!=None:
    #         indice=(indice+1)%self.dimension
    #         if indice==indiceog:
    #             print("Tabla llena")
    #             return
    #     self.tabla[indice]=(llave,valor)

    # def buscar(self,llave):
    #     indice=self.funhash(llave)
    #     indiceog=indice
    #     while self.tabla[indice] is not None:
    #         if self.tabla[indice][0]==llave:
    #             return self.tabla[indice][1]
    #         indice=(indice+1) % self.dimension
    #         if indice==indiceog:
    #             break
    #     return None