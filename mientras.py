controladora=100
print("*** Empanadas****")
print("**********************")
print("1. agregar sabor de empanada")
print("2. mostrar sabor de empanada")
print("3. cambiar sabor de empanada")
print("0.SALIR ")

while (controladora!=0):
        empanada=None
        controladora=int(input("Digita una opcion: "))
        if controladora==1:
                empanada=input("cual es el sabor: ")
        elif controladora==2:
                print(f"el sabor es {empanada}")
        elif controladora==3:
                empanada=input("cual es el sabor: ")

        elif controladora==0:
                print("vuelve pronto")
        else:
                
           print("opcion invalida")
        