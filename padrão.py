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
        return "Divisão por zero não é permitida."

# Exemplo de uso
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operacao = input("Escolha a operação (+, -, *, /): ")

if operacao == '+':
    resultado = soma(num1, num2)
elif operacao == '-':
    resultado = subtracao(num1, num2)
elif operacao == '*':
    resultado = multiplicacao(num1, num2)
elif operacao == '/':
    resultado = divisao(num1, num2)
else:
    resultado = "Operação inválida."

print(f"Resultado: {resultado}")