#imprima numero1..100 inpares /7
for c in range(1,101,1):
    if(c%2==0 or c%7==0):
        continue
    print(c)

