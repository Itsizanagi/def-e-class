import time

user_password = 1103
two_step_verification = 1104

print('='*50)
print('ボ Bem-vindo ao sistema de gestão ボ')
print('='*50)
print('Deseja entrar ?')
choice = str(input('Sim ou Não: ')).upper().strip()

if choice in 'SIM':
    print('Para entrar é preciso concluir o que se pede')
    print('Aguarde...')
    time.sleep(2)
    print('Digite sua senha para liberar o acesso!')
    user = int(input('Senha: '))
if user == user_password:
     print('Bem-Vindo')
     print(''' Digite seu horario atual.
               
    1. Anota
    2. 
    3. 
     ''')