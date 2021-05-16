import os


def pede_pasta():
    while not os.path.isdir(dir_path := input('Este programa analisa o tipo de ficheiros presente numa pasta. Insira o caminho para uma pasta: ')):
        pass
    return dir_path


def calcula_tamanho_pasta(dir_path):
    size_sum = 0
    for name in os.listdir(dir_path):
        full_path = os.path.join(dir_path, name)
        size_sum += calcula_tamanho_pasta(full_path) if os.path.isdir(full_path) else os.path.getsize(full_path) if os.path.isfile(full_path) else 0
    return size_sum


def main():
    path = pede_pasta()
    print(f'Tamanho da pasta inserida: {calcula_tamanho_pasta(path)} bytes')


if __name__ == "__main__":
    main()