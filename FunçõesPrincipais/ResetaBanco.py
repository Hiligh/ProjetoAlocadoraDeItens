from customtkinter import *
from Interface.CoresInterface import *
from VerificaçõesDeDados.VerificaçõesEntrada import *
from Interface.CriaPerguntas import *
from Interface.MostraMensagem import *
from tinydb import TinyDB

db = TinyDB('DB.json')
devolucao = TinyDB('devoluçõesClientes.json')

#apaga todos os clientes no DB.json
def resetaBanco(interface):
    interface.withdraw()
    janela = CTkToplevel()
    janela.resizable(False, False)
    janela.geometry("470x180")
    janela.title("Estoque")
    textoAviso = CTkLabel(janela, text="Voce deseja apagar todos os clientes registrados?", font=("roboto", 20), text_color=corFonte)
    textoAviso.grid(padx = 10, pady = 5)
    janela.configure(fg_color=corInterfacePrincipal)

    frame = CTkFrame(janela, width=570, height=160, fg_color=corFundoFrame, border_color=corBordas, border_width=2)
    frame.grid(padx = 25, pady = 30)
    def escolhaAçao():
        try:
            awnser = criaPerguntas("CUIDADO!, Ação perigosa", "Voce realmente deseja apagar todos os clientes registrados?\nDigite o número que corresponde a ação:\n1 - SIM / 2 - NAO", verificaçãoNUMERO)
            if(awnser == '1'):
                db.truncate()
                devolucao.truncate()
                janela.destroy()
                interface.deiconify()
                mostraMensagem("Açao bem-sucedida", "Todos os clientes foram apagados com sucesso!")
            else:
                janela.destroy()
                interface.deiconify()
        except TypeError:
            janela.destroy()
            interface.deiconify()

    def fechaJanela():
        janela.destroy()
        interface.deiconify()
    criaBotao(frame, "Sim", escolhaAçao, 0, 0)
    criaBotao(frame, "Não", fechaJanela, 0, 1)
    janela.protocol("WM_DELETE_WINDOW", fechaJanela)