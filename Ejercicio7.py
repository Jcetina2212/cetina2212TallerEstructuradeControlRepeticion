while True:
    #entradas
    datos=input()
    m,x=datos.split(" ")
    m=int(m)
    x=int(x)
    if(x==0 and m==0):
        break
    #caja negra
    r=m*x
    #salidas
    print(r)


