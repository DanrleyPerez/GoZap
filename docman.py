def le_txt(arq):
    arquivo = open(arq, 'r')
    texto = arquivo.read()
    return texto


def grava_txt(texto,arq):
    arquivo = open(arq,'w')
    arquivo.write(texto)
