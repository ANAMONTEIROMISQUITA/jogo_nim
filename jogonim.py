import random

class JogoNin: 
    def __init__(self, pedras=21, max_retirada=3, modo='Pessoa vs Pessoa'): 
        self.pedras = pedras 
        self.max_retirada = max_retirada 
        self.modo = modo 
        self.jogador = 1

    def exibir_estado(self):
        print(f"\nPedras restantes: {self.pedras}")

    def jogada_computador(self):
        retirada = (self.pedras - 1) % (self.max_retirada + 1) or random.randint (1, min(self.max_retirada, self.pedras))
        print(f"Computador retirou {retirada} pedras.")
        return retirada

    def jogada_humana(self):
        while True:
            try:
                retirada = int(input(f"Jogador {self.jogador}, escolha entre 1 e {min(self.max_retirada, self.pedras)} pedras: "))
                if 1 <= retirada <= min(self.max_retirada, self.pedras):
                    return retirada
            except ValueError:
                pass
            print(f"Escolha inválida! Tente novamente (1-{min(self.max_retirada, self.pedras)}).")

    def jogar(self):
        print(f"Bem-vindo ao Jogo do Nim! Começamos com {self.pedras} pedras.")
        while self.pedras > 0:
            self.exibir_estado()
            retirada = self.jogada_computador() if self.modo == '2' and self.jogador == 2 else self.jogada_humana()
            self.pedras -= retirada
            if self.pedras == 0:
                print(f"Jogador {self.jogador} retirou a última pedra e perdeu o jogo!")
                return
            self.jogador = 3 - self.jogador

modo = input("Escolha o modo 1 para Pessoa vs Pessoa ou 2 para Pessoa vs Computador: ").strip() 
if modo not in ['1', '2']: 
    print("Modo inválido! O jogo será iniciado no modo Pessoa vs Pessoa por padrão.") 
    modo = 'Pessoa vs Pessoa'

jogo = JogoNin (21, 3, modo) 
jogo.jogar()





