temp={}
for i in range(1,50,+1) :
		for j in range (i**3,50) :
				if((i%2!=0) and (j<50)):
					temp.append((tuple((i,j)))
print (temp)       