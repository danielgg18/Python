# Autor: Daniel Garcia
# Fecha: 26 de mayo de 2022
# Archivo: CalculoCURP.py
# Programa que genera el CURP de una persona

#Definir variables 
#Convertimos las variables en mayusculas con comando .upper()
nombre = input("Escribe tu(s) nombre(s): ").upper()
apellido_paterno =input("Escribe tu apellido paterno: ").upper()
apellido_materno =input("Escribe tu apellido materno: ").upper()
dia_nacimiento =input("Escribe tu dia de nacimiento: -> dd: ")
mes_nacimiento =input("Escribe tu mes de nacimiento: -> mm: ")
año_nacimiento =input("Escribe tu año de nacimiento: -> aaaa: ")
sexo =input("Digita tu sexo(H/M): ").upper()

#En la CURP se coloca primero la primera letra del apellido paterno
aPaterno = apellido_paterno[0:1]

#Se coloca la primer vocal del  apellido paterno
#Para esto se debe eliminar las consonantes del apellido
consonantes = ["B","C","D","F","G","H","J","K","L","M","N","Ñ","P","Q","R","S","T","V","W","X","Y","Z"]
vocal_AP=""
for letra in apellido_paterno:
    if letra not in consonantes:
        vocal_AP=vocal_AP+letra
vAP = vocal_AP[0:1]

#Creamos nuestra funcion para iniciar a crear el CURP
#Sacamos los caracteres necesarios para el CURP
def generacion_curp(nombre,apellido_materno,apellido_paterno,dia_nacimiento,mes_nacimiento,año_nacimiento,sexo):
    nombre = nombre[0:1]
    apellido_materno = apellido_materno[0:1]
    año_nacimiento = año_nacimiento[2:4]
#Juntamos todos los caracteres
    curp = apellido_materno+nombre+año_nacimiento+mes_nacimiento+dia_nacimiento+sexo
#Retornamos el CURP a la funcion principal
    return curp
    
#Necesitamos la clave de los estados para continuar
#Se mostrara un listado
print ("A continuacion se mostrara un listado con los estados")
print (' 1 => Aguascalientes \n', 
	    '2 => Baja California \n',
		'3 => Baja California Sur \n',
		'4 => Campeche \n',
		'5 => Chiapas \n',
		'6 => Chihuahua \n',
		'7 => Ciudad de México \n',
		'8 => Coahuila de Zaragoza \n',
		'9 => Colima \n',
		'10 => Durango \n',
		'11 => Guanajuato \n',
		'12 => Guerrero \n',
		'13 => Hidalgo \n',
		'14 => Jalisco \n',
		'15 => México \n',
		'16 => Michoacán de Ocampo \n',
		'17 => Morelos \n',
		'18 => Nayarit \n',
		'19 => Nuevo León \n',
		'20 => Oaxaca \n',
		'21 => Puebla \n',
		'22 => Querétaro de Arteaga \n',
		'23 => Quintana Roo \n',
		'24 => San Luis Potosí \n',
		'25 => Sinaloa \n',
		'26 => Sonora \n',
		'27 => Tabasco \n',
		'28 => Tamaulipas \n',
		'29 => Tlaxcalteca \n',
		'30 => Veracruz-Llave \n',
		'31 => Yucatán \n',
		'32 => Zacatecas \n',
			)
			
estado = { '1':'AS', '2':'BC','3': 'BS', '4':'CC','5':'CS','6':'CH','7':'DF','8':'CL','9':'CM','10':'DG','11':'GT','12':'GR','13':'HG','14':'JC','15':'MC','16':'MN','17': 'MS', '18': 'NT','19':'NL','20':'OC','21':'PL','22':'QO','23':'QR','24':'SP','25':'SL','26':'SR','27':'TC','28':'TS','29':'TL','30':'VZ','31':'YN','32':'ZS'}
print("Selecciona el estado donde naciste")
claveEstado = input('Ingresa el numero del estado (1-32): ')
nombreEstado = estado[claveEstado]

lugarNacimiento=nombreEstado

#Imprimir la primer consonante del primer apellido
#No se cuentan las letras ya utilizadas anteriormente
recAp = apellido_paterno[1:12]
vocales = ["A","E","I","O","U"]
consonante_AP=""
for letra in recAp:
    if letra not in vocales:
        consonante_AP=consonante_AP+letra
cAP = consonante_AP[0:1]


#Imprimir la primer consonante de el segundo apellido
#No se cuentan las letras ya utilizadas anteriormente
recAm = apellido_materno[1:12]
vocales = ["A","E","I","O","U"]
consonante_AM=""
for letra in recAm:
    if letra not in vocales:
        consonante_AM=consonante_AM+letra
cAM = consonante_AM[0:1]


#Imprimir la primer consonante del primer nombre
#No se cuentan las letras ya utilizadas anteriormente
recNom = nombre[1:12]
vocales = ["A","E","I","O","U"]
consonante_Nom=""
for letra in recNom:
    if letra not in vocales:
        consonante_Nom=consonante_Nom+letra
cNom = consonante_Nom[0:1]

#Homoclave de 2 caracteres unicos para cada persona
#En este caso solo se respresentara con asteriscos
homoclave = "**"

#Por ultimo imprimimos nuestro CURP completo llamando a la funcion
print(f"\n Tu CURP es:{aPaterno+vAP+generacion_curp(nombre,apellido_materno,apellido_paterno,dia_nacimiento,mes_nacimiento,año_nacimiento,sexo)+lugarNacimiento+cAP+cAM+cNom+homoclave}")
