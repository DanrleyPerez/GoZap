import os
import datetime

from kivy.app import App
from kivy.config import Config
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
from selenium import webdriver
from cryptography.fernet import Fernet

import getmac
from GoZap.capturedata import retorna_opcoes
from GoZap.capturedata import edita_opcoes
from GoZap.bancozap import conexao
from GoZap import scraper, comandos_sql, docman
import validacao
import timecheck

x = """ DOC """

KIVY_NO_ARGS = 1

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
s112 = b'6jbCQKQXw5r7tI0y8V_cKFbYnzAHyFkzRmSP6G2kDpk='


os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'
Config.set('graphics', 'resizable', False)
Config.set('graphics', 'height', '650')
Config.set('graphics', 'width', '1200')
estado = 'fechado'

# ------------------------------------REFERENTE AO BANCO DE DADOS------------------------------------

posicao1 = ''
posicao2 = ''
banco_atual = 'Conversa1'
global cliente

docman.grava_txt("calmo", 'database\\cache.txt')


def ValidacaoMac():
    enmac = str(docman.le_txt('database\\mc.txt')).strip("b''")
    chave = Fernet(s100)
    macdecryp = str(chave.decrypt(enmac.encode('UTF-8'))).strip("b''")
    mac = str(getmac.get_mac_address())
    if macdecryp == mac:
        mac1 = 'retornou true'
        return mac1
    else:
        mac1 = 'retornou false'
        return mac1


def BancoEscolhido(par_banco_atual):
    conexao_banco_atual = conexao(par_banco_atual)
    return conexao_banco_atual


lista_A = retorna_opcoes(BancoEscolhido('Conversa1'), comandos_sql.capta_opcoes_tabela_A)


def Posicao1():
    global posicao1
    if tela > 1 and posicao1 != '':
        tabela_b = "B" + str(posicao1)
        return tabela_b
    else:
        return ''


def Posicao2():
    global posicao2
    if tela == 3 and posicao2 != '':
        tabela_c = "C" + str(posicao2)
        return tabela_c
    else:
        return ''


def mostra_tabela_escolhida():
    lista_tabela_escolhida_mod = retorna_opcoes(BancoEscolhido(banco_atual), """SELECT * FROM A"""+Posicao1()+Posicao2()
                                                + """ """)
    return lista_tabela_escolhida_mod


def adiciona_opcao_tabela():
    edita_opcoes(BancoEscolhido(banco_atual), """UPDATE A"""+Posicao1()+Posicao2()+""" SET Pergunta"""
                 + str(posicao1)+"""='""" + str(posicao1)+""". """ + str(nova_resposta)+"""' """)


def adiciona_opcao_tabela2():
    edita_opcoes(BancoEscolhido(banco_atual), """UPDATE A""" + Posicao1() + Posicao2() + """ SET Pergunta"""
                 + str(posicao2) + """='""" + str(posicao2) + """. """ + str(nova_resposta2) + """' """)


def adiciona_opcao_tabela3():
    edita_opcoes(BancoEscolhido(banco_atual), """UPDATE A""" + Posicao1() + Posicao2() + """ SET Pergunta"""
                 + str(posicao3) + """='""" + str(posicao3) + """. """ + str(nova_resposta3) + """' """)


# -------------------------------REFERENTE A AUTOMAÇÃO WEB--------------------------------------------------------------


def iniciar_bot():
    global estabelecimento
    scraper.executar_bot(banco_atual, estabelecimento)


# ------------------------------REFERENTE AS OPÇÕES DE RESPOSTAS CONFIGURAVEIS------------------------------------------


