# tabuleiro do jogo da velha
class Tabuleiro(object):

    def __init__(self, vez):
        self.mapa = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        self.vez = vez
        self.humano = "o"
        self.computador = "x"
        self.vazio = 9

    def imprimir(self):
        print ' {} | {} | {} '.format(self.mapa[0][0], self.mapa[0][1], self.mapa[0][2])
        print('--- --- ---')
        print ' {} | {} | {} '.format(self.mapa[1][0], self.mapa[1][1], self.mapa[1][2])
        print('--- --- ---')
        print ' {} | {} | {} '.format(self.mapa[2][0], self.mapa[2][1], self.mapa[2][2])
        print '\nvazio:', self.vazio, '\n'

    def jogar(self, lin, col):
        self.vazio -= 1
        if self.vez == 0:
            self.mapa[lin][col] = "o"
        else:
            self.mapa[lin][col] = "x"
