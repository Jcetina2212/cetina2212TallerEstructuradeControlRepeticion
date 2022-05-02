"""
Encuesta
Entradas
Consume licor-->str-->consume_licor(r1)
Licor preferido-->str-->licor_preferido(r2)
1-Aguardiante, 2-Ron, 3-Cerveza, 4-Tequila, 
5-Whisky, 6-Otro
Edad-->int-->edad(r3)
Sexo-->str-->Sexo(r4)
"""
si=0
no=0
Aguardiente=0
Ron=0
Cerveza=0
Tequila=0
Whisky=0
Otro=0
Edad=0
hombre=0
mujer=0
c=0
s=""
t=""
while True:
    c+=1
    r1=str(input("¿Conusme licor?\n"))
    if(r1==si):
        si+=1
    else:
        no+=1
    print("1-Aguardiente\n 2-Ron\n 3-Cerveza\n 4-Tequila\n 5-Whisky\n 6-otro")
    r2=int(input("¿Licor preferido?\n"))
    if(r2==1):
        Aguardiente+=1
    elif(r2==2):
        Ron+=1
    elif(r2==3):
        Cerveza+=1
    elif(r2==4):
        Tequila+=1
    elif(r2==5):
        Whisky+=1
    elif(r2==6):
        Otro+=1
    r3=int(input("Digite su edad: "))
    r4=str(input("Digite su sexo:"))
    if(r4==hombre):
        hombre+=1
    elif(r4==mujer):
        mujer+=1
    #condicion de cierre
    r5=str(input("Si desea terminar digite t o s para continua\n"))
    if(r5==t):
        continue
    else:
        break
    #salidas
print(f"El total de personas encuentadas es de: {c}")
print(f"La cantidad de personas que toman licor es:\n Aguardiente:{Aguardiente}\n Ron:{Ron}\n Cerveza:{Cerveza}\nTequila{Tequila}\nwhisky:{Whisky}\nOtro:{Otro}")
print(f"La cantidad de hombres encuestados es:{hombre}\n La cantidad de mujers encuastadas es:{mujer}")
    
        

