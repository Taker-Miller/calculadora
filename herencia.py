def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        print("no se puede dividir por cero")




def calculadora():
    while True:
        print("1. suma")
        print("2. resta")
        print("3. multiplicacion")
        print("4. division")
        print("5. salir")
        opcion = input("ingrese una opcion: ")
        if opcion == "5":
            print("adios")
            break
        n1 = int(input("ingresa numero "))
        n2 = int(input("ingresa numero "))
        if opcion == "1":
            print("resultado de la suma: ", suma(n1, n2))
        elif opcion == "2":
            print("resultado de la resta", resta(n1, n2))
        elif opcion == "3":
            print("resultado de la multiplicacion", multiplicar(n1, n2))
        elif opcion == "4":
            print("resultado de la division", dividir(n1, n2))
        else:
            print("valor invalido")

calculadora()