from customtkinter import *
from Interface.CoresInterface import *
from Interface.CriaBotao import *

def mostraMensagem(titulo: str, texto: str):
    tela = CTkToplevel()
    tela.title(titulo)
    tela.geometry("570x200")
    tela.configure(fg_color=corInterfacePrincipal)
    frame = CTkFrame(tela, width=300, height=160, fg_color=corFundoFrame, border_color=corBordas, border_width=2)
    frame.grid(padx = 25, pady = 30)
    textoMensagem = CTkLabel(frame, text=texto, font=("roboto", 20), text_color=corFonte)
    textoMensagem.grid(row=0, padx=10, pady=10)
    def fechaJanela():
        tela.destroy()
    criaBotao(frame, "Ok", fechaJanela, 1, 0)