class opcoes(BoxLayout):                                        # vai utilizar a lista escolhida para as opcoes.
    def __init__(self, text=''):
        super(opcoes, self).__init__()
        self.ids.top.text = text

    def retorna_posicao(self):                                  # retorna a posicao da opcao aberta
        k = 1
        ms = mostra_tabela_escolhida()
        for e in ms[0]:
            if str(e) == str(self.ids.top.text):
                global posicao1
                posicao1 = k

                return posicao1
            k = k + 1

    def retorna_texto(self):
        global texto_selecionado
        texto_selecionado = self.ids.top.text
        return self.ids.top.text

    def abre_popup(self):
        popedit()

    def proxima_tela(self):
         global tela
         tela = tela + 1


class opcoes2(BoxLayout):                                       # vai utilizar a lista escolhida para as opcoes.
    def __init__(self, text='', **kwargs):
        super(opcoes2, self).__init__(**kwargs)
        self.ids.top.text = text

    def retorna_posicao(self):                                  # retorna a posicao da opcao aberta
        k = 1
        ms = mostra_tabela_escolhida()
        for e in ms[0]:
            if str(e) == str(self.ids.top.text):
                global posicao2
                posicao2 = k
                return posicao2
            else:
                pass
            k = k + 1

    def retorna_texto(self):
        global texto_selecionado2
        texto_selecionado2 = self.ids.top.text
        return self.ids.top.text

    def abre_popup(self):
        popedit2()

    def retorna_tela(self):
        global tela
        return tela

    def proxima_tela(self):
        global tela
        tela = tela+1


class opcoes3(BoxLayout):                                      # vai utilizar a lista escolhida para as opcoes.
    def __init__(self, text='', **kwargs):
        super(opcoes3, self).__init__(**kwargs)
        self.ids.top.text = text

    def retorna_posicao(self):                                 # retorna a posicao da opcao aberta
        k = 1
        ms = mostra_tabela_escolhida()
        for e in ms[0]:
            if str(e) == str(self.ids.top.text):
                global posicao3
                posicao3 = k
                return posicao3
            k = k + 1

    def retorna_texto(self):
        global texto_selecionado3
        texto_selecionado3 = self.ids.top.text
        return texto_selecionado3

    def abre_popup(self):
        popedit3()

    def retorna_tela(self):
         global tela
         return tela


# ---------------------------REFERENTE AO POPUP DE EDIÇÃO DAS OPÇÕES----------------------------------------------------


class popupss(BoxLayout):
    def __init__(self):
        super(popupss, self).__init__()

    def retorna_texto(self):
        global nova_resposta
        nova_resposta = self.ids.text_edit.text

        if nova_resposta == '':
            nova_resposta = 'Adicionar Resposta'
        adiciona_opcao_tabela()
        return nova_resposta

    def fecha_popup(self):
        popupWindow.dismiss()


class popupss2(BoxLayout):
    def __init__(self):
        super(popupss2, self).__init__()

    def retorna_texto(self):
        global nova_resposta2
        nova_resposta2 = self.ids.text_edit.text

        if nova_resposta2 == '':
            nova_resposta2 = 'Adicionar Resposta'
        adiciona_opcao_tabela2()
        return nova_resposta2

    def fecha_popup(self):
        popup2Window.dismiss()


class popupss3(BoxLayout):
    def __init__(self):
        super(popupss3, self).__init__()

    def retorna_texto(self):
        global nova_resposta3
        nova_resposta3 = self.ids.text_edit.text
        if nova_resposta3 == '':
            nova_resposta3 = 'Adicionar Resposta'
        adiciona_opcao_tabela3()
        return nova_resposta3

    def fecha_popup(self):
        popup3Window.dismiss()


class KeyVerify(BoxLayout):
    def __init__(self):
        super(KeyVerify, self).__init__()

    def retorna_texto(self):
        if validacao.le_texto() == 'primeira validacao':
            qte_validacoes = 0

        else:
            qte_validacoes = len(validacao.le_texto())

        skrp = validacao.sek1[qte_validacoes]
        kiu = Fernet(s112)
        se = str(kiu.decrypt(skrp)).strip("b''")
        print('senha oficial', se)
        __senha_oficial__ = se
        __senha__ = self.ids.text_senha.text

        if __senha__ == '123':
            validacao.adiciona_texto(datetime.date.today())
            self.ids.key.clear_widgets()
            self.ids.key.add_widget(Label(text='Licenca renovada por mais 30 dias!'))
            return 'mantem'
        else:
            self.ids.key.clear_widgets()
            self.ids.key.add_widget(Label(text='Senha Incorreta'))
            return 'mantem'

    def fecha_popup(self):
        popupSenhaWindow.dismiss()


