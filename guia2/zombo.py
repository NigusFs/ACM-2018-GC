count=0
a='{0:016b}'.format(9)
b="{0:016b}".format(32772)
#hay q analizar cuantos shif se deben hacer para que los binarios den match :s

def s_d(str1):
	alfa=str1[15]
	str1=str1[:-1]
	str1=alfa +str1
	return str1

def s_i(str1):
	alfa=str1[0]
	str1=str1+alfa
	str1=str1[1:]
	
	return str1

print(a,"9")

a=s_d(a)

print(a,"32772")


a=s_i(a)
a=s_i(a)

print(a,"18")


#https://stackoverflow.com/questions/10411085/converting-integer-to-binary-in-python/10411184


