"""
Prueeba N
Entradas
Nombre-->str-->Nombre
Puntaje-->float-->Puntaje
"""
cantidad=int(input("Digite la cantidad de estudiantes:"))
Total=0
Puntaje_mayor=0.0
Puntaje_menor=()
Porcentaje_menor=0.0
Porcentaje_mayor=0.0
for p in range(1,cantidad+1):
    NombreyPuntaje=input("Digite su Nombre Completo y el puntaje obtenido:")
    Nombre,Puntaje=NombreyPuntaje.split(" ")
    Puntaje=float(Puntaje)
    Total+=Puntaje
    if(Puntaje_mayor<=Puntaje):
        Puntaje_mayor=Puntaje
    #elif(Puntaje_menor<Puntaje):
       # Puntaje_menor=Puntaje
    elif(Puntaje<Total):
        Porcentaje_menor+=1
    elif(Puntaje>=Total):
        Porcentaje_mayor+=1
        
print(f"El puntaje mas alto fue obtenido por:\n{Nombre} con {Puntaje_mayor}")
#print(f"El Puntaje mas bajo fue obtenido por:\n {Nombre} con {Puntaje_menor}")
print(f"El promedio es:{round(Total/cantidad,2)}")
#print(f"El promedio de estudiantes con puntaje menor a la media es: {Puntaje_menor}/100")
print(f"El Promedio de estudiantes con pntaje mayor al promedio es: {Puntaje_mayor/100}")
