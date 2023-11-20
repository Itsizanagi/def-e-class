import time


class Login:
    def __init__(self, nome, sobrenome, idade):
        self.nome = nome
        user = str(input('Qual é o seu nome? '))
        if user == nome:
            print('Verificando...')
            time.sleep(3)
            print('Nome correto')
        else:
            raise Exception('Seu nome esta invalido ')
        self.sobrenome = sobrenome
        user = str(input('Qual é o seu sobrenome? '))
        if user == sobrenome:
            print('Verificando...')
            time.sleep(3)
            print('sobrenome correto')
        else:
            raise Exception('Seu nome esta invalido ')
        self.idade = idade
        user = str(input('Qual é sua idade ?'))
        if user == idade:
            print('Verificando...')
            time.sleep(3)
            print('idade correta')
        else:
            raise Exception('Seu nome esta invalido ')
        
        print('Aguarde...')
        time.sleep(2)
controle_remoto = Login('gustavo', 'andrade', '12')
print('='*50)
print(f' Seu nome é: {controle_remoto.nome}')
print(f' Seu sobrenome é :{controle_remoto.sobrenome}')
print(f' Sua idade é: {controle_remoto.idade}')
print('='*50)
senha_usuario = 12334

print(' ++++ Bem-Vindo ao sistema de gestão ++++')
print('Deseja em entrar ? ')
entrada = str(input('Sim ou Não: ')).upper().strip()

if entrada in 'SIM':
    print('Bem-Vindo ao sistema!!')
    print('Aguarde...')
    time.sleep(2)
    print('Digite sua senha para liberar o acesso!')
    user = int(input('Senha: '))

    if user == senha_usuario:
        print('''Sua Opções:
              
    1. Verificar saldo total 
    2. Verificar estado atual da loja 
    3. Verificar saldo bancário
              ''')
        usuario = int(input('Digite uma ação: '))
        if usuario == 1:
            print('Saldo total registrado com sucesso')
            time.sleep(2)
            print('Saldo: 13.500')
        elif usuario == 2:
         print(''' Digite seu horario atual.
               
    1. Manhã
    2. Tarde
    3. Noite
''')
         date = int(input('Qual sua opção: '))
         if date == 1:
              print('Bom-dia!')
              print('Estado atual: Aberto!')
         elif date == 2:
              print('Boa-Tarde!')
              print('Estado atual: Aberto!')
         elif date == 3:
              print('Boa-noite')
              print('Estado atual: Fechado!')

        elif usuario == 3:
         print('Acesso restrito!')
         verif = int(input('Digite sua senha: '))
         if verif == senha_usuario:
              print('''Opções de entrada: 
                    
                    1. Verificar saldo atual
                    2. Sair
                    ''')
              acess = int(input('Qual sua entrada: '))
              if acess == 1:
                   print('Saldo atual: R$ 5.000 recebidos ')
              elif acess == 2:
                   print('Saindo...')
                   time.sleep(3)
                   exit()
    else:
         print('Senha incorreta')
else:
    print('Até mais')
    print('Fechando sistema...')
    time.sleep(3)