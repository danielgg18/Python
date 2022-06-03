#Nombre del programa: calcCurp.py
#Autor: Daniel Garcia
#Fecha: 31/05/22
#Descripcion del programa: Programa que calcula el CURP con los datos de una persona

import os

def curp():
    
    #Diccionario que contiene las entidades federativas de Mexico y sus respectivas abreviaciones
    entidades = {
    1:['1.Aguascalientes','AS'], 
    2:['2.Baja California','BC'], 
    3:['3.Baja California Sur','BS'],
    4:['4.Campeche','CC'], 
    5:['5.Chiapas','CS'], 
    6:['6.Chihuahua','CH'], 
    7:['7.Coahuila','CL'],
    8:['8.Colima','CM'], 
    9:['9.Ciudad de Mexico','DF'], 
    10:['10.Durango','DG'], 
    11:['11.Guanajuato','GT'],
    12:['12.Guerrero','GR'], 
    13:['13.Hidalgo','HG'], 
    14:['14.Jalisco','JC'], 
    15:['15.Estado de Mexico','MC'],
    16:['16.Michoacan','MN'], 
    17:['17.Morelos','MS'], 
    18:['18.Nayarit','NT'], 
    19:['19.Nuevo Leon','NL'],
    20:['20.Oaxaca','OC'], 
    21:['21.Puebla','PL'], 
    22:['22.Queretaro','QO'],
    23:['23.Quintana Roo','QR'],
    24:['24.San Luis Potosi','SP'], 
    25:['25.Sinaloa','SL'], 
    26:['26.Sonora','SR'], 
    27:['27.Tabasco','TC'],
    28:['28.Tamaulipas','TS'], 
    29:['29.Tlaxcala','TL'], 
    30:['30.Veracruz','VZ'], 
    31:['31.Yucatan','YN'], 
    32:['32.Zacatecas','ZS']
    }
    
    
    nombre=input("Escriba su nombre: ").upper()
    aPaterno=input("Escriba su apellido paterno: ").upper()
    aMaterno=input("Escriba su apellido materno: ").upper()
        

    dia=input("Dia de nacimiento: ")
    mes=input("Mes de nacimiento: ")
    anio=input("Año de nacimiento: ")
        
        
    genero=input("¿Cuál es su género?(Hombre o Mujer) ").upper()
    
    os.system ("clear")

    for x in entidades:
        print(entidades[x][0])

    entidadFederativa=int(input("¿En qué entidad federativa nació? "))
    
    if entidadFederativa == 1:
        entidadFederativa = entidades[1][1]
        aEntidad = entidadFederativa
    elif entidadFederativa > 1:
        while x < entidades:
            x += 1 
            #aux = str(aux)
            entidadFederativa = entidades[entidadFederativa][1]

    """ elif entidadFederativa == 2:
        entidadFederativa = entidades['2'][1]
        aEntidad = entidadFederativa
    elif entidadFederativa == 3:
        entidadFederativa = entidades['3'][1]
        aEntidad = entidadFederativa
    elif entidadFederativa == 4:
        entidadFederativa = entidades['4'][1]
        aEntidad = entidadFederativa
    elif entidadFederativa == 5:
        entidadFederativa = entidades['5'][1]
        aEntidad = entidadFederativa
    elif entidadFederativa == 6:
        entidadFederativa = entidades['6'][1]
        aEntidad = entidadFederativa
    elif entidadFederativa == 7:
        entidadFederativa = entidades['7'][1]
        aEntidad = entidadFederativa
    elif entidadFederativa == 8:
        entidadFederativa = entidades['8'][1]
        aEntidad = entidadFederativa
    elif entidadFederativa == 9:
        entidadFederativa = entidades['9'][1]
        aEntidad = entidadFederativa
    elif entidadFederativa == 10:
        entidadFederativa = entidades['10'][1]
        aEntidad = entidadFederativa
    elif entidadFederativa == 11:
        entidadFederativa = entidades['11'][1]
        aEntidad = entidadFederativa
    elif entidadFederativa == 12:
        entidadFederativa = entidades['12'][1]
        aEntidad = entidadFederativa
    elif entidadFederativa == 13:
        entidadFederativa = entidades['13'][1]
        aEntidad = entidadFederativa
    elif entidadFederativa == 14:
        entidadFederativa = entidades['14'][1]
        aEntidad = entidadFederativa
    elif entidadFederativa == 15:
        entidadFederativa = entidades['15'][1]
        aEntidad = entidadFederativa
    elif entidadFederativa == 16:
        entidadFederativa = entidades['16'][1]
        aEntidad = entidadFederativa
    elif entidadFederativa == 17:
        entidadFederativa = entidades['17'][1]
        aEntidad = entidadFederativa
    elif entidadFederativa == 18:
        entidadFederativa = entidades['18'][1]
        aEntidad = entidadFederativa
    elif entidadFederativa == 19:
        entidadFederativa = entidades['19'][1]
        aEntidad = entidadFederativa
    elif entidadFederativa == 20:
        entidadFederativa = entidades['20'][1]
        aEntidad = entidadFederativa
    elif entidadFederativa == 21:
        entidadFederativa = entidades['21'][1]
        aEntidad = entidadFederativa
    elif entidadFederativa == 22:
        entidadFederativa = entidades['22'][1]
        aEntidad = entidadFederativa
    elif entidadFederativa == 23:
        entidadFederativa = entidades['23'][1]
        aEntidad = entidadFederativa
    elif entidadFederativa == 24:
        entidadFederativa = entidades['24'][1]
        aEntidad = entidadFederativa
    elif entidadFederativa == 25:
        entidadFederativa = entidades['25'][1]
        aEntidad = entidadFederativa
    elif entidadFederativa == 26:
        entidadFederativa = entidades['26'][1]
        aEntidad = entidadFederativa
    elif entidadFederativa == 27:
        entidadFederativa = entidades['27'][1]
        aEntidad = entidadFederativa
    elif entidadFederativa == 28:
        entidadFederativa = entidades['28'][1]
        aEntidad = entidadFederativa
    elif entidadFederativa == 29:
        entidadFederativa = entidades['29'][1]
        aEntidad = entidadFederativa
    elif entidadFederativa == 30:
        entidadFederativa = entidades['30'][1]
        aEntidad = entidadFederativa
    elif entidadFederativa == 31:
        entidadFederativa = entidades['31'][1]
        aEntidad = entidadFederativa
    elif entidadFederativa == 32:
        entidadFederativa = entidades['32'][1]
        aEntidad = entidadFederativa
 """
    diferenciadorH=str(0)
    digitoV=str(9)

    print("Su CURP es: ", aPaterno[0:2]+aMaterno[0]+nombre[0]+anio[2:4]+mes[0:2]+dia[0:2]+genero[0]+entidadFederativa+aPaterno[2]+aMaterno[2]+nombre[1]+diferenciadorH+digitoV)    

#Flujo principal
curp()