class popupssConexao(BoxLayout):
    def __init__(self):
        super(popupssConexao, self).__init__()

    def fecha_popup(self):
        popupConexaoWindow.dismiss()


class popupssMac(BoxLayout):
    def __init__(self):
        super(popupssMac, self).__init__()

    def fecha_popup(self):
        popupMac.dismiss()


class popupssDataErrada(BoxLayout):
    def __init__(self):
        super(popupssDataErrada, self).__init__()

    def fecha_popup(self):
        popupDataWindow.dismiss()


class popupssEmpresa(BoxLayout):
    def __init__(self):
        super(popupssEmpresa, self).__init__()

    def retorna_nome_estabelecimento(self):
        global nome_estabelecimento
        nome_estabelecimento = self.ids.nome_estabelecimento.text
        docman.grava_txt(str(nome_estabelecimento), "database\\estabelecimento.txt")
        principal1.ids.nome_empresa.clear_widgets()
        principal1.ids.nome_empresa.add_widget(Label(text=str(nome_estabelecimento), color=(0,0,0,1)))

    def fecha_popup(self):
        popupWindowEmpresa.dismiss()


class popupssArquivoErrada(BoxLayout):
    def __init__(self):
        super(popupssArquivoErrada, self).__init__()

    def fecha_popup(self):
        popupArquivoWindow.dismiss()


def popeditsenha():
    global popupSenhaWindow
    show = KeyVerify()
    popupSenhaWindow = Popup(title="Prazo Vencido! Senha: 123", content=show,
                             size_hint=(None, None), size=(400, 200))
    popupSenhaWindow.open()


def popupMacAdress():
    global popupMac
    show = popupssMac()
    popupMac = Popup(title="Computador não Identificado", content=show,
                     size_hint=(None, None), size=(400, 200))
    popupMac.open()


def popedit():
    global popupWindow
    show = popupss()
    popupWindow = Popup(title="Texto Resposta", content=show,
                        size_hint=(None, None), size=(400, 200))
    popupWindow.open()


def popeditempresa():
    global popupWindowEmpresa
    show = popupssEmpresa()
    popupWindowEmpresa = Popup(title="Nome Empresa", content=show,
                        size_hint=(None, None), size=(400, 200))
    popupWindowEmpresa.open()


def popedit2():
    global popup2Window
    show = popupss2()
    popup2Window = Popup(title="Texto Resposta", content=show,
                         size_hint=(None, None), size=(400, 200))
    popup2Window.open()


def popedit3():
    global popup3Window
    show = popupss3()
    popup3Window = Popup(title="Texto Resposta", content=show,
                         size_hint=(None, None), size=(400, 200))
    popup3Window.open()


def sem_conexao():
    global popupConexaoWindow
    show = popupssConexao()
    popupConexaoWindow = Popup(title="Sem Conexão", content=show,
                               size_hint=(None, None), size=(400, 200))
    popupConexaoWindow.open()


def data_errada():
    global popupDataWindow
    show = popupssDataErrada()
    popupDataWindow = Popup(title="Data do Sistema Errada!", content=show,
                            size_hint=(None, None), size=(400, 200))
    popupDataWindow.open()


def arquivo_alterado():
    global popupArquivoWindow
    show = popupssArquivoErrada()
    popupArquivoWindow = Popup(title="Arquivo Alterado", content=show,
                               size_hint=(None, None), size=(400, 200))
    popupArquivoWindow.open()


