"""
1. Alcohol 2. Gasoline 3. Diesel 4. End
"""
Alcool=0
Gasolina=0
Diesel=0
while True:
    codigo=int(input())
    if(codigo==1):
        Alcool+=1
    elif(codigo==2):
        Gasolina+=1
    elif(codigo==3):
        Diesel+=1    
    elif(codigo==4):
        break
    else:
        continue
print("MUITO OBRIGABO")
print(f"Alcool: {Alcool}")
print(f"Gasolina: {Gasolina}")   
print(f"Diesel: {Diesel}")