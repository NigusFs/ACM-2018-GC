#hay q analizar cuantos shif se deben hacer para que los binarios den match :s

def s_d(str1): #shift derecha a mano con string , hacerlo general para q entre el largo del string
	alfa=str1[15]
	str1=str1[:-1]
	str1=alfa +str1
	return str1

def s_i(str1): #shift izq a mano con string
	alfa=str1[0]
	str1=str1+alfa
	str1=str1[1:]
	return str1

key=input()
auxI=key
auxD=key
count=0

Y=int(input()) #casos
for i in range(0,Y):
	alfa=int(input()) # int q te dan
	b= "{0:016b}".format(alfa) # lo paso a binario

	while(auxD != b ): #se detiene cuando b es igual al binario shiftiado a la derecha
		count+=1 #sumo uno cada vez q se shift
		if count ==16:
			#print(count)
			break
		if (auxI == b): #se detiene cuando b es igual al binario shiftiado a la izq
			break
		auxD=s_d(auxD) # se shift a la dercha
		auxI=s_i(auxI) # y a la izq a la vez
		
	#cuando entra aca es porq ya encontro el valor	o llego al limite de shift (16)
	if(auxD == b ):
		print("correcto")
		print(count,"D")

	elif(auxI == b):
		print("correcto")
		print(count,"D")	
	else:
		print("Incorrecto")
		break
#print(key)


#https://stackoverflow.com/questions/10411085/converting-integer-to-binary-in-python/10411184





#https://stackoverflow.com/questions/10411085/converting-integer-to-binary-in-python/10411184


