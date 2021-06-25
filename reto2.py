#Importación de modulos necesarios para librerias matematicas
import math
#*************************
#**Definición de funciones
#*************************
# Funcion que compara la velocidad actual record contra la velocidad del record
def comparaVelocidad (velActual,velCorredor):
    if (velActual >= velCorredor) :
        print( 'VELOCIDAD NORMAL')
    if (velActual < velCorredor) :
        velDiff=(velCorredor-velActual)/velActual
        if (velDiff<0.2) :
            print( 'NUEVO RECORD')
        else :
            print( 'ENTREVISTA' )
 
# Funcion que calcula la velocidad del corredor
def velocidadcorredor(distancia,tiempoCorredor):
    distancia=distancia/1000
    tiempoCorredor=tiempoCorredor/3600
    return distancia/tiempoCorredor

#********************************
#**Código Principal de ejecucion
#********************************
# main ()

distancia,velActual,tiempoCorredor=input().split()
distancia=int(distancia)
velActual=int(velActual)
tiempoCorredor=int(tiempoCorredor)
if (tiempoCorredor<0  or velActual<0 or distancia<0):
    print('ERROR') 
else : 
    velCorredor=velocidadcorredor(distancia,tiempoCorredor)
    respuesta=comparaVelocidad (velActual,velCorredor)

