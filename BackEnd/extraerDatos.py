import re
from clases import Usuario, Afectado, Error

class Analizar:
    def __init__(self):
       self.texto=""
       self.etiquetas=[]
       self.usuarios=[]
       self.fechas=[]
       self.afectados=[]
       self.errores=[]
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
        self.quitarEtiquetas()
        for i in self.etiquetas:
            fechas=re.findall(r"\d\d/\d\d/\d\d\d\d", i)
            fecha=fechas[0]
            self.insertarFecha(fecha)
            #print(fecha)
            #print(self.getUsuario(i))
            self.insertarUsuario(fecha,self.getUsuario(i))
            self.insertarAfectado(fecha,self.getAfectados(i))
            self.insertarError(fecha,self.getError(i))
    
    def insertarUsuario(self, fecha, usuario):
        if len(self.usuarios)==0:
            self.usuarios.append(Usuario(fecha,usuario,1))
        else:
            if self.verificarExisteUsuario(fecha,usuario):
                id=self.getPoscionUsuario(fecha,usuario)
                self.usuarios[id].cantidad+=1
            else:
                self.usuarios.append(Usuario(fecha,usuario,1))

    def insertarError(self, fecha, error):
        if len(self.usuarios)==0:
            self.errores.append(Error(fecha,error,1))
        else:
            if self.verificarExisteError(fecha,error):
                id=self.getPoscionError(fecha,error)
                self.errores[id].cantidad+=1
            else:
                self.errores.append(Error(fecha,error,1))

    def insertarAfectado(self, fecha, afectado):
        for i in afectado:
            if self.verificarExisteAfectado(fecha,i)==False:
                self.afectados.append(Afectado(fecha,i))
    
    def verificarExisteAfectado(self,fecha, afectado):
        encontrado=False
        for i in self.afectados:
            if i.afectado==afectado and i.fecha==fecha:
                encontrado=True
        return encontrado

    def verificarExisteError(self,fecha, error):
        encontrado=False
        for i in self.errores:
            if i.error==error and i.fecha==fecha:
                encontrado=True
        return encontrado
    
    def insertarFecha(self, fecha):
        if len(self.fechas)==0:
            self.fechas.append(fecha)
        else:
            if fecha in self.fechas:
                print()
            else:
                self.fechas.append(fecha)

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

    def getPoscionError(self, fecha, error):
        cont=0
        for i in self.errores:
            if i.error==error and i.fecha==fecha:
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
            if "Reportado por" in i:
                linea=i
                break
        usuarios=re.findall(r"[a-zA-Z0-9.!#$%&’*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*", linea)
        return usuarios[0]

    def getError(self,txt):
        usuarios=re.findall(r"\d\d\d\d\d", txt)
        return usuarios[0]

    def getAfectados(self,txt):
        linea=""
        lineas=txt.splitlines()
        for i in lineas:
            if "Usuarios afectados" in i:
                linea=i
                break
        usuarios=re.findall(r"[a-zA-Z0-9.!#$%&’*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*", linea)
        return usuarios

    def verFechas(self):
        for i in self.fechas:
            print(i)
    
    def verAfectados(self):
        for i in self.afectados:
            print(i)
    
    def verErrores(self):
        for i in self.errores:
            print(i)
    
    def generarEstadisticas(self):
        txt="<ESTADISTICAS>"
        for i in self.fechas:
            txt+="\n\t<ESTADISTICA>"
            txt+="\n\t\t<FECHA>"+i+"</FECHA>"
            txt+="\n\t\t<CANTIDAD_MENSAJES>"+str(self.obtenerMensajesFecha(i))+"</CANTIDAD_MENSAJES>"
            txt+="\n\t\t<REPORTADO_POR>"
            for j in self.usuarios:
                if j.fecha == i:
                    txt+="\n\t\t\t<USUARIO>"
                    txt+="\n\t\t\t\t<EMAIL>"+j.usuario+"</EMAIL>"
                    txt+="\n\t\t\t\t<CANTIDAD_MENSAJES>"+str(j.cantidad)+"</CANTIDAD_MENSAJES>"
                    txt+="\n\t\t\t</USUARIO>"
            txt+="\n\t\t</REPORTADO_POR>"

            txt+="\n\t\t<AFECTADOS>"
            for j in self.afectados:
                if j.fecha == i:
                    txt+="\n\t\t\t<AFECTADO>"+j.afectado+"</AFECTADO>"
            txt+="\n\t\t</AFECTADOS>"
            
            txt+="\n\t\t<ERRORES>"
            for j in self.errores:
                if j.fecha == i:
                    txt+="\n\t\t\t<ERROR>"
                    txt+="\n\t\t\t\t<CODIGO>"+j.error+"</CODIGO>"
                    txt+="\n\t\t\t\t<CANTIDAD_MENSAJES>"+str(j.cantidad)+"</CANTIDAD_MENSAJES>"
                    txt+="\n\t\t\t</ERROR>"
            txt+="\n\t\t</ERRORES>"

            txt+="\n\t</ESTADISTICA>"

        txt+="\n</ESTADISTICAS>"
        self.crearArchivo(txt)

    def obtenerMensajesFecha(self, fecha):
        cont=0
        for i in self.usuarios:
            if i.fecha==fecha:
                cont+=i.cantidad
        return cont

    def crearArchivo(self, texto):
        archivo=open("Database/Estadisticas.xml", 'w', encoding='utf8')
        archivo.write(texto)
        archivo.close()

prueba = Analizar()
# prueba.getDatos()
# prueba.verUsuarios();
# prueba.verFechas()
# prueba.verAfectados()
# prueba.verErrores()
# prueba.generarEstadisticas()