# ----------------------------------------------------------------------------------------------------------------------

# ------------------------------------------TELAS ----------------------------------------------------------------------


class principal(Screen):
    def __init__(self):
        super(principal, self).__init__()
        global tela
        global estado
        global helpe
        global estabelecimento
        estabelecimento = docman.le_txt("database\\estabelecimento.txt")
        if estabelecimento:
            self.ids.nome_empresa.clear_widgets()
            self.ids.nome_empresa.add_widget(Label(text=str(estabelecimento), color=(0, 0, 0, 1)))

        estado = 'fechado'
        helpe = Ajuda()
        tela = 1
        ms = mostra_tabela_escolhida()
        texto_titulo_conversa = banco_atual[:8] + ' ' + banco_atual[8:]
        self.ids.titulo_conversa.add_widget(Label(text=texto_titulo_conversa, color=(0, 0, 0, 1)))

        if ms:
            for ele in ms[0]:
                if ele!= None:
                    self.ids.boxc1.add_widget(opcoes(text=str(ele)))
                else:
                    self.ids.boxc1.add_widget(opcoes(text="Adicionar Opção de Resposta"))
        else:
            for e in range(5):
                self.ids.boxc1.add_widget(opcoes(text="Adicionar Opção de Resposta"))

    def tela_senha(self):
        self.add_widget(KeyVerify())

    def mac_errado(self):
        popupMacAdress()

    def redimensionar(self):
        self.ids.a53.height = '1000sp'

    def sem_conexao(self):
        sem_conexao()

    def data_errada(self):
        data_errada()

    def arquivo_alterado(self):
        arquivo_alterado()

    def acalma_cliente(self, state):
        global cliente
        if state:
            cliente = 'estressado'
            docman.grava_txt(cliente, 'database\\cache.txt')
        else:
            cliente = 'calmo'
            docman.grava_txt(cliente, 'database\\cache.txt')

    def Help(self):
        global estado
        global helpe
        if estado == 'fechado':
            self.add_widget(helpe)
            estado = 'aberto'
            return estado
        elif estado == 'aberto':
            self.remove_widget(helpe)
            estado = 'fechado'
            return estado

    def Troca_Tela(self):
        self.manager.current = 'janela_opcoes'

    def update(self):
        ms = mostra_tabela_escolhida()
        lista_atualizada = []
        for i in range(5):
            self.ids.boxc1.clear_widgets()
        for e in ms[0]:
            if e != texto_selecionado:
                lista_atualizada.append(e)
            else:
                lista_atualizada.append(nova_resposta)
        for ele in lista_atualizada:
            self.ids.boxc1.add_widget(opcoes(text=str(ele)))

    def mudar_conversa(self):
        global posicao1
        global posicao2
        posicao1 = ''
        posicao2 = ''
        ms = mostra_tabela_escolhida()
        self.ids.titulo_conversa.clear_widgets()
        texto_titulo_conversa = banco_atual[:8]+' '+banco_atual[8:]
        self.ids.titulo_conversa.add_widget(Label(text=texto_titulo_conversa, color=(0, 0, 0, 1)))

        for p in range(5):
            self.ids.boxc1.clear_widgets()
        for e in ms[0]:
            self.ids.boxc1.add_widget(opcoes(str(e)))

    def valida_mac(self):
        pass
        #activate this if you need a mac control
        #validamac = ValidacaoMac()
        validamac = 'retornou true'
        return validamac

    def validacao_licenca(self):

        ultima_data = validacao.le_texto()

        if ultima_data == 'Arquivo Alterado':
            return 'Arquivo Alterado'
        elif ultima_data == 'primeira validacao':
            return 'primeira validacao'
        else:
            todas_validacoes = validacao.le_texto()
            ultima_validacao = todas_validacoes[len(todas_validacoes)-1]
            lista_data_separada = []
            listtemporaria = []
            contultimo = 0
            for l in ultima_validacao:
                contultimo += 1
                if l == '-':
                    lista_data_separada.append(listtemporaria)
                    listtemporaria = []
                else:
                    listtemporaria.extend(l)
                    if len(ultima_validacao) == contultimo:
                        lista_data_separada.append(listtemporaria)

            ano = ''
            mes = ''
            dia = ''

            for a in lista_data_separada[0]:
                ano = ano + a
            for m in lista_data_separada[1]:
                mes = mes + m
            for d in lista_data_separada[2]:
                dia = dia + d

            verificacao_data_servidor = timecheck.compara_data_sistema()
            print(ano,mes,dia)
            data_expiracao = validacao.data_final(datetime.date(int(ano), int(mes), int(dia)))

            if verificacao_data_servidor == 'Impossivel conectar a internet':
                return 'Impossivel'
            elif verificacao_data_servidor[0] != verificacao_data_servidor[1]:
                return 'Data errada'
            elif datetime.date.today() >= data_expiracao:
                return 'Fora Validade'
            else:
                return 'Liberado'

    def start_bot(self):
        global estabelecimento
        estabelecimento = docman.le_txt("database\\estabelecimento.txt")
        iniciar_bot()

    def setinha(self):
        if banco_atual == 'Conversa1':
            self.ids.boxcon2.clear_widgets()
            self.ids.boxcon3.clear_widgets()
            self.ids.boxcon1.clear_widgets()
            self.ids.boxcon1.add_widget(Label(text='>', color=(0, 0, 0, 1)))
        elif banco_atual == 'Conversa2':
            self.ids.boxcon1.clear_widgets()
            self.ids.boxcon3.clear_widgets()
            self.ids.boxcon2.clear_widgets()
            self.ids.boxcon2.add_widget(Label(text='>', color=(0, 0, 0, 1)))
        else:
            self.ids.boxcon1.clear_widgets()
            self.ids.boxcon2.clear_widgets()
            self.ids.boxcon3.clear_widgets()
            self.ids.boxcon3.add_widget(Label(text='>', color=(0, 0, 0, 1)))

    def retorna_banco1(self):
        global banco_atual
        banco_atual = self.ids.con1.text

    def retorna_banco2(self):
        global banco_atual
        banco_atual = self.ids.con2.text

    def retorna_banco3(self):
        global banco_atual
        banco_atual = self.ids.con3.text

    def abre_popup_senha(self):
        popeditsenha()

    def pop_nome_empresa(self):
        popeditempresa()


