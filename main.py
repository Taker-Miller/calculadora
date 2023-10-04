from Calculadora import Calculadora
#OTRO METODO 
#n1 = input("ingresa valor: ")
#n2 = input("ingresa valor: ")
#c = Calculadora(n1, n2)
#print(c) #para el caso de def str
#c.mostrar_resultado() #para el caso de mostrar_resultado

def calcular():
    while True:
        print("1. suma")
        print("2. resta")
        print("3. multiplicar")
        print("4. division")
        print("5. salir")
        opcion = input("ingresa una opcion: ")
        if opcion == "5":
            print("adios")
            break
        num1 = int(input("ingresa primer numero: "))
        num2 = int(input("ingresa segundo numero: "))
        c = Calculadora(num1,num2) # ----> Se crea un objeto
        if opcion == "1":
            resultado = c.suma()
        elif opcion == "2":
             resultado = c.resta()
        elif opcion == "3":
             resultado = c.multiplicar()
        elif opcion == "4":
             resultado = c.dividir()
        else:
            print("Valor no valido")
        print(f"resultado: {resultado}")

calcular()
