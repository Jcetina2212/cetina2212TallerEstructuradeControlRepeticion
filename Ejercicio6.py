"""
Efectuar la divicion de dos numero enteros usando el metodo de la de las restas sucesivas
Enttradas
Numero1(Dividendo)-->int-->n1
NumeroDivisor)2(-->int--n2
caja negra 
cociente-->float-->co
"""
#Entradas
numeros=input("")
n1,n2=numeros.split("/")
n1=int(n1)
n2=int(n2)
diferencia=0
while(n1>n2):
    if(n1!=n2):
        n3=n1-n2
        diferencia+=n3
    else:
        break
print(diferencia)