class janela_opcoes(Screen):
    def __init__(self):
        super(janela_opcoes, self).__init__()

    def Opcoes_telas(self):
        self.ids.titulo_conversa.clear_widgets()
        self.ids.titulo_conversa.add_widget(Label(text=texto_selecionado, color=(0, 0, 0, 1) ))
        self.ids.janela_options.clear_widgets()
        lista_tabela_escolhida = mostra_tabela_escolhida()

        if lista_tabela_escolhida:
            for ele in lista_tabela_escolhida[0]:
                if ele != None:
                    self.ids['janela_options'].add_widget(opcoes2(text=str(ele)))
                else:
                    self.ids['janela_options'].add_widget(opcoes2(text='Adicionar Opção de Resposta'))
        else:
            for t in range(5):
                self.ids['janela_options'].add_widget(opcoes2(text='Adicionar Opção de Resposta'))
        return lista_tabela_escolhida

    def voltar(self):
        global tela
        global posicao1
        tela = tela-1
        posicao1 = ''

    def update(self):
        ms = mostra_tabela_escolhida()
        lista_atualizada = []

        for i in range(5):
            self.ids.janela_options.clear_widgets()
        for e in ms[0]:
            if e != texto_selecionado2:
                lista_atualizada.append(e)
            else:
                lista_atualizada.append(nova_resposta2)
        for ele in lista_atualizada:
            self.ids.janela_options.add_widget(opcoes2(text=str(ele)))

    def setinha(self):
        if banco_atual == 'Conversa1':
            self.ids.boxcon2.clear_widgets()
            self.ids.boxcon3.clear_widgets()
            self.ids.boxcon1.clear_widgets()
            self.ids.boxcon1.add_widget(Label(text='>', color=(0, 0, 0, 1)))
        elif banco_atual == 'Conversa2':
            self.ids.boxcon1.clear_widgets()
            self.ids.boxcon3.clear_widgets()
            self.ids.boxcon2.clear_widgets()
            self.ids.boxcon2.add_widget(Label(text='>', color=(0, 0, 0, 1)))
        else:
            self.ids.boxcon1.clear_widgets()
            self.ids.boxcon2.clear_widgets()
            self.ids.boxcon3.clear_widgets()
            self.ids.boxcon3.add_widget(Label(text='>', color=(0, 0, 0, 1)))


