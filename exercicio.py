def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Divis�o por zero n�o � permitida."

num1 = float(input("Digite o primeiro n�mero: "))
num2 = float(input("Digite o segundo n�mero: "))
operacao = input("Escolha a opera��o (+, -, *, /): ")

if operacao == '+':
    resultado = soma(num1, num2)
elif operacao == '-':
    resultado = subtracao(num1, num2)
elif operacao == '*':
    resultado = multiplicacao(num1, num2)
elif operacao == '/':
    resultado = divisao(num1, num2)
else:
    resultado = "Opera��o inv�lida."

print(f"Resultado: {resultado}")