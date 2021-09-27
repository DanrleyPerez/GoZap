"""
Webscraper
"""


from selenium import webdriver
from time import sleep
import docman

list = []
lista2 = []
lista3 = []


def get_fire():
    global gecko
    gecko = webdriver.Firefox(executable_path='../okzap/gecko/geckodriver.exe')
    global strelemgecko
    elemgecko = gecko.get("https:/web.whatsapp.com")
    if elemgecko:
        return True

j = 0

from capturedata import retorna_opcoes
from bancozap import conexao
from sqlite3 import Error

conexao_banco_atual =conexao('conversa1')

position1 = ''
position2 = ''


def escolhe_resposta(bank, posicion1,posicion2):
    try:

        lista_tabela_escolhida_mod = retorna_opcoes(conexao(bank), """SELECT * from A"""+posicion1+posicion2)

        return lista_tabela_escolhida_mod
    except Error as er:
        print(er)


vezes = 0
armazena = []


def capta_ultima_mensagem():
    lista3 = gecko.find_elements_by_xpath("//div[@class='_33LGR']//div[@class='_2wUmf message-in focusable-list-item']//span[@class='i0jNr selectable-text copyable-text']")
    k=0
    for e in lista3:
        k = k + 1
        if k == len(lista3):
            texto1 = e.text

            return str(texto1)


def capta_penultima_mensagem_valida():
    w = 0
    r = 0

    pos_mensagem_invalida = None
    lista_mensagens = gecko.find_elements_by_xpath("//div[@class='_33LGR']//div[@class='_2wUmf message-in focusable-list-item']//span[@class='i0jNr selectable-text copyable-text']")
    lista_minhas_mensagens = gecko.find_elements_by_xpath("//div[@class='_33LGR']//div[@class='_2wUmf message-out focusable-list-item']//span[@class='i0jNr selectable-text copyable-text']")

    if lista_minhas_mensagens != []:
        for e in lista_minhas_mensagens:
            if e.text == 'Resposta Invalida':
                pos_mensagem_invalida = w
            w = w + 1

    if pos_mensagem_invalida != None:
        for j in lista_mensagens:
            if r == pos_mensagem_invalida:
                lista_mensagens.remove(j)

            r = r + 1
    k = 0

    penultima = len(lista_mensagens)-1

    for i in lista_mensagens:
        k = k + 1
        if k == penultima:
            texto2 = i.text
            return texto2


def capta_ultima_mensagem_minha_valida():
    lista_ultima_mensagem_minha_valida = gecko.find_elements_by_xpath("//div[@class='_33LGR']//div[@class='_2wUmf message-out focusable-list-item']//span[@class='i0jNr selectable-text copyable-text']")
    k = 0

    for e in lista_ultima_mensagem_minha_valida:

        if e.text == 'Resposta Invalida':
            pos_ultima_valida = k - 1

            ultima = lista_ultima_mensagem_minha_valida[pos_ultima_valida].text

            return ultima
        else:

            ultima = lista_ultima_mensagem_minha_valida[k].text
            if k+1 == len(lista_ultima_mensagem_minha_valida):
                return ultima

        k = k + 1


def transforma_ultima_mensagem_em_lista():

    lista_ultima_mensagem = []
    ultima_mensagem = capta_ultima_mensagem_minha_valida()
    for caractere in ultima_mensagem:
        if caractere == '1' or caractere == '2' or caractere == '3' or caractere == '4' or caractere == '5':
            lista_ultima_mensagem.append(caractere)

    return lista_ultima_mensagem


