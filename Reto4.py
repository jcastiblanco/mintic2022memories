#Reto 4: Detectando fraude en los talleres de matemáticas
#Numero de muestras
N=0 
#Memoria de profesor
k=0 
#Funciones
def sublist(x ,posc): 
    y=[] ##declara nueva lista
    for i in range(posc):            
       y.append(x[i])
    return y

def sublistProfe(x ,posc,inicial): 
    y=[] ##declara nueva lista
    
    for i in range(inicial,posc):            
       y.append(x[i])
    return y

def tieneFraude(sublist,valor):
    fraude=0
    if valor in sublist:
        fraude=1
    else:
        fraude=0
    return fraude
#**************************
#********Main**************
#************************** 
N,f=map(int,input().split())
r=list(input().split())  # Guardar la entrada de examenes en una lista
largoLista=len(r) 
contfraudeProgram=0
contfraudeProfe=0
#Rutina Python

for i in range(N-1):
        k=i+1
        #print (r[k] )
        sublista=sublist(r,k)
        #print (sublista)
        #print(r[k])
        contfraudeProgram=contfraudeProgram+tieneFraude(sublista,r[k])

#Rutina profesor
for i in range(N-1):
        k=i+1
        if(k-f)<0:
            w=0 
        else: 
            w=k-f
        #print (r[k] )
        #print(w)
        sublista=sublistProfe(r,k,w)
        #print (sublista)
        #print(i)
        contfraudeProfe=contfraudeProfe+tieneFraude(sublista,r[k])
print(contfraudeProgram,contfraudeProfe)
       


 
