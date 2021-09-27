from cryptography.fernet import Fernet
import datetime
from GoZap import docman

s96 = b'8QtIYtGPAAWaWQVJiZ24nept7qAkseXLrqfjV6xptb4='
s97 = b'9WsX7EKxNugFfjBSRTaH0QTDKohJaBbrdUghwLYBrFw='
s98 = b'SRTaH0QTDKohJaBb9WsX7EKxUghwLYBrFwKxNukeofl='
s99 = b'fjBSRTaH0QohJaBbrdUghw9WsX7EKxNukeodskJhGbh='
s100 = b'9WsX7EKxNugFasdfdwvzSQTDKohJaBbrdUghwLYBrFw='
s101 = b'SRTaH0QTDKohJaBb9WsX7EKxUghwLFewdxzwWefeofl='
s102 = b'GvdsxSRTaH0QohJaBbrdUghw9WsX7EKxghfdskJhGbh='
s103 = b'9WsX7EfdredFfjBSRTaH0QTDKohJaBbrdUghwLYBrFw='
s104 = b'SRTaH0QTDKohJaBbiertERfd548sddsdwAxdNukeofl='
s105 = b'fjtthjhn0QohJaBbrdUghw9WsX7EKxNukeodskJhGbh='
s106 = b'9WsX7EKxNluilhrfghWrf1gdDF23dsbrdUghwLYBrFw='
s107 = b'SRTaH0QTDKohDVdwd2342dsFVsdf2YBrFwKxNukeofl='
s108 = b'trgtTrdfbfedewDFFEUghw9WsX7EKxNukeodskJhGbh='
s109 = b'9WsX7EKxNugFfrghrtgnED45jfew2422efghwLYBrFw='
s110 = b'6jbCQKQXw5r7tI0y8V_cKFbYnzAHyFkzRmSP6G2kDpk='
s111 = b'SRDFdswswe2434fsdGdf3dfedDVG5YBrFwKxNukeofl='

sek1 = [b'gAAAAABhE8vIBcCO4jWJiVZ0LUxjvDRMHVCQS0n4UzFS0DXDfioLevaKwNAWtVSeGvjDBMgGGN0mssovKBviWN5hxBz5Pfw6Eg==',
      b'gAAAAABhE8vI784BxYx85TOiNDSGnZns_zrdOs9BnUr-RTn8X8gm1t8M4wHgKRwyid9kX6Q4QZbs1vT9pw_X8X3su9OXW-yRnA==',
      b'gAAAAABhE8vICkmadoPw32Z8zXPfjOA7zrAms8YHmC1txb7qEn0gFkz7KUJ4skocCjGUQCAPfnzLo-fkSUgW_6ep0n04-hv6mQ==',
      b'gAAAAABhE8vIMhvgJtTzV3siuQ5AH52Jky-DkACBESB7WmXbMCBhOJHFS-cHBmEP1uEYg5ugvqEqGcHh2sybu8ep3Uonh_adAw==',
      b'gAAAAABhE8vIOms3NhwAmtdLy-K1oCeZrGUuQ28usobAfBtCf8kDPTRFXCevd4uwixIBXZETMTKhFGE7va1qW4xNx8A6k-KANw==',
      b'gAAAAABhE8vIidtM8NV3qQ1nUxZPyR7YD5I4CqMq0jDtmV3rskpCzp3wEKwOorSrcbyJsCQsCeuQh3F9Gl72tdWHT7aIvy53iQ==',
      b'gAAAAABhE8vI-_qCb7s5JAP16mjMXW4-EZCAIQ4jnQYjIynkk26m1UOVeVQ0VQheb0m2YvVMKgQUmuO9q1IkHDFNX5a3JHD-VA==',
      b'gAAAAABhE8vIw0Vw8z-MtpPy-4hCywk5Drk8YuXWcfLWZrj6i6gj4y9C2Q-qp251tOdSvS9okKxPGiu_IePexe6x_i5e27BRAw==',
      b'gAAAAABhE8vIRcmbtFWiqr5dAJbWQDQUvdboG-5ibX7HFMcS5WDrll5OPM0uJ2VX0YibPJtl71oiUN9zrN3-rnZC71KlKSwZIQ==',
      b'gAAAAABhE8vIvL49y0rZMxd9RQlv4nNlO4U8sUp10RotGnLVrNfpOgkxP2QfkKclYtF6Cimz0w9Gajwb6U6f0fESATi-FOqKxA==',
      b'gAAAAABhE8vIV4ffXgD8GJXaOMFXSYNyXbs3jVrVpTaWOUlx_cueloJ6nWJOP-EVx-anqsfTMJ-4khMgjf6jXQVaksyIdtyyQw==',
      b'gAAAAABhE8vInM112wqSsaU-1RH7-Bi8zDG7IsNqeusVr47iYz-W9QybnoB-XwJiih7AUkOJEZjujETrT8_vX_S5i6SpY82Z7A==']

