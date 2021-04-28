import re
txt='''
<EVENTOS>
    <EVENTO>
        Guatemala, 15/01/2021
        Reportado por: <”Nombre Empleado 1” xx@ing.usac.edu.gt>
        Usuarios afectados: aa@ing.usac.edu.gt, <bb@ing.usac.edu.gt>
        Error: 20001 - Desbordamiento de búfer de memoria RAM en el servidor de correo electrónico.
    </EVENTO>
     <EVETO>
        Guatemala, 15/01/2021
        Reportado por: <
        Usuarios afectados: aa@ing.usac.edu.gt, <bb@ing.usac.edu.gt>
        Error: 20001 - Desbordamiento de búfer de memoria RAM en el servidor de correo electrónico.
    </EVENTO>
     <EVENTO>
        Guatemala, 15/01/2021
        Reportado por: <”Nombre Empleado 1” xx@ing.usac.edu.gt>
        Usuarios afectados: a>
        Error: 20001 - Desbordamiento de búfer de memoria RAM en el servidor de correo electrónico.
    </EVENTO
    <EVENTO>HLASDFSADFASDFA</EVENTO>
</EVENTOS
'''
f=txt.replace("\n","|||\n")
f=txt.splitlines()

j=""
for i in f:
    j+=str(i)
a= re.findall(r'<EVENTO>(.*)</EVENTO>', txt)
for i in a:
    print(i)

