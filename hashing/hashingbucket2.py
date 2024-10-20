class buckets:
    lista:list
    dimension:int
    bucket:list
    over:int
    i:int
    j:int

    def __init__(self, i, j):
        self.i=int(i+(i*(20/100)))
        self.j=j
        self.dimension=i*j
        self.over=i+1
        self.lista=[[0 for _ in range(self.j)] for _ in range(self.i)]
        self.bucket=[0 for _ in range(self.i)]
        print(self.dimension)

    def hash_division(self, valor):
        return valor%self.i
    
    def hash_extraccion(self, valor):
        valorx=int(valor) / 100
        valorx=int(valorx) % 1000
        valorx=int(valorx)
        return valorx%self.i

    def hash_plegado(self, valor):
        valorx=str(valor)
        longitud=len(valorx)
        acum=0
        i=0
        for i in range(0, longitud, 2):
            acum+=int(valorx[i]+valorx[i+1])
        return acum%self.i

    def hash_halfcube(self, valor):
        valorx=valor*valor
        valorx=int(valorx)/10000000
        valorx=int(valorx)%100
        return valorx%self.i
    
    def hash_alfa(self, valor):
        valorx="".join(str(ord(c)) for c in valor)
        valorfinal=int(valorx)%self.i
        return valorfinal

    def hasheo(self,dato,tipo,op):
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
        if op==1:
            self.insertar(dato,indice)
        if op==2:
            self.mostrar2(dato,indice)

    def insertar(self,dato,indice):
        if self.bucket[indice]!=self.j:
            j=self.bucket[indice]
            i=indice
            self.lista[i][j]=dato
            self.bucket[indice]+=1
        else:
            print("Bucket lleno, colision detectada")
            indice=self.over
            self.insertarlleno(dato,indice)
    
    def insertarlleno(self,dato,indice):
            if self.bucket[indice]==self.j:
                indice+=1
                self.insertarlleno(dato,indice)
            else:
                j=self.bucket[indice]
                i=indice
                self.lista[i][j]=dato
                self.bucket[indice]+=1

    def mostrar(self):
        for fila in self.lista:
            print(fila)
        for i in range(self.i):
            print(f"Bucket {i}: {self.bucket[i]}/{self.j}")

    def mostrar2(self,dato,indice):
        for j in range(0, self.bucket[indice]):
            if self.lista[indice][j]==dato:
                print("Econtrado")
                return
        if self.bucket[indice]!=self.j:
            print("No encontrado")
            return
        else:
            for i in range(self.over, self.i):
                if self.bucket[i]==0:
                    print("No encontrado")
                    return 
                for j in range(0, self.bucket[i]):
                    if self.lista[i][j]==dato:
                        print("Econtrado")
                        return

if __name__=="__main__":
    listado=buckets(20,10)
    listado.hasheo("E010-267","alfa",1)
    listado.hasheo("E010-267","alfa",2)
    listado.hasheo(45212557,"halfcube",1)
    listado.hasheo(45212557,"halfcube",2)
    listado.hasheo(47212557,"halfcube",2)
    listado.hasheo(45212557,"halfcube",1)
    listado.hasheo(45212557,"halfcube",1)
    listado.hasheo(45212557,"halfcube",1)
    listado.hasheo(45212557,"halfcube",1)
    listado.hasheo(45212557,"halfcube",1)
    listado.hasheo(45212557,"halfcube",1)
    listado.hasheo(45212557,"halfcube",1)
    listado.hasheo(45212557,"halfcube",1)
    listado.hasheo(45212557,"halfcube",1)
    listado.hasheo(45212557,"halfcube",1)
    listado.mostrar()