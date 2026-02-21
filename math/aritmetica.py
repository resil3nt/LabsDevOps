class Aritmetica:

    #Realizar Operaciones aritmeticas basicas
    
    def __init__(self, operandoA, operandoB):
        self.operandoA = operandoA
        self.operandoB = operandoB

    def sumar(self):
        return self.operandoA + self.operandoB
    
    def restar(self):
        return self.operandoA - self.operandoB

    def multiplicar(self):
        return self.operandoA * self.operandoB

    def dividir(self):
        return self.operandoA * self.operandoB
    
aritmetica1= Aritmetica(5,3)
print(f'Suma: {aritmetica1.sumar()}') # Se imprime la sumatoria de los numeros
print(f'Resta: {aritmetica1.restar()}') # Se imprime la resta de los numeros
print(f'Multiplicacion: {aritmetica1.multiplicar()}') # Se imprime la multiplicación de los numeros
print(f'Division: {aritmetica1.dividir()}') # Se imprime la división de los numeros



