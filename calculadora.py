''' Calculadora com while '''

while True:

    num1 = input('Digite um número: ')
    num2 = input('Digite outro número: ')
    operador = input('Digite um operador (+-/*): ')

    numeoros_validos = None
    num1_float = 0
    num2_float = 0
    numeoros_validos = True

    try:
        num1_float = float(num1)
        num2_float = float(num2)
        numeoros_validos = True
    except:
        numeoros_validos = None

    if numeoros_validos is None:
        print('Um ou ambos os números digitados são inválidos')
        continue

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('Oparador inválido')
        continue
    if len(operador) > 1:
        print('Digite apenas 1 operador')
        continue

    print('Realizando sua conta ')
    if operador == '+':
        print(f'{num1_float} + {num2_float}=', num1_float + num2_float)
    elif  operador == '-':
        print(f'{num1_float} - {num2_float}=',num1_float - num2_float)
    elif operador == '/':
        print(f'{num1_float} / {num2_float}=',num1_float / num2_float)
    elif operador == '*':
        print(f'{num1_float} * {num2_float}=',num1_float * num2_float)


    sair = input('Quer sair? [s]im: ')
    sair = sair.lower()
    sair = sair.startswith('s')
    print(sair)

    if sair is True:
        break