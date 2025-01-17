from Interface.CoresInterface import *
from customtkinter import *
from Interface.CriaBotao import *
from tinydb import TinyDB

db = TinyDB('DB.json')

#mostra o lucro obtido no mes por todos os alugamentos  
def lucroTotal(interface):
    interface.withdraw()
    contaLucro = 0
    el = db.all()
    for i in range(len(db)):
        pagamentoTotal = el[i]
        contaLucro += float(pagamentoTotal["paymentAmount"])

    janela = CTkToplevel()
    janela.geometry("500x200")
    janela.title("Estoque")
    janela.configure(fg_color=corInterfacePrincipal)
    frame = CTkFrame(janela, width=300, height=160, fg_color=corFundoFrame, border_color=corBordas, border_width=2)
    frame.grid(padx = 25, pady = 30)
    lucroTotalText = CTkLabel(frame, text="O lucro estimado para este mês é de {:.2f}R$".format(contaLucro), font=("roboto", 20), text_color=corFonte)
    lucroTotalText.grid(row=1, column=0, padx=5, pady=2)
    def fechaJanela():
        janela.destroy()
        interface.deiconify()
    criaBotao(frame, "Ok", fechaJanela, 2, 0)
    janela.protocol("WM_DELETE_WINDOW", fechaJanela)