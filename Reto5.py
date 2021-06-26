
def AGREGAR(indice,x):
    
    if indice <len(tienda):
       ERROR=1
    else:
        tienda.append(x)
        ERROR=0
    return ERROR
   # print(tienda[10])

def ACTUALIZAR(indice,Y):
    #print(indice)
    #print(Y)
    actualizareg=0
    
    if indice <=len(tienda):
        tienda[indice]=Y   
        ERROR=0
    else:
        ERROR=1
    return ERROR
    #print(tienda[6])

def BORRAR(indice):
    if indice in tienda:
        tienda.remove(indice)    
        ERROR=0
    else:
        ERROR=1
    return ERROR 

def pmayor(x,y) :
    precioMayor=0
    if x<y:
        precioMayor=y
    else:
        precioMayor=x
    return precioMayor

def calcNombreProductoMayor():
    precioMayor=0
    listPrecioMayor=[]
    for i in range(len(tienda)):
       prod=tienda[i]
       precioMayor=pmayor(prod[2],precioMayor) #envia precios
       if prod[2]==precioMayor:
           listPrecioMayor=prod
    return listPrecioMayor[1]

def pmenor(prod,precioMenorlist) :
    precioProducto=prod[2]
    listaresultado=[]
    precioMenor=0
    if len(precioMenorlist)==0:
        precioMenor=9999999999
    else:
        precioMenor=precioMenorlist[2]

    if precioProducto>=precioMenor:
        listaresultado=precioMenorlist
    else:
        listaresultado=prod
    #print(listaresultado)
    return listaresultado


def calcNombreProductoMenor():
    
    listPrecioMenor=[]
    for i in range(len(tienda)):
       prod=tienda[i]
       listPrecioMenor=pmenor(prod,listPrecioMenor) #envia precios   
     #  print(prod,listPrecioMenor)  
    return listPrecioMenor[1]

def calcPromedioPrecios():
    promPrecios=0
    for i in range(len(tienda)):
       prod=tienda[i]
       promPrecios=prod[2]+promPrecios #envia precios
    promPrecios=promPrecios/len(tienda)
    return round(promPrecios,1)
def calcValorInventario(): 
    valorInventario=0
    for i in range(len(tienda)):
       prod=tienda[i]
       valorInventario=(prod[2]*prod[3])+valorInventario #envia precios
    return round(valorInventario,1)

#Variables
tienda=[
[1,"Manzanas",6000.0,25],
[2,"Limones",2500.0,15],
[3,"Peras",2700.0,33],
[4,"Arandanos",9300.0,34],
[5,"Tomates",2100.0,42],
[6,"Fresas",4100.0,10],
[7,"Helado",4500.0,41],
[8,"Galletas",500.0,8],
[9,"Chocolates",4500.0,80],
[10,"Jamon",15000.0,10]
]
#********************
#**********main******
#********************

x=input()
id,producto,valor,cantidad=input().split()
id=int(id)
valor=float(valor)
cantidad=int(cantidad)
indice=id-1 #dado que la posicion en lista inicia en 0
Y=[id,producto,valor,cantidad]
esError=0
if x == 'ACTUALIZAR':
	esError=ACTUALIZAR(indice,Y)
if x == 'AGREGAR':
	esError=AGREGAR(indice,Y)   
if x == 'BORRAR':
	esError=BORRAR(Y)

if esError==1:
    print('ERROR')
else:
    nombreProdMayor=calcNombreProductoMayor()
    nombreProdMenor=calcNombreProductoMenor()
    promedioDePrecios=calcPromedioPrecios()
    valorInventario=calcValorInventario()
    print(nombreProdMayor,nombreProdMenor
        ,promedioDePrecios,valorInventario)


#Arandanos Galletas 3670.0 1275500.0