def cria_grupo_menu():
    options = gecko.find_elements_by_xpath("//span[@data-testid='menu']")
    options[0].click()

    novo_grupo = gecko.find_element_by_xpath("//div[@class='o--vV wGJyi']//div[@aria-label='Novo grupo']")
    novo_grupo.click()

    pesquisa_contat = gecko.find_element_by_xpath("//input[@class='_1x9wV copyable-text selectable-text']")
    pesquisa_contat.send_keys("Danrley")

    contato = gecko.find_element_by_xpath("//div[@class='_3OvU8']")
    contato.click()

    go = gecko.find_element_by_xpath("//span[@data-testid='arrow-forward']")
    go.click()

    nome_grupo = gecko.find_element_by_xpath("//div[@class='_13NKt copyable-text selectable-text']")
    nome_grupo.send_keys("menu")

    ok_grupo = gecko.find_element_by_xpath("//span[@data-testid='checkmark-medium']")
    ok_grupo.click()

    sleep(3)
    dados_grupo = gecko.find_element_by_xpath("//div[@class='_24-Ff']")
    dados_grupo.click()

    lateral_grupo = gecko.find_element_by_xpath("//div[@class='_3Bc7H KPJpj']")
    gecko.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight', lateral_grupo)
    sleep(2)
    contato_a_remover = gecko.find_elements_by_xpath("//div[@class='_3Bc7H KPJpj']//div[@class='_3uIPm WYyr1']//div[@class='_3m_Xw']")
    action = webdriver.ActionChains(gecko)
    action.context_click(contato_a_remover[0]).perform()
    sleep(2)
    remover = gecko.find_elements_by_xpath("//div[@class='_2oldI dJxPU']")
    remover[1].click()

    confirmar_remocao = gecko.find_element_by_xpath("//div[@class='_20C5O _2Zdgs']")
    confirmar_remocao.click()

    sleep(10)


def volta_pro_menu():
    try:
        menu = gecko.find_element_by_xpath("//div[@class='_3uIPm WYyr1']//div[@class='_2nY6U']//span[@title='menu']")
        menu.click()

    except:
        menu = gecko.find_element_by_xpath("//div[@class='_3uIPm WYyr1']//div[@class='_2nY6U']//span[@title='menu']")

        try:
            menu.click()
        except:
            cria_grupo_menu()


def page_up():
    try:
        opened_window = gecko.find_element_by_xpath("//div[@class='_33LGR']")
        gecko.execute_script('arguments[0].scrollTop = arguments[0].scrollTop - arguments[0].offsetHeight', opened_window)
    except:
        pass


