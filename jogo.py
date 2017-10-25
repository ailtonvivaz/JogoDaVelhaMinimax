#!/usr/bin/env python
# -*- coding: utf-8 -*-

from model import Tabuleiro
from model import Jogador

if __name__ == '__main__':
    tabuleiro = Tabuleiro(Jogador.HUMANO)

    while tabuleiro.vazio > 0:

        tabuleiro.imprimir()

        if tabuleiro.vez == Jogador.HUMANO:
            pos = input("Digite a posição que deseja jogar (linha, coluna): ")
        else:
            print "Aguarde a jogada do computador..."
            tabuleiro.gera_filhos()
            pos = tabuleiro.prox_pos

        print pos, '\n\n'
        tabuleiro.jogar(pos[0], pos[1])
