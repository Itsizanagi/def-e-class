class Login:
    def __init__(self, nome, sobrenome, idade):
        self.nome = nome 
        self.sobrenome = sobrenome
        self.idade = idade
            
    
    def Confirmacao(nome):
        user = str(input('Qual é o seu nome? '))
        if user == nome:
            print('Nome corrreto')




controle_remoto = Login('gustavo', 'andrade', '12 anos')
print(controle_remoto.nome)
print(controle_remoto.sobrenome)
print(controle_remoto.idade)