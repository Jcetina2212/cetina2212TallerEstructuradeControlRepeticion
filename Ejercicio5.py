suma=0
c=0
for k in range(1,1000):
    if(suma<=1000):
        suma+=((k**2)+1)/k
        if(suma<=1000):
            c+=1
    else:
        break
print(suma)
    
