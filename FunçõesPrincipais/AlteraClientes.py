from tinydb import Query
from Interface.CoresInterface import *
from customtkinter import *
from Interface.CriaBotao import criaBotao
from VerificaçõesDeDados.VerificaçõesEntrada import *
from Interface.MostraMensagem import *
from Interface.CriaPerguntas import criaPerguntas
from VerificaçõesDeDados.VerificaçõesCliente import db


Cliente = Query()

#altera os valores de cada cliente pelo cpf        
def alteraClientes(interface, id):
    interface.withdraw()
    janela = CTkToplevel()
    janela.title("Janela de Alteraçoes")
    janela.geometry("940x520")#600x450
    janela.resizable(False, False)
    janela.configure(fg_color=corInterfacePrincipal)
    tituloFrame = CTkLabel(janela, text="Selecione um botao para fazer a alteraçao do campo", font=("roboto", 20), text_color=corFonte)
    tituloFrame.pack(anchor=CENTER)
    frame = CTkFrame(janela, width=500, height=470, fg_color=corFundoFrame, border_color=corBordas, border_width=2)
    frame.pack(pady=20, padx=12)

    def fazNada(valor):
        return valor

    criaBotao(frame, "Nome", lambda: alteracaoC("nome", "nome", janela, interface, verificaçãoNome, id), 0, 0)

    criaBotao(frame, "Endereço do Cliente", lambda: alteracaoC("addresClient", "Endereço do Cliente", janela, interface, fazNada, id), 0, 1)

    criaBotao(frame, "Endereço da Obra", lambda: alteracaoC("addresObra", "Endereço da Obra", janela, interface, fazNada, id), 1, 0)

    criaBotao(frame, "Valor da Escora", lambda: alteracaoC("valueEscora", "Valor da Escora", janela, interface, verificaçãoNUMERO, id), 1, 1)

    criaBotao(frame, "Tamanho da Escora", lambda: alteracaoC("sizeEscora", "Tamanho da Escora", janela, interface, verificaçãoNUMERO, id), 2, 0)

    criaBotao(frame, "Quantidade da Escora", lambda: alteracaoC("quantity", "Quantidade de Escoras", janela, interface, verificaçãoNUMERO, id), 2, 1)

    criaBotao(frame, "Forma de Pagamento", lambda: alteracaoC("formPayment", "Forma de Pagamento", janela, interface, fazNada, id), 3, 0)

    criaBotao(frame, "Quantidade de Andaimes", lambda: alteracaoC("quantityAndaime", "Quantidade de Andaimes", janela, interface, verificaçãoNUMERO, id), 3, 1)

    criaBotao(frame, "Valor do Andaime", lambda: alteracaoC("valueAndaimes", "Valor do Andaime", janela, interface, verificaçãoNUMERO, id), 4, 1)

    criaBotao(frame, "Valor da Betoneira", lambda: alteracaoC("valueBetoneira", "Valor da Betoneira", janela, interface, verificaçãoNUMERO, id), 0, 2)

    criaBotao(frame, "Quantidade de Betoneiras", lambda: alteracaoC("quantityBetoneira", "Quantidade de Betoneiras", janela, interface, verificaçãoNUMERO, id), 1, 2)

    criaBotao(frame, "Valor da Plataforma", lambda: alteracaoC("valuePlataforma", "Valor da Plataforma", janela, interface, verificaçãoNUMERO, id), 2, 2)

    criaBotao(frame, "Quantidade de Plataformas", lambda: alteracaoC("quantityPlataforma", "Quantidade de Plataformas", janela, interface, verificaçãoNUMERO, id), 3, 2)

    criaBotao(frame, "Valor da Roldana", lambda: alteracaoC("valueRoldana", "Valor da Roldana", janela, interface,verificaçãoNUMERO, id), 0, 3)

    criaBotao(frame, "Quantidade de Roldanas", lambda: alteracaoC("quantityRoldana", "Quantidade de Roldanas", janela, interface, verificaçãoNUMERO, id), 1, 3)

    criaBotao(frame, "Valor do Regulador", lambda: alteracaoC("valueRegulador", "Valor do Regulador", janela, interface, verificaçãoNUMERO, id), 2, 3)

    criaBotao(frame, "Quantidade de Reguladores", lambda: alteracaoC("quantityRegulador", "Quantidade de Reguladores", janela, interface, verificaçãoNUMERO, id), 3, 3)

    criaBotao(frame, "Data(Inicio de Período)", lambda: alteracaoC("todayDate", "Data(Inicio de Período)", janela, interface, verificaçãoDATA, id), 4, 2)

    criaBotao(frame, "Data(Final de Período)", lambda: alteracaoC("paymentDate", "Data(Final de Período)", janela, interface, verificaçãoDATA, id), 4, 3)

    def fechaJanela():
        janela.destroy()
        interface.deiconify()
    criaBotao(frame, "Voltar para Tela Inicial", fechaJanela, 4, 0)
    janela.protocol("WM_DELETE_WINDOW", fechaJanela)

#funçao que altera os valores de acordo com o campo escolhido na interface
def alteracaoC(tipoDado: str, campo: str, janela, interface, tipoVerificaçao, id: int):
    janela.iconify()
    try:
        if(tipoDado == "formPayment"):
            novoValor = criaPerguntas("Novo valor", "Digite o novo valor do {}".format(campo), tipoVerificaçao)
            if(novoValor.lower().rstrip().lstrip() == "vencimento"):
                db.update({tipoDado: novoValor.lower().rstrip().lstrip()}, Cliente.id == int(id))
                db.update({"statePayment": "Pendente"}, Cliente.id == int(id))
                mostraMensagem("Alteraçao feita com sucesso!", "O campo {} foi alterado com sucesso!".format(campo))
                interface.deiconify()
                janela.destroy()
            else:
                db.update({tipoDado: novoValor.lower().rstrip().lstrip()}, Cliente.id == int(id))
                db.update({"statePayment": "Pago"}, Cliente.id == int(id))
                mostraMensagem("Alteraçao feita com sucesso!", "O campo {} foi alterado com sucesso!".format(campo))
                interface.deiconify()
                janela.destroy()
        else:
            novoValor = criaPerguntas("Novo valor", "Digite o novo valor do {}".format(campo), tipoVerificaçao)
            db.update({tipoDado: novoValor}, Cliente.id == int(id))
            mostraMensagem("Alteraçao feita com sucesso!", "O campo {} foi alterado com sucesso!".format(campo))
            interface.deiconify()
            janela.destroy()             
    except TypeError:
        interface.deiconify()
        janela.destroy()