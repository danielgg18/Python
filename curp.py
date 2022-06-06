#Nombre del programa: calcCurp.py
#Autor: Daniel Garcia
#Fecha: 05/06/22
#Descripcion del programa: Programa que calcula el CURP con los datos de una persona

#biblioteca que contiene la función para limpiar el contenido de la pantalla
import os

def curp():
    
    #Nombre completo de la persona
    nombre=input("Escriba su nombre: ").upper()
    aPaterno=input("Escriba su apellido paterno: ").upper()
    aMaterno=input("Escriba su apellido materno: ").upper()

    #Lista con las consonantes
    consonantes = [
        "B","C","D","F","G",
        "H","J","K","L","M",
        "N","Ñ","P","Q","R",
        "S","T","V","W","X","Y","Z"]
    
    #Selecciona la primer vocal del apellido paterno
    vocalApaterno=""
    for letra in aPaterno:
        if letra not in consonantes:
            vocalApaterno=vocalApaterno+letra
    vocalAP = vocalApaterno[0:1]

    #Fecha de nacimiento de la persona
    dia=input("Dia de nacimiento: ")
    mes=input("Mes de nacimiento: ")
    anio=input("Año de nacimiento: ")
        
        
    genero=input("¿Cuál es su género?(H:hombre M:mujer) ").upper()
    
    #Limpiar el contenido de la pantalla (solo funciona en linux)
    os.system ("clear")

    #Diccionario con las abreviaturas de las entidades federativas
    entidades = { 
        '1':'AS', '2':'BC','3': 'BS', '4':'CC','5':'CS',
        '6':'CH','7':'DF','8':'CL','9':'CM','10':'DG',
        '11':'GT','12':'GR','13':'HG','14':'JC','15':'MC',
        '16':'MN','17': 'MS', '18': 'NT','19':'NL','20':'OC',
        '21':'PL','22':'QO','23':'QR','24':'SP','25':'SL',
        '26':'SR','27':'TC','28':'TS','29':'TL','30':'VZ',
        '31':'YN','32':'ZS'}
    
    print("\t***Estados de la República Mexicana***")
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
			
    claveEstado = input('Ingresa el numero del estado en que naciste (1-32): ')
    nombreEstado = entidades[claveEstado]

    #Lista con las vocales
    vocales = ["A","E","I","O","U"]
    
    #Selecciona la primer consonante del apellido paterno
    recAp = aPaterno[1:12]
    consonanteApaterno=""
    for letra in recAp:
        if letra not in vocales:
            consonanteApaterno=consonanteApaterno+letra
    consonanteAP = consonanteApaterno[0:1]


    #Selecciona la primer consonante del apellido materno
    recAm = aMaterno[1:12]
    consonanteAmaterno=""
    for letra in recAm:
        if letra not in vocales:
            consonanteAmaterno=consonanteAmaterno+letra
    consonanteAM = consonanteAmaterno[0:1]


    #Selecciona la primer consonante del nombre
    recNom = nombre[1:12]
    consonanteNom=""
    for letra in recNom:
        if letra not in vocales:
            consonanteNom=consonanteNom+letra
    consonanteN = consonanteNom[0:1]

    #Diferenciador Homoclave
    diferenciadorH=str(0)
    #Digito verificador
    digitoV=str(9)

    print("Su CURP es: ", aPaterno[0]+vocalAP+aMaterno[0]+nombre[0]+anio[2:4]+mes[0:2]+dia[0:2]+genero[0]+nombreEstado+consonanteAP+consonanteAM+consonanteN+diferenciadorH+digitoV)    

#Flujo principal
curp()