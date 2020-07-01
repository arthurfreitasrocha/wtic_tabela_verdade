from tkinter import *
from PIL import ImageTk, Image
import os

# ESSA CLASSE CONSTRÓI AS TABELAS
class Tabela:

    # CRIA A TABELA AND
    def construirTabelaAND(self, imagem_tabela):

        label_tabela = Label(self.janela, image=imagem_tabela)
        label_tabela.place(x=30, y=70)

    # CRIA A TABELA OR
    def construirTabelaOR(self, imagem_tabela):

        label_tabela = Label(self.janela, image=imagem_tabela)
        label_tabela.place(x=30, y=70)

    # CRIA A TABELA NOT
    def construirTabelaNOT(self, imagem_tabela):

        label_tabela = Label(self.janela, image=imagem_tabela)
        label_tabela.place(x=30, y=70)
        
    def __init__(self, janela):

        # INICIALIZO A VARIÁVEL JANELA
        self.janela = janela
    

# ESSA CLASSE CRIA OS RADIOBUTTONS E FAZ O CONTROLE DE QUAIS TABELAS IRÃO APARECER
class RadioButtons:

    def opcaoEscolhida(self):

        # ESSA VARIÁVEL CAPTURA O VALOR DO RADIOBUTTON, OU SEJA, A OPÇÃO ESCOLHIDA PELO USUÁRIO
        opcao_selecionada = self.opcao_selecionada.get()

        if opcao_selecionada == 1:
            
            # CRIA A TABELA AND
            tabelaAND = Tabela(self.janela)
            tabelaAND.construirTabelaAND(self.imagem_tabela_and)

        if opcao_selecionada == 2:

            # CRIA A TABELA OR
            tabelaOR = Tabela(self.janela)
            tabelaOR.construirTabelaOR(self.imagem_tabela_or)

        if opcao_selecionada == 3:

            # CRIA A TABELA NOT
            tabelaNOT = Tabela(self.janela)
            tabelaNOT.construirTabelaNOT(self.imagem_tabela_not)
        
    def construirRadiobuttons(self):
        
        # CRIO UMA VARIÁVEL QUE ARMAZENARÁ O VALOR DE CADA RADIOBUTTON
        self.opcao_selecionada = IntVar()

        # RADIOBUTTONS SENDO CRIADOS
        radio_tabela_and = Radiobutton(self.frame, text='Tabela AND', bg='deepskyblue4', fg='white', font=('arial', 10, 'bold'), variable=self.opcao_selecionada, value=1, command=self.opcaoEscolhida)
        radio_tabela_and.place(x=25, y=20)

        radio_tabela_or = Radiobutton(self.frame, text='Tabela OR', bg='deepskyblue4', fg='white', font=('arial', 10, 'bold'), variable=self.opcao_selecionada, value=2, command=self.opcaoEscolhida)
        radio_tabela_or.place(x=155, y=20)

        radio_tabela_not = Radiobutton(self.frame, text='Tabela NOT', bg='deepskyblue4', fg='white', font=('arial', 10, 'bold'), variable=self.opcao_selecionada, value=3, command=self.opcaoEscolhida)
        radio_tabela_not.place(x=275, y=20)

    def __init__(self, info_janela, imagens):
        
        # INICIALIZO AS VARIÁVEIS PASSADAS PELAS LISTAS
        self.janela = info_janela[0]
        self.frame = info_janela[1]

        self.imagem_tabela_and = imagens[0]
        self.imagem_tabela_or = imagens[1]
        self.imagem_tabela_not = imagens[2]


# ESSA CLASSE É REPONSÁVEL POR CRIAR A JANELA QUE SERÃO INICIALIZADOS OS WIDGETS
class Janela:

    def construirJanela(self):
        
        janela = Tk()

        # INICIALIZA AS IMAGENS QUE SERÃO USADAS NO PROGRAMA
        imagem_inicio = ImageTk.PhotoImage(Image.open(f"{self.diretorio_atual}\\imageminicio.png"))
        imagem_tabela_and = ImageTk.PhotoImage(Image.open(f"{self.diretorio_atual}\\tabelaand.png"))
        imagem_tabela_or = ImageTk.PhotoImage(Image.open(f"{self.diretorio_atual}\\tabelaor.png"))
        imagem_tabela_not = ImageTk.PhotoImage(Image.open(f"{self.diretorio_atual}\\tabelanot.png"))

        # CRIA O FRAME RAIZ
        frame_raiz = Frame(janela, width=400, height=300, bg='deepskyblue2')
        frame_raiz.pack(side=TOP)

        # LABEL QUE IRÁ MOSTRAR A PRIMEIRA IMAGEM
        label_tabela = Label(janela, image=imagem_inicio)
        label_tabela.place(x=30, y=70)

        # LISTAS QUE ARMAZENAM AS INFORMAÇÕES DAS JANELAS E AS IMAGENS
        info_janela = [janela, frame_raiz]
        imagens = [imagem_tabela_and, imagem_tabela_or, imagem_tabela_not]

        # CRIA OS RADIOBUTTONS
        radiobutton = RadioButtons(info_janela, imagens)
        radiobutton.construirRadiobuttons()

        # CONFIGURAÇÕES DA JANELA
        janela.iconbitmap('wtic.ico')
        janela.geometry('400x300+500+200')
        janela.resizable(width=False, height=False)
        janela.title('Tabela Verdade - WTIc Python Básico')
        janela.mainloop()

    def __init__(self):

        # ARMAZENA O DIRETÓRIO QUE O SCRIPT ESTÁ SENDO RODADO
        self.diretorio_atual = os.getcwd()


# INSTANCIAMENTO DA JANELA E CONSTRUÇÃO DA MESMA
janela = Janela()
janela.construirJanela()
