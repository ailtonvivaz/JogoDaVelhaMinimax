import copy
from jogador import Jogador


# tabuleiro do jogo da velha
class Tabuleiro(object):
    def __init__(self, jogador):
        self.mapa = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        self.filhos = []
        self.ganhador = None
        self.valor = None
        self.vez = jogador
        self.vazio = 9
        self.prox_pos = None

    def apaga_filhos(self):
        self.filhos = []

    def imprimir(self):
        print ' {} | {} | {} '.format(self.mapa[0][0], self.mapa[0][1], self.mapa[0][2])
        print('--- --- ---')
        print ' {} | {} | {} '.format(self.mapa[1][0], self.mapa[1][1], self.mapa[1][2])
        print('--- --- ---')
        print ' {} | {} | {} '.format(self.mapa[2][0], self.mapa[2][1], self.mapa[2][2])
        print '\nvazio:', self.vazio, '\n'

    def jogar(self, lin, col):
        if self.mapa[lin][col] == " ":
            self.vazio -= 1
            self.mapa[lin][col] = self.vez.peca
            self.avaliar()
            if self.vez == Jogador.COMPUTADOR:
                self.vez = Jogador.HUMANO
            else:
                self.vez = Jogador.COMPUTADOR

    def gera_filhos(self):
        conta = 0
        if self.vazio > 0 or not self.isFinished():
            copia = copy.deepcopy(self)
            for i in range(3):
                for j in range(3):
                    if self.mapa[i][j] == ' ':
                        filho = copy.deepcopy(copia)
                        max = self.vez == Jogador.COMPUTADOR
                        filho.jogar(i, j)
                        filho.gera_filhos()
                        # self.filhos.append(filho)

                        # maximiza
                        if max:
                            if filho.valor >= self.valor or self.valor is None:
                                self.valor = filho.valor
                                self.prox_pos = (i, j)

                        # minimiza
                        else:
                            if filho.valor <= self.valor or self.valor is None:
                                self.valor = filho.valor
                                self.prox_pos = (i, j)

    def verifica_linhas(self):
        for linha in self.mapa:
            igual = linha[0] == linha[1] == linha[2] == self.vez.peca
            if igual:
                return igual

        return False

    def verifica_colunas(self):
        for coluna in range(3):
            igual = self.mapa[0][coluna] == self.mapa[1][coluna] == self.mapa[2][coluna] == self.vez.peca
            if igual:
                return igual

        return False

    def verifica_diagonais(self):
        return self.mapa[0][0] == self.mapa[1][1] == self.mapa[2][2] == self.vez.peca or \
               self.mapa[2][0] == self.mapa[1][1] == self.mapa[0][2] == self.vez.peca

    def isFinished(self):
        return self.ganhador != '' or self.vazio == 0

    def avaliar(self):
        if self.verifica_linhas() or \
                self.verifica_colunas() or \
                self.verifica_diagonais():
            self.ganhador = self.vez
        elif self.vazio == 0:
            self.ganhador = Jogador.VELHA