ass74 = """hqowehfa,sdqWWjdasaskjfqwkefhqoowowoOjddjajOLALSD;==.DVMNASDOAJSLDFJNHSD,JFBasdffiughqweifbkashdgfoawgefuyg2uuy3gr2736rtauhygwsf76Ygagbsdyhfgqhbwuvfas5d4fa5s4d5f4a54sdf54as5d4f543524534rf5w78437JGygufjh23r7wsd74fg87srgi34ruhsdUHuhgaygsdfbgygaosuinrfg;oasdniv;alkjsndv;oaunsb;goiuabsfdovjnas'dlfvnha;ouv;alsdnvoaihsdf'gvjasd'ifa'dighq'owidgal'sdg'aiorhoaehnrg;oaidfg'adnfgadfg'hahde'gsaelthfAS'rogq'aeprtjqwebgSMGJAND'FLGA'DFNGS;JDFNGB;JKqWWDFHGISHDF/sd;ABSD/LVFBAS;DLGNH:isdFBA'SFLIDHVB<dNFV;KAJSGAqWWF'ljsndg;kasdng'absd==fKNSD'GOUASDlgvKs'IOGHAsdGJA'SGNA'SDNGALSDNGALSDINGLAISDHFG;KANSFGLIHA;DFGNAOSUGFA/SLDHNGVA'SDFIHG;ALSIDFHG;LANDF;KGJNA;KFJNGA;ELFNHGA;NG;ANSFD;BAFDS;GBAK;SJDFHBG;AWEGR;KJANBSDLJGvayBKUSHDFL;KGVHSDKLJF;GVKSDJFHGV;SJDFNVKHZKCVNnjjnsjdhsjdhsjhdjfhdskflsdksnv==gjnodubedeovmkdovidnhvjsknmdksncujbdjvnnYB3jjjYig7g==nslkdjsldjh"""
ass75 = """hqowehfa,sdqWWjdasaskjfqwkefhqoowowoOjddjajOLALSD;==.DVMNASDOAJSLDFJNHSD,JFBASDKVbjlasijdf;asjkdbaslkdnaksjdbaksdbagAAbaskdjbfasldkjvbasldkjvbasdkjva.,nsdva.m,sdnvlkasj==nv;kasbd;qkbw;euaksjdvna.,sjnbd;gaubs;fkgvjabsd;kjvba;sdjnva;sdkjlngfv;aosuinrfg;oasdniv;alkjsndv;oaunsb;goiuabsfdovjnas'dlfvnha;ouv;alsdnvoaihsdf'gvjasd'ifa'dighq'owidgal'sdg'aiorhoaehnrg;oaidfg'adnfgadfg'hahde'gsaelthfAS'rogq'aeprtjqwebgSMGJAND'FLGA'DFNGS;JDFNGB;JKqWWDFHGISHDF/sd;ABSD/LVFBAS;DLGNH:isdFBA'SFLIDHVB<dNFV;KAJSGAqWWF'ljsndg;kasdng'absd==fKNSD'GOUASDlgvKs'IOGHAsdGJA'SGNA'SDNGALSDNGALSDINGLAISDHFG;KANSFGLIHA;DFGNAOSUGFA/SLDHNGVA'SDFIHG;ALSIDFHG;LANDF;KGJNA;KFJNGA;ELFNHGA;NG;ANSFD;BAFDS;GBAK;SJDFHBG;AWEGR;KJANBSDLJGvayBKUSHDFL;KGVHSDKLJF;GVKSDJFHGV;SJDFNVKHZKCVNnjjnsjdhsjdhsjhdjfhdskflsdksnv==gjnodubedeovmkdovidnhvjsknmdksncujbdjvnnYB3jjjYig7g==nslkdjsldjh"""
ass54 = """cjt66htbbw53761rc1zzq9lo4rpxfvoqjy9zn538pegehoerxhutbq89jzz9ph75al3c34alsdjfhakjsdbckabjsdk54s5d4f5fzxXDv5dsx==sdsdfdwRdWed588841Dlsk#dkdfhxdjashuieknfhcxhjjdxkfSDfeje322k3h4u3kjhn4jgksjhdgj2hk3jldf45gjih23DSksnl-nsdgjfs@,mkfsdhjfbsk,hdjklçmnbjkhs,ljdbdkhwvjhsd#$3jbsnjd,shgwkjhdlkjhfksjbdfjyhsgdflskjdfosjndfçjsd@#@#~ldmkfgdSS44sdfSDFkhfjbhskdhfgblskdflskmdfçksjdfç444544sdfs5d4fsdf785s4d5sd8g75sd4g8g4w278324sd8g7sdg=-dfsd7fs8d854d8f7sd87gsd78f7sdgihFKHFKHBfldsfds7KIjldfgijdfss8sdojsjkndgkdsfgsfbx"""
ass55 = """cjt66htbbw53761rc1zzq9lo4rpxfvoqjy9zn538pegehoerxhutbq89jzz9ph75al3c348hrxvfj9x3yk1nmddA7r6xn4cdzugaad14g==83a2pcphtt7hmib7ow1m6mt5xy5vfpdpmxqfddA7r6xn4cdzugaad14g==kiraawk4aaxty3f692x27swo3r7jv6o14v3x4sx8dmk2in1r8smk924ym92q78gavjmt7nwv1kk3xre5fvaxjhcnyakdd356vw2w78rpytmj1fyyxu3ob2127d85cpsv74xiua2ohl2qiftwmucu9h9magkzhwnzus8egAA8fyjgin4eiy3vjnuga9ss61r7orhbrfvzbycsraz4xra==9dayhgl7mr3zjov1q56xkzekeoe1fo5glhbvhul4ezrjx8cyz3vd3korij3d68r3wkz9czmd2p5cv2j4mqlo9vrmj3qf9r4fvnosnsactj3mhsfy52w6oy3fbx"""
kq = []
kq.append(s96)
kq.append(s97)
kq.append(s98)
kq.append(s99)
kq.append(s100)
kq.append(s101)
kq.append(s102)
kq.append(s103)
kq.append(s104)
kq.append(s105)
kq.append(s106)
kq.append(s107)
kq.append(s108)
kq.append(s109)
kq.append(s110)
kq.append(s111)