def encerrar(texto, nmr, banco):
    try:
        conversa_a_encerrar = gecko.find_element_by_xpath("""//div[@class='ldL67 _2i3T7 _191H_']//div[@class='_3m_Xw']//div[@class='_37FrU']//span[text()='"""+nmr+"""']""")
        conversa_a_encerrar.click()
        lista_respostas1 = []
        p = 0
        k = 0

        if nmr == '7':
            elemento = gecko.find_element_by_xpath("//div[@class='ldL67 _3sh5K']//div[@class='_1SEwr']//div[@class='_13NKt copyable-text selectable-text']")

            texto9 = texto

            elemento.send_keys(texto9)
            elementoclick = gecko.find_element_by_xpath("//button[@class='_4sWnG']")
            elementoclick.click()
            sleep(3)
            mais_opcoes = gecko.find_elements_by_xpath("//div[@title='Mais opções']")

            for t in mais_opcoes:
                p = p + 1
                if p == 2:
                    t.click()
                    limpar= gecko.find_element_by_xpath("//div[@aria-label='Limpar mensagens']")
                    limpar.click()
                    certeza = gecko.find_element_by_xpath("//div[@class='_20C5O _2Zdgs']")
                    certeza.click()
                    sleep(2)

        if nmr == '6':

            mais_opcoes = gecko.find_elements_by_xpath("//div[@title='Mais opções']")

            for t in mais_opcoes:
                p = p + 1
                if p == 2:
                    t.click()
                    limpar = gecko.find_element_by_xpath("//div[@aria-label='Limpar mensagens']")
                    limpar.click()
                    certeza = gecko.find_element_by_xpath("//div[@class='_20C5O _2Zdgs']")
                    certeza.click()
                    sleep(2)

            elemento = gecko.find_element_by_xpath("//div[@class='ldL67 _3sh5K']//div[@class='_1SEwr']//div[@class='_13NKt copyable-text selectable-text']")

            texto9 = texto

            elemento.send_keys(texto9)
            elementoclick = gecko.find_element_by_xpath("//button[@class='_4sWnG']")
            elementoclick.click()
            sleep(3)

            tupla_respostas = escolhe_resposta(banco, '', '')
            for t in tupla_respostas[0]:
                lista_respostas1.append(t)
            for o in lista_respostas1:

                if o == "1. Adicionar Resposta" or o == "2. Adicionar Resposta" or o == "3. Adicionar Resposta" or o == "4. Adicionar Resposta" or o == "5. Adicionar Resposta":
                    pos = k
                    lista_respostas1[pos] = ''
                k = k + 1

            listelem3 = gecko.find_elements_by_xpath("//div[@class='_13NKt copyable-text selectable-text']")
            q = 0

            for elemento3 in listelem3:
                q = q + 1
                if q == 2:
                    elemento3.send_keys(""" """+str(lista_respostas1[0])+"""                                                                                                      """+str(lista_respostas1[1])+"""                                                                                                                """+str(lista_respostas1[2])+"""                                                                                                      """+str(lista_respostas1[3])+"""                                                                                                         """+str(lista_respostas1[4])+"""                                                                                                                    7. Para Encerrar O Atendimento""")
                    elem = gecko.find_element_by_xpath("""//button[@class='_4sWnG']""")
                    elem.click()

        volta_pro_menu()

    except:
        pass


def procura_novas_mensagens(banco):
    try:
        novas_mensagens = gecko.find_elements_by_xpath("//span[@class='_23LrM']")

        encerrar("Conversa Encerrada. Obrigado pelo contato", '7', banco)
        encerrar("Menu Principal", '6', banco)
        sleep(0.3)

        return novas_mensagens
    except:
        situacao = 'quebrar software'
        return situacao


def faz_lista_possiveis_respostas_cliente(lista_respostas_anterior):
    lista_respostas_possiveis = []
    x = 1
    for x in lista_respostas_anterior:
        lista_respostas_possiveis.append(str(x))
        x = x + 1
    return lista_respostas_possiveis


