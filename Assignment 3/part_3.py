x="string@1&2$" 
freq = {}   
for i in x: 
    for j in i:
        if (ord(i)==64 and ord(i)==36 and ord(i)==38) in freq:
            freq.append(i,j)
   
print(str(freq))