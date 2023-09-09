# Faça uma função calculadora de dois números com três parâmetros: os dois primeiros serão os números da operação e o terceiro será a entrada que definirá a operação a ser executada. Considera a seguinte definição:
# 1. Soma
# 2. Subtração
# 3. Multiplicação
# 4. Divisão

# Caso seja inserido um número de operação que não exista, o resultado deverá ser 0.

def calculadora(num1, num2, operacao):
    if operacao == 1:  
        resultado = num1 + num2
    elif operacao == 2:  
        resultado = num1 - num2
    elif operacao == 3:  
        resultado = num1 * num2
    elif operacao == 4:  
        if num2 != 0:
            resultado = num1 / num2
        else:
            print("Você não pode fazer divisão por zero")
            return 0
    else:
        print("Operação inválida: O número inserido não existe ou isso não é um número")
        return 0

    return resultado

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operacao = int(input("Escolha a operação:  "))

result = calculadora(num1, num2, operacao)

print("Resultado: ", result)