class Usuario:
    def __init__(self,fecha, usuario, cantidad):
        self.fecha=fecha
        self.usuario=usuario
        self.cantidad=cantidad
    
    def __str__(self):
        string=str(self.fecha)+" "+str(self.usuario)+" "+str(self.cantidad)
        return string
        
class Afectado:
    def __init__(self,fecha, afectado):
        self.fecha=fecha
        self.usuario=afectado
    
    def __str__(self):
        string=str(self.fecha)+" "+str(self.usuario)+" "+str(self.cantidad)
        return string

class Error:
    def __init__(self,fecha, error, cantidad):
        self.fecha=fecha
        self.usuario=error
        self.cantidad=cantidad
    
    def __str__(self):
        string=str(self.fecha)+" "+str(self.error)+" "+str(self.cantidad)
        return string