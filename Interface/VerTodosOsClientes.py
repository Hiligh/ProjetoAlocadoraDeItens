from customtkinter import *
from Interface.CoresInterface import *
from Interface.CriaBotao import *
from tinydb import TinyDB, Query
from Interface.menuOpçõesUsuario import *
Cliente = Query()
db = TinyDB('DB.json')

def verPrazoEntrega(interface):
    interface.withdraw()
    janela = CTkToplevel()
    janela.resizable(False, False)
    janela.geometry("800x550")
    janela.title("Prazos de Vencimento")
    janela.configure(fg_color=corInterfacePrincipal)

    labelTexto = CTkLabel(janela, text=f"Digite o nome do cliente procurado no retângulo abaixo:", font=("roboto", 20), text_color=corFonte)
    labelTexto.grid(row=0, padx=10, pady=5, sticky='n')

    retanguloDeBusca = CTkEntry(janela, width=300, height=38, placeholder_text="Digite aqui o nome do cliente", corner_radius=10, fg_color=corFundoFrame, text_color=corFonte, placeholder_text_color="white", font=("roboto", 17))
    retanguloDeBusca.grid(row=1, padx=10, pady=10)

    frame = CTkScrollableFrame(janela, width=700, height=280, fg_color=corFundoFrame, border_color=corBordas, border_width=2, orientation=VERTICAL)
    frame.grid(row=3, padx=25, pady=10)

    botaoDePesquisa = CTkButton(janela, text="Pesquisar Contratos", text_color=corFonte, font=("roboto", 17), command=lambda: procurarCliente(retanguloDeBusca.get(), frame, janela), border_color=corBordas, border_width=2, fg_color=corBotao, width=150, height=30)
    botaoDePesquisa.grid(row=2, padx=10, pady=5, sticky='n')

    def fechaJanela():
        janela.destroy()
        interface.deiconify()
    criaBotao(janela, "Voltar para a janela principal", fechaJanela, 4, 0)
    janela.protocol("WM_DELETE_WINDOW", fechaJanela)

def procurarCliente(nome, frame, janela):
    for widget in janela.winfo_children():
        if isinstance(widget, CTkEntry):
            widget.delete(0, 'end')

    for widget in frame.winfo_children():
        widget.destroy()

    listaDeIds = []
    el = db.all()

    for i in range(len(db)):
        datas = el[i]
        if(nome.lower() in datas['nome'].split()[0].lower()):
            listaDeIds.append(datas['id'])
        else:
            pass

    cont = 0
    for id in listaDeIds:
        cliente = db.get(Cliente.id == int(id))
        frameDataVencimento = CTkFrame(frame, width=300, height=150, fg_color=corBotao, border_color=corBordas, border_width=2)
        frameDataVencimento.grid(row=cont, column=0, padx=20, pady=20)

        lucroTotalText = CTkLabel(frameDataVencimento, text=f"Data do vencimento: {cliente['paymentDate']}", font=("roboto", 20), text_color=corFonte)
        lucroTotalText.grid(padx=15, pady=10)

        botaoCliente = CTkButton(frame, text=f"{cliente['nome']}", text_color=corFonte, font=("roboto", 19), command=lambda id = cliente['id']: menuOpcoesUsuario(id, janela), border_color=corBordas, border_width=2, fg_color=corBotao, width=150, height=50)
        botaoCliente.grid(row=cont, column=1, padx=10, pady=20, sticky="ew")
        cont += 1