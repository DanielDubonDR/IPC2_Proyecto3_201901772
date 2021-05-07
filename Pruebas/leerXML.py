import re
txt='''
<EVENTOS>
	<EVENTO>
	Guatemala, 15/01/2021
	Reportado por: user1@ing.usac.edu.gt
	Usuarios afectados: user2@ing.usac.edu.gt, user3@ing.usac.edu.gt
	Error: 20001 - Desbordamiento de búfer de memoria RAM
	en el servidor de correo electrónico.
	</EVENTO>
	<EVENTO>
	Guatemala, 16/01/2021
	Reportado por: user4@ing.usac.edu.gt
	Usuarios afectados: user1@ing.usac.edu.gt, <"usuario3" user3@ing.usac.edu.gt>
	Error: 10001 - Excepción en pila
	</EVENTO>
	<EVENTO>
	Guatemala, 17/01/2021
	Reportado por: <coordinador@ing.usac.edu.gt>
	Usuarios afectados: user2@ing.usac.edu.gt, <user3@ing.usac.edu.gt>
	Error: 30001 - Servicio no encontrado
	</EVENTO>
	<EVENTO>
	Guatemala, 15/01/2021
	Reportado por: <user2@ing.usac.edu.gt>
	Usuarios afectados: coordinador@ing.usac.edu.gt, user1@ing.usac.edu.gt
	Error: 20001 - Desbordamiento de búfer de memoria RAM
	en el servidor de correo electrónico.
	</EVENTO>
	<EVENTO>
	Guatemala, 16/01/2021
	Reportado por: user1@ing.usac.edu.gt
	Usuarios afectados: user2@ing.usac.edu.gt, user4@ing.usac.edu.gt, <"coordinador" coordinador@ing.usac.edu.gt>
	Error: 30001 - Servicio no encontrado
	</EVENTO>
	<EVENTO>
	Guatemala, 16/01/2021
	Reportado por: user1@ing.edu.gt
	Usuarios afectados: user2@ing.usac.edu.gt, <user3@ing.usac.edu.gt>
	Error: 10001 - Excepción en pila
	</EVENTO>
</EVENTOS>
'''

#expresion correo= r"[a-zA-Z0-9.!#$%&’*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*"
# <EVENTO>(.|\n)*?</EVENTO>
a= re.findall(r"<EVENTO>(\n|.)*?</EVENTO>", txt)
print(a)

