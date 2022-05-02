"""
while True:
    numeros=int(input())
    #condicion de salida
    if(numeros==2002):
        print("Acesso Permitido")
        break
    else:
        print("Senha Invalida")
"""
c=0
numero=int(input())
while(numero!=2002):
    c+=1
    if(c==3):
        print("Demasiados intentos")
        break
    print("Senha Invalida")
    numero=int(input())  
else:
    print("Acesso Permitido")