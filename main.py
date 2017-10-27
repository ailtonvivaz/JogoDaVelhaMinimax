#!/usr/bin/env python
# -*- coding: utf-8 -*-

from model import Jogador
from model import Tabuleiro


if __name__ == '__main__':

    tabuleiro = Tabuleiro(Jogador.HUMANO)
    tabuleiro.imprimir()

    while not tabuleiro.isFinished():

        if tabuleiro.vez == Jogador.HUMANO:
            pos = input("Digite a posição que deseja jogar (linha, coluna): ")
        else:
            print "Aguarde a jogada do computador..."
            tabuleiro.gera_filhos()
            pos = tabuleiro.prox_pos

        if isinstance(pos, tuple):
            print pos, '\n\n'
            if tabuleiro.jogar(pos[0], pos[1]):
                tabuleiro.valor = None
                tabuleiro.filhos = []
                tabuleiro.imprimir()
            else:
                print 'Posicao {} já está ocupada\n\n'.format(pos)

    print 'Ganhador foi {}'.format(tabuleiro.ganhador.peca)
