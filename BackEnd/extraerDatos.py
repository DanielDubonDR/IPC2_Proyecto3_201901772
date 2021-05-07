class Analizar:
    def __init__(self):
       self.texto=""
       self.etiquetas=[]
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

prueba = Analizar()
prueba.verEtiquetas()