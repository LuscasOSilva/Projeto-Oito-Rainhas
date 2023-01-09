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
        return self.item

    '''
        Função que verifica se todos as colunas possuem 8 casas de altura,
        se todas as linhas tem 8 casas de largura e verifica se todos os 
        caracteres são apenas 1s e 0s
    '''
    def verifica_entrada_val(self):
        if len(self.item) != 8:
            return 0
        for linha in self.item:
            if len(linha) != 8:
                return 0
            for caracter_casa in linha:
                if caracter_casa != 0 and caracter_casa != 1:
                    return 0 
        return 1

    def verificar_solucao(self):

        '''
            1° - Vamos percorrer todas as diagonais, começando pelas bordas sempre.
            Nessa primeira etapa vamos percorrer começando pelas bordas da direita e
            de cima, percorrendo suas diagonais no sentido inferior direito.
            exemplo:

             →  →  →  →  →  →  →
            ↑0, 0, 0, 0, 0, 0, 0, 0
            ↑0, 0, 0, 0, 0, 0, 0, 0
            ↑0, 0, 0, 0, 0, 0, 0, 0
            ↑0, 0, 0, 0, 0, 0, 0, 0
            ↑0, 0, 0, 0, 0, 0, 0, 0
            ↑0, 0, 0, 0, 0, 0, 0, 0
            ↑0, 0, 0, 0, 0, 0, 0, 0
             0, 0, 0, 0, 0, 0, 0, 0
        '''
        for borda_direita in range(len(self.item)-2, 0, -1):
            soma = 0
            for indice in range(0, 7):
                soma += self.item[borda_direita+indice][indice]
                if borda_direita+indice == 7:
                    break
            if soma > 1:
                return 0

        '''
            SOMA DIAGONAL PRINCIPAL
        '''
        if sum(self.item[meio][meio] for meio in range(len(self.item))) > 1:
            return 0

        for borda_superior in range(1, len(self.item)-1):
            soma = 0
            for indice in range(0, 7):
                soma += self.item[indice][borda_superior+indice]
                if borda_superior+indice == len(self.item)-1:
                    break
            if soma > 1:
                return 0

        '''
            2° - Vamos percorrer todas as diagonais, começando pelas bordas sempre.
            Nessa segunda etapa vamos percorrer as bordas de cima e
            da esquerda, percorrendo suas diagonais no sentido inferior esquerdo.
            exemplo:

               →  →  →  →  →  →  →
            0, 0, 0, 0, 0, 0, 0, 0↓
            0, 0, 0, 0, 0, 0, 0, 0↓
            0, 0, 0, 0, 0, 0, 0, 0↓
            0, 0, 0, 0, 0, 0, 0, 0↓
            0, 0, 0, 0, 0, 0, 0, 0↓
            0, 0, 0, 0, 0, 0, 0, 0↓
            0, 0, 0, 0, 0, 0, 0, 0↓
            0, 0, 0, 0, 0, 0, 0, 0↓
        '''
        for borda_superior in range(1, len(self.item)-1):
            soma = 0
            for indice in range(0, 7):
                soma += self.item[indice][borda_superior-indice]
                if borda_superior-indice == 0 or indice == len(self.item)-1:
                    break
            if soma > 1:
                return 0

        '''
            SOMA DIAGONAL SECUNDARIA
        '''
        if sum(self.item[begin][end] for begin, end in zip(range(len(self.item)), range(len(self.item)-1, -1, -1))) > 1:
            return 0

        for borda_esquerda in range(1, len(self.item)-1):
            soma = 0
            for indice in range(0, 7):
                soma += self.item[borda_esquerda+indice][7-indice]
                if borda_esquerda+indice == len(self.item)-1:
                    break
            if soma > 1:
                return 0

        '''
            Aqui vamos verificar se existe só 1 rainha em todas as linhas e todas as colunas
        '''
        for indice1 in range(len(self.item)):
            soma_linha = 0
            soma_coluna = 0
            for indice2 in range(len(self.item)):
                soma_linha += self.item[indice1][indice2]
                soma_coluna += self.item[indice2][indice1]
            if soma_coluna > 1 or soma_linha > 1:
                return 0

        '''
            Se tudo estiver passado, retorna 1, que significa correto
        '''
        return 1
