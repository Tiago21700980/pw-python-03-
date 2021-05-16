import os
import csv
from matplotlib import pyplot as plt


def pede_pasta():
    while not os.path.isdir(dir_path := input("Deve inserir o caminho de uma pasta para o programa analisar")):
        pass
    return dir_path


def faz_calculos(dir_path):
    # contabiliza a quantidade de ficheiros e volume total ocupado em kBytes
    info = {}
    for name in os.listdir(dir_path):
        full_path = os.path.join(dir_path, name) # returns o full path da pasta/ficheiro que ele esta a ler
        if os.path.isdir(full_path):  # read directory recursively
            temp_info = faz_calculos(full_path)
            for ext in set(info) & set(temp_info):  # extensions already saved
                info[ext]['volume'] += temp_info[ext]['volume']
                info[ext]['quantidade'] += temp_info[ext]['quantidade']
            for ext in set(temp_info) - set(info):  # new extensions
                info[ext] = {'volume': temp_info[ext]['volume'], 'quantidade': temp_info[ext]['quantidade']}
        elif os.path.isfile(full_path):  # add file info
            ext = full_path.split(".")[-1]
            if ext in info:
                info[ext]['volume'] += os.path.getsize(full_path)
                info[ext]['quantidade'] += 1
            else:
                info[ext] = {'volume': os.path.getsize(full_path), 'quantidade': 1}
    return info

def guarda_resultados(dir_path):
    filename = dir_path.split('\\')[-1] + '.csv'
    file = open(filename, 'w')
    file.write('Extensao,Quantidade,Tamanho[kByte]\n')
    for ext in (info := faz_calculos(dir_path)):
        file.write(f'{ext},{info[ext]["volume"]},{info[ext]["quantidade"]}\n')
    file.close()
    print(f'Os resultados foram guardados no ficheiro `{filename}`')


def faz_grafico_queijos(titulo, lista_chaves, lista_valores):
    plt.pie(lista_valores, labels=lista_chaves, autopct='%1.0f%%')
    plt.title(titulo)
    plt.show()


def faz_grafico_barras(titulo, lista_chaves, lista_valores):
    plt.bar(lista_chaves, lista_valores)
    plt.title(titulo)
    plt.show()

def choose_graphic(title, dir_info):
    while (graphic_type := input('Insira "queijos" ou "barras" consoante o gráfico que quiser obter: ')) not in ['queijos', 'barras']:
        print('Invalid input')
    while (graphic_info := input('Insira "volume" ou "quantidade" consoante a informação que quiser obter: ')) not in ['volume', 'quantidade']:
        print('Invalid input')
    if graphic_type == 'queijos':
        faz_grafico_queijos(title, dir_info.keys(), [x[graphic_info] for x in dir_info.values()])
    else:
        faz_grafico_barras(title, dir_info.keys(), [x[graphic_info] for x in dir_info.values()])


folder_path_test = "C:/Users/Ethys/Desktop/NOTESCOLA/PawnStrings/"
print(faz_calculos(folder_path_test))
guarda_resultados(folder_path_test)
choose_graphic('Directory Info', faz_calculos(folder_path_test))