from oito_rainhas import Tabuleiro
'''
        Teste apenas para ver se o tabuleiro está sendo recebido corretamente
'''
def testar_retorna():
        teste = Tabuleiro([["00000100"],
            ["01000000"],
            ["00010000"],
            ["00000010"],
            ["00100000"],
            ["00000001"],
            ["00001000"],
            ["10000000"]])
        assert teste.retorna() == [[0, 0, 0, 0, 0, 1, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 1, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0]]

'''
        dando errado de proposito, mudar para 1
'''
def testar_verifica_entrada_val():

        teste = Tabuleiro([["00000100"],
            ["01000000"],
            ["00010000"],
            ["00000010"],
            ["00100000"],
            ["00000001"],
            ["00001000"],
            ["10000000"]])
        assert teste.verifica_entrada_val() == 0
        