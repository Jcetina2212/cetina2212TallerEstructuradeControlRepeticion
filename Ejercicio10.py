#entrada
cantidad=int(input("Digite el numero de estudiantes:"))
altura_mayor=0
#entradas
for i in range(1,cantidad+1):
    altura=float(input("Digite la altura"))
    if(altura_mayor<=altura):
        altura_mayor=altura
#salidas
print(altura_mayor)
