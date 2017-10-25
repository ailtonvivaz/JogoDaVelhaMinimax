#!/usr/bin/env python
# -*- coding: utf-8 -*-

from model import Tabuleiro

if __name__ == '__main__':
    tabuleiro = Tabuleiro(0)
    tabuleiro.imprimir()
    tabuleiro.jogar(2, 1)
    tabuleiro.imprimir()