class janela_opcoes2(Screen):
    def __init__(self):
        super().__init__()

    def Opcoes_telas2(self):
        self.ids.titulo_conversa.clear_widgets()
        self.ids.titulo_conversa.add_widget(Label(text=texto_selecionado2, color=(0, 0, 0, 1)))
        self.ids.janela_options.clear_widgets()
        lista_tabela_escolhida = mostra_tabela_escolhida()

        if lista_tabela_escolhida != []:
            for ele in lista_tabela_escolhida[0]:
                if ele != None:
                    self.ids['janela_options'].add_widget(opcoes3(text=str(ele)))
                else:
                    self.ids['janela_options'].add_widget(opcoes3(text='Adicionar Opção de Resposta'))
        else:
            for t in range(5):
                self.ids['janela_options'].add_widget(opcoes3(text='Adicionar Opção de Resposta'))
        return lista_tabela_escolhida

    def voltar2(self):
        global tela
        tela = tela - 1

    def update(self):
        ms = mostra_tabela_escolhida()
        lista_atualizada2 = []

        for i in range(5):
            self.ids.janela_options.clear_widgets()
        for e in ms[0]:
            if str(e) != str(texto_selecionado3):
                lista_atualizada2.append(e)
            else:
                lista_atualizada2.append(nova_resposta3)
        for ele in lista_atualizada2:
            self.ids.janela_options.add_widget(opcoes3(text=str(ele)))

    def setinha(self):
        if banco_atual == 'Conversa1':
            self.ids.boxcon2.clear_widgets()
            self.ids.boxcon3.clear_widgets()
            self.ids.boxcon1.clear_widgets()
            self.ids.boxcon1.add_widget(Label(text='>', color=(0, 0, 0, 1)))
        elif banco_atual == 'Conversa2':
            self.ids.boxcon1.clear_widgets()
            self.ids.boxcon3.clear_widgets()
            self.ids.boxcon2.clear_widgets()
            self.ids.boxcon2.add_widget(Label(text='>', color=(0, 0, 0, 1)))
        else:
            self.ids.boxcon1.clear_widgets()
            self.ids.boxcon2.clear_widgets()
            self.ids.boxcon3.clear_widgets()
            self.ids.boxcon3.add_widget(Label(text='>', color=(0, 0, 0, 1)))


class Ajuda(FloatLayout):
    def __init__(self):
        super(Ajuda, self).__init__()

    def video_aula(self):
        c = webdriver.Firefox(executable_path='C:\\gecko\\geckodriver.exe')
        c.get('https://www.youtube.com/watch?v=rNghDQAetuc')


# -------------------------------------CONSTRUÇÃO--APLICATIVO-----------------------------------------------------------


class CustomScreen(ScreenManager):
    def __init__(self):
        super(CustomScreen, self).__init__()
        global principal1
        principal1 = principal()
        self.add_widget(principal1)
        self.add_widget(janela_opcoes())
        self.add_widget(janela_opcoes2())


class graphics(App):
    def build(self):
        return CustomScreen()


if __name__ == "__main__":
    graphics().run()


