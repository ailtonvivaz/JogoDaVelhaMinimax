#!/usr/bin/env python
# -*- coding: utf-8 -*-

from model import Jogador
from model import Tabuleiro


if __name__ == '__main__':

    tabuleiro = Tabuleiro(Jogador.COMPUTADOR, True)
    tabuleiro.imprimir()

    while not tabuleiro.isFinished():

        if tabuleiro.vez == Jogador.HUMANO:
            pos = input("Digite a posição que deseja jogar (linha, coluna): ")
        else:
            print "Aguarde a jogada do computador..."
            tabuleiro.gera_filhos()
            pos = tabuleiro.prox_pos
            print 'Total de filhos: {}'.format(tabuleiro.total_filhos)

        if isinstance(pos, tuple):
            print pos, '\n\n'
            if tabuleiro.jogar(pos[0], pos[1]):
                tabuleiro.valor = None
                tabuleiro.filhos = []
                tabuleiro.total_filhos = 0
                tabuleiro.alfa = -10
                tabuleiro.beta = 10
                tabuleiro.imprimir()
            else:
                print 'Posicao {} já está ocupada\n\n'.format(pos)

    print 'Ganhador foi {}'.format(tabuleiro.ganhador.peca)
