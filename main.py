from Calculadora import Calculadora
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
