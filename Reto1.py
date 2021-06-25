#Importación de modulos necesarios para librerias matematicas
import decimal
import math
#********************************
#**Código Principal de ejecucion
#********************************
# main ()

#Variables
salarioBase=176
pcthorasExtras=1.25
horasExtras=0
pctbonificacion=0.065
salarioBase=0
salarioExtras=0
salarioBonificaciones=0

planDeSalud=0.025
aportePension=0.025
cajaCompensacion=0.04
esbonificiacion=0

salarioBase,horasExtras,esbonificiacion=input().split()
salarioBase = float(salarioBase )
horasExtras= int(horasExtras)
esbonificiacion= int(esbonificiacion)
#Operaciones
salarioExtras=horasExtras * ((salarioBase/176) *  pcthorasExtras)
salarioBonificaciones=esbonificiacion*(salarioBase * pctbonificacion)
salarioTotal=round((salarioBase + salarioExtras + salarioBonificaciones),1)
salarioDespuesDescuentos=round((salarioBase + salarioExtras + salarioBonificaciones)-(salarioTotal*0.09),1)

#Resultado
print(f"{salarioTotal} {salarioDespuesDescuentos}")

#1000000 5 0
