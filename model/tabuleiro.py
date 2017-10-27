import copy
from jogador import Jogador
from node import Node


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
        self.node = Node()

    def apaga_filhos(self):
        self.filhos = []

    def imprimir(self):
        print '*   0   1   2 \n'
        print '0   {} | {} | {} '.format(self.mapa[0][0], self.mapa[0][1], self.mapa[0][2])
        print('   --- --- ---')
        print '1   {} | {} | {} '.format(self.mapa[1][0], self.mapa[1][1], self.mapa[1][2])
        print('   --- --- ---')
        print '2   {} | {} | {} '.format(self.mapa[2][0], self.mapa[2][1], self.mapa[2][2])
        print '\nvazio:', self.vazio, '\n'

    def jogar(self, lin, col):
        if self.vazio > 0 and self.mapa[lin][col] == " ":
            self.vazio -= 1
            self.mapa[lin][col] = self.vez.peca
            self.avaliar()

            if self.ganhador is not None:
                self.valor = self.ganhador.valor

            if self.vez == Jogador.COMPUTADOR:
                self.vez = Jogador.HUMANO
            else:
                self.vez = Jogador.COMPUTADOR

            return True
        else:
            return False

    def gera_filhos(self):

        if not self.isFinished():

            if self.vazio == 0:
                self.ganhador = Jogador.VELHA
            else:
                copia = copy.deepcopy(self)
                for i in range(3):
                    for j in range(3):
                        if self.mapa[i][j] == ' ':
                            filho = copy.deepcopy(copia)
                            filho.jogar(i, j)
                            filho.gera_filhos()
                            # self.filhos.append(filho)

                            max = self.vez == Jogador.COMPUTADOR

                            if self.valor is None or (max and filho.valor > self.valor) or (
                                        not max and filho.valor < self.valor):
                                self.valor = filho.valor
                                self.prox_pos = (i, j)

    def verifica_linhas(self):
        return self.mapa[0][0] == self.mapa[0][1] == self.mapa[0][2] == self.vez.peca or \
               self.mapa[1][0] == self.mapa[1][1] == self.mapa[1][2] == self.vez.peca or \
               self.mapa[2][0] == self.mapa[2][1] == self.mapa[2][2] == self.vez.peca

    def verifica_colunas(self):
        return self.mapa[0][0] == self.mapa[1][0] == self.mapa[2][0] == self.vez.peca or \
               self.mapa[0][1] == self.mapa[1][1] == self.mapa[2][1] == self.vez.peca or \
               self.mapa[0][2] == self.mapa[1][2] == self.mapa[2][2] == self.vez.peca

    def verifica_diagonais(self):
        return self.mapa[0][0] == self.mapa[1][1] == self.mapa[2][2] == self.vez.peca or \
               self.mapa[2][0] == self.mapa[1][1] == self.mapa[0][2] == self.vez.peca

    def isFinished(self):
        return self.ganhador is not None

    def avaliar(self):
        if self.verifica_linhas() or self.verifica_colunas() or self.verifica_diagonais():
            self.ganhador = self.vez
        elif self.vazio == 0:
            self.ganhador = Jogador.VELHA
