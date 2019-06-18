temp=[]
for i in range(1,22):
	for j in range(i+1,22):
		if((i+j)%2==0 and (i+j) in range(22)):
			temp.append(tuple((i,j)))
print(temp)