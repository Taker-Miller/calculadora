class Calculadora:
    def __init__(self, num1, num2):
        self.__num1 = num1
        self.__num2 = num2

    def get_numero1(self):
        return self.__num1
    def set_numero1(self, num1):
        self.__num1 = num1
    
    def get_numero2(self):
        return self.__num2
    def set_numero2(self, num2):
        self.__num2 = num2

    def suma(self):
        return self.__num1 + self.__num2
    
    def resta(self):
        return self.__num1 - self.__num2
    
    def multiplicar(self):
        return self.__num1 * self.__num2
    
    def dividir(self):
        if self.__num2 != 0:
            return self.__num1 / self.__num2
        else:
            print("no se puede dividir por 0")

    
