import re
from clases import Usuario, Afectado, Error

class Analizar:
    def __init__(self):
       self.texto=""
       self.etiquetas=[]
       self.usuarios=[]
       self.leerArchivo()

    def leerArchivo(self):
        archivo=open("Database/Archivo.xml",'r', encoding='utf8')
        for linea in archivo:
           self.texto+=linea
        archivo.close() 
        self.texto+="\n"
        self.analizar()

    def verEtiquetas(self):
        for i in self.etiquetas:
            print(i)
            print("\n")
    
    def analizar(self):
        estado=0
        posicion=0
        string=""
        longitud=len(self.texto)
        while posicion<longitud:
            caracter=self.texto[posicion]
            # print(string)
            if estado==0:
                if caracter=="<":
                    estado=1
                    string+=caracter
                    posicion+=1

                elif caracter==" ":
                    posicion+=1

                elif caracter=="\n":
                    posicion+=1
                
                else:
                    posicion+=1

            elif estado==1:
                if caracter=="E":
                    estado=2
                    string+=caracter
                    posicion+=1
                else:
                    estado=0
                    string=""
                    
            
            elif estado==2:
                if caracter=="V":
                    estado=3
                    string+=caracter
                    posicion+=1
                else:
                    estado=0
                    string=""
                    
            
            elif estado==3:
                if caracter=="E":
                    estado=4
                    string+=caracter
                    posicion+=1
                else:
                    estado=0
                    string=""
                    

            elif estado==4:
                if caracter=="N":
                    estado=5
                    string+=caracter
                    posicion+=1
                else:
                    estado=0
                    string=""
                    

            elif estado==5:
                if caracter=="T":
                    estado=6
                    string+=caracter
                    posicion+=1
                else:
                    estado=0
                    string=""
                    
            
            elif estado==6:
                if caracter=="O":
                    estado=7
                    string+=caracter
                    posicion+=1
                else:
                    estado=0
                    string=""
                    

            elif estado==7:
                if caracter==">":
                    estado=8
                    string+=caracter
                    posicion+=1
                else:
                    estado=0
                    string=""
                    

            elif estado==8:
                if caracter=="<":
                    estado=9
                    string+=caracter
                    posicion+=1
                else:
                    string+=caracter
                    posicion+=1

            elif estado==9:
                if caracter=="/":
                    estado=10
                    string+=caracter
                    posicion+=1
                else:
                    estado=8
                    string+=caracter
                    posicion+=1
            
            elif estado==10:
                if caracter=="E":
                    estado=11
                    string+=caracter
                    posicion+=1
                else:
                    estado=0
                    string=""
                    
            elif estado==11:
                if caracter=="V":
                    estado=12
                    string+=caracter
                    posicion+=1
                else:
                    estado=0
                    string=""

            elif estado==12:
                if caracter=="E":
                    estado=13
                    string+=caracter
                    posicion+=1
                else:
                    estado=0
                    string=""

            elif estado==13:
                if caracter=="N":
                    estado=14
                    string+=caracter
                    posicion+=1
                else:
                    estado=0
                    string=""

            elif estado==14:
                if caracter=="T":
                    estado=15
                    string+=caracter
                    posicion+=1
                else:
                    estado=0
                    string=""
            
            elif estado==15:
                if caracter=="O":
                    estado=16
                    string+=caracter
                    posicion+=1
                else:
                    estado=0
                    string=""
            
            elif estado==16:
                if caracter==">":
                    estado=17
                    string+=caracter
                    posicion+=1
                else:
                    estado=0
                    string=""
            
            elif estado==17:
                    self.etiquetas.append(string)
                    estado=0
                    string=""
    
    def quitarEtiquetas(self):
        for i in range(len(self.etiquetas)):
            self.etiquetas[i]=self.etiquetas[i].replace("<EVENTO>", "")
            self.etiquetas[i]=self.etiquetas[i].replace("</EVENTO>", "")
            self.etiquetas[i]=self.etiquetas[i].lstrip().rstrip()
    
    def getDatos(self):
        for i in self.etiquetas:
            fechas=re.findall(r"\d\d/\d\d/\d\d\d\d", i)
            fecha=fechas[0]
            print(fecha)
            print(self.getUsuario(i))
            self.insertarUsuario(fecha,self.getUsuario(i))
    
    def insertarUsuario(self, fecha, usuario):
        if len(self.usuarios)==0:
            self.usuarios.append(Usuario(fecha,usuario,1))
        else:
            if self.verificarExisteUsuario(fecha,usuario):
                print("hola ")
                id=self.getPoscionUsuario(fecha,usuario)
                self.usuarios[id].cantidad+=1
            else:
                print("holass ")
                self.usuarios.append(Usuario(fecha,usuario,1))

    def verificarExisteUsuario(self,fecha, usuario):
        encontrado=False
        for i in self.usuarios:
            if i.usuario==usuario and i.fecha==fecha:
                encontrado=True
        return encontrado
    
    def getPoscionUsuario(self, fecha, usuario):
        cont=0
        for i in self.usuarios:
            if i.usuario==usuario and i.fecha==fecha:
                return cont
            else:
                cont+=1
    
    def verUsuarios(self):
        for i in self.usuarios:
            print(i)
    
    def getUsuario(self,txt):
        linea=""
        lineas=txt.splitlines()
        for i in lineas:
            if "Reportado por:" in i:
                linea=i
                break
        usuarios=re.findall(r"[a-zA-Z0-9.!#$%&’*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*", linea)
        return usuarios[0]
        

prueba = Analizar()
prueba.quitarEtiquetas()
prueba.getDatos()
prueba.verUsuarios();