chcryp = docman.le_txt('C:\\Gozap\\db\\chryp.txt').strip("b''")
chcrypenc = chcryp.encode('UTF-8')

wie = datetime.date.today()
s = 0
t = 0
ctr = kq[s]
qwer = Fernet(ctr)
pi = qwer.decrypt(chcrypenc)
she = 'ss'
sqi = ['5777', 'rttt5567', 'azxc5678', 'jhjk1817', 'jhir7777', 'mmnn0000', 'hhss4333']
pi = str(pi).strip("b''")

for po in pi:
    if t == len(sqi)+4:
        she = po
    t +=1
o = int(she)-1
strkq = str(kq[o])
exec("""elemens = str("""+strkq+""").strip("b''").encode('UTF-8')""")

c = Fernet(elemens)


def adiciona_texto(texto_adicionado):
    edit = open('database\\validacao.txt', 'a')
    texto_criptografado = c.encrypt(str(texto_adicionado).encode('UTF-8'))
    strtexto_criptografado = str(texto_criptografado).strip("b''")
    edit.write(ass75)
    edit.write(strtexto_criptografado)
    edit.close()
    print("Adicionado com Sucesso!")


def pega_faixa_assinatura(textocrypto,texto_analisado,pulo):
    contli = 0
    for p in textocrypto:
        contli += 1

    numero_loops = int(contli/945)
    inicio_data = 0
    contador = 0
    ass = ''
    todas_assinaturas = []
    u = 0

    for z in range(numero_loops):                     #looping para as assinaturas criptografadas
        fim = inicio_data + texto_analisado
        for elemento in textocrypto:
            contador += 1
            if inicio_data < contador < fim:
                ass = ass + elemento
            elif contador == fim:
                ass = ass + elemento
                u += 1
                if ass == ass75:
                    todas_assinaturas.append(ass)
                    ass = ''
        contador = 0
        inicio_data = fim + pulo
    return numero_loops, todas_assinaturas


def pega_faixa_data(textocrypto,texto_analisado,pulo):
    contli = 0
    for p in textocrypto:
        contli += 1

    numero_loops = int(contli/945)
    inicio_data = 845
    contador = 0
    ass = ''
    todas_datas = []
    u = 0

    for z in range(numero_loops):               #looping para as assinaturas criptografadas
        fim = inicio_data + texto_analisado
        for elemento in textocrypto:
            contador += 1
            if inicio_data < contador < fim:
                ass = ass + elemento
            elif contador == fim:
                ass = ass + elemento
                u += 1
                todas_datas.append(ass)
                ass = ''

        contador = 0
        inicio_data = fim + pulo

    return numero_loops, todas_datas


def le_texto():
    with open('database\\validacao.txt', 'r') as encfile:
        criptografadototal = str(encfile.read())

    assinatura_check = criptografadototal[:500]

    if assinatura_check != ass55:
        return 'Arquivo Alterado'

    lixocriptografado = criptografadototal[500:]
    an_texto = pega_faixa_assinatura(lixocriptografado,845,100)

    if len(an_texto[1]) == an_texto[0]:
        pass
    else:
        return "Arquivo Alterado"

    an_texto_data = pega_faixa_data(lixocriptografado, 100, 845)
    contador = 1
    lista_datas_descriptografadas = []

    if an_texto_data[1] == []:
        return 'primeira validacao'
    for i in an_texto_data[1]:
        contador += 1
        text_descriptografado = str(c.decrypt(i.strip("''").encode('UTF-8')).decode('UTF-8'))
        lista_datas_descriptografadas.append(text_descriptografado)
    return lista_datas_descriptografadas


def informacao_a_adicionar():
    data = input(" data a adicionar")
    adiciona_texto(data)


def data_final(date_ativacao):
    data_expiracao = date_ativacao + datetime.timedelta(31)
    return data_expiracao

