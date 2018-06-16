def printSolution( sol ):
    for i in sol:
        for j in i:
            print(str(j) + " ", end="")
        print("")

def memo(i,j): # las filas y columnas de la matriz inicial
	MatrizMemo=[[-1] * (j) for k in range(i)] #matriz que guardara el valor minimo de cada camino DP
	return MatrizMemo
def spath(matriz,i,j,MatrizMemo): 
	#matriz dada
	#MatrizMemo matriz en donde se guardan los valores ya analizados
	#i filas
	#j columnas	

	if j < 0 or j > len(matriz[0])-1: # retorna si esta fuera de los limites de la columna
		return 0 # es un numero grande para que no lo tome en cuenta.

	if i > len(matriz)-1: # retorna cuando ya no quedan mas filas hacia abajo
		return 0 # es es cero para que no cambie la respuesta final
	if matriz[i][j]==0: ##
		return 10**5 # es un numero grande para que no lo tome en cuenta.

	if MatrizMemo[i][j] != -1: # si es diferente de -1 es porq ya saco el valor mas pequeño de un camino	
		#print("dinamic prro")
		return MatrizMemo[i][j] # retorna lo que tenia guardado


	P_AbajoIzq= matriz[i][j]+spath(matriz,i+1,j-1,MatrizMemo) #punto abajo a la izquierda del punto en el q se esta actualmente
	P_Abajo= matriz[i][j]+spath(matriz,i+1,j,MatrizMemo)	#abajo
	P_AbajoDer= matriz[i][j]+spath(matriz,i+1,j+1,MatrizMemo) #abajo der



	ValorMin=min(P_AbajoIzq,P_Abajo,P_AbajoDer) # elige el camino con menor valor (solo guarda la sumatoria de los caminos)
	
	if MatrizMemo[i][j] == -1 or (MatrizMemo[i][j] != -1 and ValorMin< MatrizMemo[i][j]): #si MatrizMemo[i][j] == -1 significa que todavia no ha analizado la energia de ese numero
		MatrizMemo[i][j]=ValorMin #Por lo tanto guarda los valores en el arreglo para no tener que sacar de nuevo el camino mas corto	
	return ValorMin

#input aca 
size=int(input("Ingrese size "))
MatrizMemo=memo(size,size)# crea un arreglo del tamaño de la matriz analizada para guardar las energia de los caminos

matriz = list([0 for i in range(size)])
for i in range(0,size):
    b = [int(x) for x in input("Ingrese la fila ").split()]
    matriz[i] = b

C_entrenamientos= int(input("Cantidad de entrenamientos "))
GastoTotal_E=0
for i in range (0,C_entrenamientos):
	gasto_i=int(input("ingrese cuanto energia gasto en el entrenamiento "))
	GastoTotal_E+=gasto_i
#matriz=[[0,580,2000],[0,0,220],[0,0,0]]  

for j in range (0,len(matriz[0])):
	if j!=0:
		spath(matriz,0,j,MatrizMemo)# analiza desde el primer elemento no nulo de la primera fila y si no hay nada en la fila hay q agregar q busque en la sgte pero me da paja, adios
		break

aux=10**5
for l in MatrizMemo[0]:
	if l==-1:
		pass
	else:
		if  l < aux:
			aux=l


MinimoValor=aux
CaloriasTotal=MinimoValor+GastoTotal_E
#print(CaloriasTotal)

EnergiaComida=0
c_doritos=0
c_power=0
def funn(CaloriasTotal,EnergiaComida,c_power,c_doritos):
	if CaloriasTotal<=EnergiaComida:
		kk=[c_power,c_doritos]
		return 
	c_doritos+=int(CaloriasTotal/700)
	EnergiaComida=CaloriasTotal-c_doritos*700
	if EnergiaComida<=400:
		c_power+=1
	else:
		funn(CaloriasTotal,EnergiaComida,0,c_doritos)
	return c_power,c_doritos

print(funn(CaloriasTotal,EnergiaComida,c_power,c_doritos))



#print("Valor minimo",MinimoValor)

