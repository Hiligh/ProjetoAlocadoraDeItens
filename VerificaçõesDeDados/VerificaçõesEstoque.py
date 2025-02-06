from tinydb import TinyDB
from Interface.CriaBoxDeErro import *
from customtkinter import *
from FunçõesPrincipais.ValoresProdutos import *
from Interface.CoresInterface import *
from Interface.CriaBotao import *

db = TinyDB('DB.json')

def verificaçãoEstoque(quant: int, tipo: str, tipoCampo: str):
    el = db.all()
    verificacao = 0
    for i in range(len(db)):
        tipoCampo = el[i]
        verificacao += int(tipoCampo[tipo])

    return quant - verificacao
    
def EstoqueDisponivel(interface):
    interface.withdraw()
    somaEscoras = 0
    somaAndaimes = 0
    somaBetoneiras = 0
    somaRoldanas = 0
    somaPlataformas = 0
    somaReguladores = 0
    el = db.all()
    for i in range(len(db)):
        estoque = el[i]
        somaEscoras += int(estoque['quantity'])
        somaAndaimes += int(estoque['quantityAndaime'])
        somaBetoneiras += int(estoque['quantityBetoneira'])
        somaRoldanas += int(estoque['quantityRoldana'])
        somaPlataformas += int(estoque['quantityPlataforma'])
        somaReguladores += int(estoque['quantityRegulador'])
    contaEscora = escoras - somaEscoras
    contaAndaime = andaimes - somaAndaimes;
    contaBetoneira = betoneiras - somaBetoneiras
    contaRoldana = roldanas - somaRoldanas
    contaPlataforma = plataformas - somaPlataformas
    contaRegulador = reguladores - somaReguladores

    janela = CTkToplevel()
    janela.geometry("470x500")
    janela.title("Estoque")
    janela.configure(fg_color=corInterfacePrincipal)
    frame = CTkFrame(janela, width=600, height=400, fg_color=corFundoFrame, border_color=corBordas, border_width=2)
    frame.grid(padx = 20, pady = 30)

    escorasDisponíveis = CTkLabel(frame, text="No Estoque estão disponíveis {} escoras!\n".format(contaEscora), font=("roboto", 20), text_color=corFonte)
    escorasDisponíveis.grid(row=0, column=0, padx=5, pady=5)

    andaimesDisponíveis = CTkLabel(frame, text="No Estoque estão disponíveis {} andaimes!\n".format(contaAndaime), font=("roboto", 20), text_color=corFonte)
    andaimesDisponíveis.grid(row=1, column=0, padx=5, pady=5)

    betoneirasDisponíveis = CTkLabel(frame, text="No Estoque estão disponíveis {} betoneiras!\n".format(contaBetoneira), font=("roboto", 20), text_color=corFonte)
    betoneirasDisponíveis.grid(row=2, column=0, padx=5, pady=5)

    plataformasDisponíveis = CTkLabel(frame, text="No Estoque estão disponíveis {} plataformas!\n".format(contaPlataforma), font=("roboto", 20), text_color=corFonte)
    plataformasDisponíveis.grid(row=3, column=0, padx=5, pady=5)

    roldanasDisponíveis = CTkLabel(frame, text="No Estoque estão disponíveis {} roldanas!\n".format(contaRoldana), font=("roboto", 20), text_color=corFonte)
    roldanasDisponíveis.grid(row=4, column=0, padx=5, pady=5)

    reguladoresDisponíveis = CTkLabel(frame, text="No Estoque estão disponíveis {} reguladores!\n".format(contaRegulador), font=("roboto", 20), text_color=corFonte)
    reguladoresDisponíveis.grid(row=5, column=0, padx=5, pady=5)
    
    def fechaJanela():
        janela.destroy()
        interface.deiconify()
    criaBotao(frame, "Ok", fechaJanela, 6, 0)
    janela.protocol("WM_DELETE_WINDOW", fechaJanela)