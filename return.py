# Criando uma classe 
class Carro:
    # Cria a funcionalidade inicial da classe, no nosso caso, iremos definir as propriedades da classe
    def __init__(self, marca, cor):
        self.marca = marca
        self.cor = cor

    # Cria um método, no nosso caso, iremos criar um método para ligar o carro.
    def ligar(self):
        print(f'O carro da marca {self.marca} de cor {self.cor} ligou')


# Instanciando uma classe
carro1 = Carro('agrale', 'preta')
# Obtendo os dados da instância
print(carro1.marca, carro1.cor)
# Chamando a propriedade "ligar" presente na classe
carro1.ligar()