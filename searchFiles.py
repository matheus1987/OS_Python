"""


"""
import os

PATH = 0


while PATH != 'sair':
    PATH = input('Digite o diretório:\n')
    if os.path.exists(PATH):
        contadorArq = 0

        contadorDir = 0

        for root,dirs,files in os.walk(PATH):
            print('Procurando em:',root)
            for diretorio in dirs:
                contadorDir = contadorDir+1
            for Files in files:
                contadorArq = contadorArq+1

        print('Número de arquivos:',contadorArq)
        print('Número de diretórios:',contadorDir)
        print('Total:',contadorArq+contadorDir)
    else:
        print('Diretório não existe!!!')


print('Análise encerrada')