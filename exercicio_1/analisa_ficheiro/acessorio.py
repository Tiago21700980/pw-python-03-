import os

def pede_nome():
    file_name = input("Introduza nome do ficheiro de texto\n")
    while not os.path.exists(file_name):
        print('file not found\n')
        file_name = input("Introduza nome do ficheiro de texto\n")
    else:
        print('file exists\n')
        return file_name


def gera_nome(file_name):
    name = file_name.split(".txt")[0]
    return name + '.json'

'''#pede_nome()
print('Ola')
print(gera_nome('james.txt'))'''