"""
mostras la suma de todos los numeros pares 
comprendidos entre 97 y 1003
"""
#entradas
sumatoria=0
for i in range(97,1004):
    if(i%2==1):
        continue
    sumatoria+=i
    print(i)
print("La sumatoria es:",sumatoria)