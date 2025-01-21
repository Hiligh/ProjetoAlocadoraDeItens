from Interface.CriaPerguntas import *
from VerificaçõesDeDados.VerificaçõesCliente import *
from Interface.MostraMensagem import *
from tinydb import Query
import pandas as pd

Cliente = Query()

def criaRelatorio(interface, id):
    interface.withdraw()
    janela = CTkToplevel()
    janela.resizable(False, False)
    janela.geometry("740x400")
    janela.title("Relatórios")
    textoAviso = CTkLabel(janela, text="Clique em um dos botões para fazer a ação desejada!", font=("roboto", 20), text_color=corFonte)
    textoAviso.grid(padx=10, pady=13)

    janela.configure(fg_color=corInterfacePrincipal)
    frame = CTkFrame(janela, width=570, height=160, fg_color=corFundoFrame, border_color=corBordas, border_width=2)
    frame.grid(padx=25, pady=30)

    criaBotao(frame, "Devolução de Escoras", funçaoDevolveEscoras, 0, 0)