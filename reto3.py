#Importación de modulos necesarios para librerias matematicas
def validaCondiciones(nroEstadio,tmnEstadio,altEstadio,equipos,dinero):
    if nroEstadio>=12 and tmnEstadio>=35000 and altEstadio<=1500 and equipos>=3:
        resultados.append(dinero)
       
  #  else:
  #     print("no hay plata")


resultados=[]
f=int(input())

#Ciclo para repetir la Sentencia
for i in range (1,(f+1)):
    nroEstadio,tmnEstadio,altEstadio,equipos,dinero=input().split()
    nroEstadio=int(nroEstadio)
    tmnEstadio=int(tmnEstadio)
    altEstadio=int(altEstadio)
    equipos=int(equipos)
    dinero=int(dinero)
    validaCondiciones(nroEstadio,tmnEstadio,altEstadio,equipos,dinero)
#Resultado
if len(resultados)==0:
    print ( 'NO DISPONIBLE')
else:
    print(resultados[0])