def responde_novas_mensagens(banco,client,estabelecimento):
    try:
        procura_novas_mensagens(banco)
        for ele in procura_novas_mensagens(banco):

            ele.click()
            sleep(0.5)
            global lista_respostas
            posicao_invalida = None
            lista_respostas =[]
            z = 0
            k=0
            j = 0
            menu = False
            page_up()
            listelem = gecko.find_elements_by_xpath("//div[@class='_13NKt copyable-text selectable-text']")

            list_minhas_respostas = gecko.find_elements_by_xpath("//div[@class='_1LcQK']//div[@class='_2wUmf message-out focusable-list-item']//span[@class='i0jNr selectable-text copyable-text']")

            if list_minhas_respostas != []:
                for e in list_minhas_respostas:
                    if e.text == 'Resposta Invalida':
                        posicao_invalida = z

                    z = z + 1
            try:
                resposta_dupla = gecko.find_elements_by_xpath("//div[@class='_1LcQK']//div[@class='_2wUmf _21bY5 message-out focusable-list-item']//span[@class='i0jNr selectable-text copyable-text']")
                for i in resposta_dupla:
                    if i.text == 'Menu Principal':
                        print("deu true aq ")
                        menu = True
            except:
                pass

            listnova = gecko.find_elements_by_xpath("//div[@class='_1LcQK']//div[@class='_2wUmf message-in focusable-list-item']")

            if posicao_invalida != None:
                for w in listnova:
                    if j == posicao_invalida:
                        listnova.remove(w)

                    j = j +1

            tamanholistnova = len(listnova)
            if menu == True:
                tamanholistnova = tamanholistnova + 1
            print(tamanholistnova)

            if tamanholistnova == 1:
                tupla_respostas = escolhe_resposta(banco, '', '')
                for t in tupla_respostas[0]:
                    lista_respostas.append(t)

                for o in lista_respostas:

                    if o == "1. Adicionar Resposta" or o == "2. Adicionar Resposta" or o == "3. Adicionar Resposta" or o == "4. Adicionar Resposta" or o == "5. Adicionar Resposta":
                        pos = k
                        lista_respostas[pos] = ''
                    k = k + 1
                n=0
                for elemento in listelem:
                    n = n + 1
                    if n == 2:
                                    #entrada tabela A

                        elemento.send_keys("""Bom dia! Voce fala com o *"""+estabelecimento+"""*  Escolha uma das opções para seguirmos com seu atendimento:                                                                                               """+str(lista_respostas[0])+"""                                                                                                      """+str(lista_respostas[1])+"""                                                                                                                """+str(lista_respostas[2])+"""                                                                                                      """+str(lista_respostas[3])+"""                                                                                                         """+str(lista_respostas[4])+"""                                                                                                   7. Para Encerrar O Atendimento""")

                        elem2 = gecko.find_element_by_xpath("//button[@class='_4sWnG']")
                        elem2.click()
                        volta_pro_menu()
                        sleep(2)
                                    #entrada para a tabela ab
            elif tamanholistnova == 2:

                global position1
                verificacao_mensagem = capta_ultima_mensagem()
                lista_respostas_possiveis = transforma_ultima_mensagem_em_lista()

                if verificacao_mensagem in lista_respostas_possiveis:

                    position1 = verificacao_mensagem

                    tabelaB = 'B'+str(position1)
                    tupla_respostas2 = escolhe_resposta(banco, tabelaB, '')
                    lista_respostas2 = []

                    for t in tupla_respostas2[0]:
                        lista_respostas2.append(t)

                    for o in lista_respostas2:

                        if o == "1. Adicionar Resposta" or o == "2. Adicionar Resposta" or o == "3. Adicionar Resposta" or o == "4. Adicionar Resposta" or o == "5. Adicionar Resposta":
                            pos = k
                            lista_respostas2[pos] = ''
                        k = k + 1

                    listelem1 = gecko.find_elements_by_xpath("//div[@class='_13NKt copyable-text selectable-text']")
                    l = 0

                    for elemento1 in listelem1:
                        l = l + 1
                        if l == 2:

                            elemento1.send_keys(str(lista_respostas2[0])+"""                                                                                                                     """+str(lista_respostas2[1])+"""                                                                                                   """+str(lista_respostas2[2])+"""                                                                                                                     """+str(lista_respostas2[3])+"""                                                                                                                                          """+str(lista_respostas2[4])+"""                                                                                                              6. Para Voltar Para o Menu                                                                                   7. Para Encerrar o Atendimento""")
                            elem2 = gecko.find_element_by_xpath("""//button[@class='_4sWnG']""")
                            elem2.click()

                else:

                    listelem1 = gecko.find_elements_by_xpath("//div[@class='_13NKt copyable-text selectable-text']")
                    l = 0

                    for elemento1 in listelem1:
                        l = l + 1
                        if l == 2:
                            elemento1.send_keys("Resposta Invalida")
                            elemento1.send_keys()
                            elem2 = gecko.find_element_by_xpath("""//button[@class='_4sWnG']""")
                            elem2.click()

                volta_pro_menu()
                                # entrada tabela Ax By Cz
            elif tamanholistnova == 3:
                global position2
                verificacao_penultima = capta_penultima_mensagem_valida()
                verificacao_ultima = capta_ultima_mensagem()
                lista_respostas_possiveis = transforma_ultima_mensagem_em_lista()

                if verificacao_ultima in lista_respostas_possiveis:
                    position1 = verificacao_penultima
                    position2 = verificacao_ultima
                    tabelaB = 'B'+position1
                    tabelaC = 'C'+position2
                    lista_respostas3 =[]
                    tupla_respostas3 = escolhe_resposta(banco, tabelaB, tabelaC)

                    for t in tupla_respostas3[0]:
                        lista_respostas3.append(t)
                    for o in lista_respostas3:
                        if o == "1. Adicionar Resposta" or o == "2. Adicionar Resposta" or o == "3. Adicionar Resposta" or o == "4. Adicionar Resposta" or o == "5. Adicionar Resposta":
                            pos = k
                            lista_respostas3[pos] = ''
                        k = k + 1
                    listelem2 = gecko.find_elements_by_xpath("//div[@class='_13NKt copyable-text selectable-text']")
                    t = 0
                    for elemento2 in listelem2:
                        t = t + 1
                        if t == 2:

                            elemento2.send_keys(str(lista_respostas3[0]).strip('1.')+"""                                                                                                                                       """+str(lista_respostas3[1]).strip('2.')+"""                                                                                                                                  """+str(lista_respostas3[2]).strip('3.')+"""                                                                                                                             """+str(lista_respostas3[3]).strip('4. ')+"""                                                                                                                                          """+str(lista_respostas3[4]).strip('5')+"""                                                                                                                        6. Para Voltar Para o Menu                                                                                        7. Para voltar para Encerrar o Atendimento""")
                            elem2 = gecko.find_element_by_xpath("""//button[@class='_4sWnG']""")
                            elem2.click()
                    volta_pro_menu()

                else:
                    listelem1 = gecko.find_elements_by_xpath("//div[@class='_13NKt copyable-text selectable-text']")
                    l = 0

                    for elemento1 in listelem1:
                        l = l + 1
                        if l == 2:
                            elemento1.send_keys("Resposta Invalida")
                            elemento1.send_keys()
                            elem2 = gecko.find_element_by_xpath("""//button[@class='_4sWnG']""")
                            elem2.click()

                volta_pro_menu()

            elif tamanholistnova == 4:
                listelem3 = gecko.find_elements_by_xpath("//div[@class='_13NKt copyable-text selectable-text']")
                q = 0
                for elemento3 in listelem3:
                    q = q + 1
                    if q == 2:
                        elemento3.send_keys("Obrigado! Aguarde um de nossos funcionários para ser atendido. ou digite 6 para Encerrar o atendimento")
                        elem3 = gecko.find_element_by_xpath("""//button[@class='_4sWnG']""")
                        elem3.click()
                volta_pro_menu()

            elif 8 > len(listnova) >= 5 and client == 'estressado':
                listelem3 = gecko.find_elements_by_xpath("//div[@class='_13NKt copyable-text selectable-text']")
                q = 0

                for elemento3 in listelem3:
                    q = q + 1
                    if q == 2:
                        elemento3.send_keys(" Só mais um instante e iremos atende-lo! Digite 6 para Encerrar o atendimento")
                        elem3 = gecko.find_element_by_xpath("""//button[@class='_4sWnG']""")
                        elem3.click()
                volta_pro_menu()

            else:
                volta_pro_menu()

        procura_novas_mensagens(banco)

    except:
        pass


verifica = 0


def executar_bot(bank_atual,estabelecimento):

    get_fire()
    while procura_novas_mensagens:
        if procura_novas_mensagens(bank_atual) != None and procura_novas_mensagens(bank_atual)!= 'quebrar software':
            responde_novas_mensagens(bank_atual, docman.le_txt('C:\\Gozap\\db\\cache.txt'),estabelecimento)

                    # mostra o looping
        elif procura_novas_mensagens(bank_atual) == None:
            pass
        else:
            break


if __name__=='__main__':
    executar_bot('Conversa1')