def calcula_linhas(file_name):
    soma = 0
    for line in open(file_name):
        soma += 1
    return soma

#print(calcula_linhas('james.txt'))

def calcula_carateres(file_name):
    soma = 0
    excesso = calcula_linhas(file_name) - 1

    for line in open(file_name):
        soma += len(line)

    return soma - excesso

#print(calcula_carateres('james.txt'))

def calcula_palavra_comprida(file_name):
    bigWord = ''
    for line in open(file_name):
        words = line.split(" ")
        for word in words:
            #print(word)
            if len(bigWord) < len(word):
                bigWord = word
    return bigWord

#print(calcula_palavra_comprida('james.txt'))

def calcula_ocorrencia_de_letras(file_name):
    ocorrencias = {}
    lista=[]
    for line in open(file_name):
        list1 = list(line.lower().split())
        for item in list1:
            lista[:0]=item
    for item in lista:
        ocorrencias.update({item: lista.count(item)})

    return ocorrencias
#print(calcula_ocorrencia_de_letras('james.txt'))
