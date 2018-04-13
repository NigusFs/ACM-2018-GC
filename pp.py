def pp(str1,x=0,y=1,c=0,count=0):
	if x<0 or y> len(str1)-1: #restriccion de limites
		return c
	if (str1[x]==str1[y]): 
		c+=1
		c+= pp(str1,x-1,y+1,0,1)
	if (count==1):
		return c
	if y+1 < len(str1)-1 and count ==0:
		if (str1[x]==str1[y+1]) :
			c+=1
			c+= pp(str1,x-1,y+2,0,1)

	return c + pp(str1,x+1,y+1,0)

a=input()
print(pp(a))