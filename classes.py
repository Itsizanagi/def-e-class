class ControleRemoto:
    def __init__(self, cor, altura, profundidade, largura):
        self.cor = cor # cor = valor / self.cor = caracteristica
        self.altura = altura
        self.profundidade = profundidade
        self.largura = largura
        
    def passar_canal(self,botao):
        if botao == "+":
            print('Aumentar o Canal')
        elif botao == "-":
            print('Diminuir o Canal')



controle_remoto = ControleRemoto('preto', '10cm', '2cm', '2cm')
print(controle_remoto.cor)
print(controle_remoto.altura)
print(controle_remoto.profundidade)
print(controle_remoto.largura)
controle_remoto.passar_canal("+")