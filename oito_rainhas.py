'''
    Algoritmo para verificar o problema das 8 rainhas

    Consiste em dispor 8 rainhas em um tabuleiro de xadrez de forma que nenhuma possa matar outra

    O código apenas recebe uma possível solução e confere se ela é verdadeira, retornando (1) caso
    ela seja uma solução válida, 0 se for invalida, e -1 caso a entrada seja invalida, de forma que
    não tenha apenas 1s e 0s ou não se encaixe no formato de tabuleiro 8x8.
'''
class Tabuleiro:
    '''
        Classe que representa o tabuleiro de xadrez, sendo disposta no formato de lista de listas
        [[0, 0, 0, 0, 0, 0, 0, 0]
         [0, 0, 0, 0, 0, 0, 0, 0]
         [0, 0, 0, 0, 0, 0, 0, 0]
         [0, 0, 0, 0, 0, 0, 0, 0]
         [0, 0, 0, 0, 0, 0, 0, 0]
         [0, 0, 0, 0, 0, 0, 0, 0]
         [0, 0, 0, 0, 0, 0, 0, 0]
         [0, 0, 0, 0, 0, 0, 0, 0]]

        recebemos um exemplo no mesmo tipo que o dado previamente pelo professor, sendo:
        00000100
        01000000
        00010000
        00000010
        00100000
        00000001
        00001000
        10000000
    '''
    def __init__(self, tabela_completa):
        self.item = []
        for linha in tabela_completa:
            for casa in linha:
                self.item.append([int(x) for x in casa])


    '''
        Função teste apenas para retornar o a variável 
    '''
    def retorna(self):
        return 1