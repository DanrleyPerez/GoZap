import socket
import datetime
import time
import struct


def data_servidor_ntp():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.connect(('0.br.pool.ntp.org', 123))
    sock.send(b'\x1b' + 47 * b'\0')
    data = sock.recv(1024)
    TIME1970 = 2208988800
    s= ''

    if data:
        t = struct.unpack('!12I', data)[10]
        t -= TIME1970
        s = time.ctime(t)
    return s


def compara_data_sistema():
    try:
        palavra_temporaria = []
        data_servidor = data_servidor_ntp()
        lista_total = []
        cont = 0

        for letra in data_servidor:
            cont += 1
            if letra == ' ':
                lista_total.append(palavra_temporaria)
                palavra_temporaria = []
            else:
                palavra_temporaria.extend(letra)
                if cont == len(data_servidor):
                    lista_total.append(palavra_temporaria)

        frase = ''
        lista_definitiva = []

        for ele in lista_total:
            for c in ele:
                frase= frase+c
            if frase != '':
                lista_definitiva.append(frase)
            frase = ''

        meses_ano = {'Jan':'01','Feb':'02','Mar':'03','Apr':'04','May':'05','Jun':'06','Jul':'07','Aug':'08','Sep':'09','Oct':'10','Nov':'11','Dec':'12'}
        mes_servidor = meses_ano[lista_definitiva[1]]
        dia_servidor = str(lista_definitiva[2])
        ano_servidor = lista_definitiva[4]

        if len(dia_servidor) == 1:
            dia_servidor = str('0'+dia_servidor)

        data_servidor_modulada = str(ano_servidor)+'-'+str(mes_servidor)+'-'+str(dia_servidor)
        data_sistema_operacional = str(datetime.date.today())

        if data_sistema_operacional == data_servidor_modulada:
            return data_sistema_operacional, data_servidor_modulada
        else:
            return data_sistema_operacional, data_servidor_modulada

    except:
        mensagem = "Impossivel conectar a internet"
        return mensagem


print(compara_data_sistema())