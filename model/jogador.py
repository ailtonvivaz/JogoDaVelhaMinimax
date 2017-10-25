from enum import Enum


class Jogador(Enum):
    HUMANO = ('o', -1)
    COMPUTADOR = ('x', 1)
    VELHA = ('v', 0)

    def __init__(self, peca, valor):
        self.peca = peca
        self.valor = valor

