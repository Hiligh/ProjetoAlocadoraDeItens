from customtkinter import *
from Interface.CoresInterface import *
from tinydb import TinyDB, Query
from Interface.CriaBotao import *

db = TinyDB('DB.json')
Cliente = Query()

def copiaTexto(texto, interface):
    textoCopiado = texto
    interface.clipboard_clear()
    interface.clipboard_append(textoCopiado)
    interface.update()

def verInformaçõesAdicionaisDoUsuario(interface, id):
    interface.withdraw()
    set_appearance_mode("dark")
    set_default_color_theme("dark-blue")
    interfaceUsuario = CTkToplevel()
    interfaceUsuario.title("Gerenciador de Dados - LH Locações")
    interfaceUsuario.geometry("999x538")#999x538
    interfaceUsuario.configure(fg_color=corInterfacePrincipal)

    cliente = db.get(Cliente.id == int(id))

    labelTexto = CTkLabel(interfaceUsuario, text=f"Informações Adicionais do Cliente: {cliente['nome']}", font=("roboto", 20, "bold"), text_color=corFonte)
    labelTexto.grid(row=0, column=1, padx=50, pady=10, sticky='n')

    framePrincipal = CTkFrame(interfaceUsuario, width=700, height=450, fg_color=corFundoFrame, border_color=corBordas, border_width=2)
    framePrincipal.grid(row=0, column=1, padx=50, pady=5)

    nomeCliente = CTkLabel(framePrincipal, text=f"Nome do Cliente: {cliente['nome']}", font=("roboto", 20, "bold"), text_color=corFonte)
    nomeCliente.grid(row=0, column=0, padx=80, pady=15)

    labelEndereçoCliente = CTkLabel(framePrincipal, text=f"Endereço do Cliente: {cliente['addresClient']}", font=("roboto", 20, "bold"), text_color=corFonte)
    labelEndereçoCliente.grid(row=1, column=0, padx=80, pady=15)

    labelEndereçoObra = CTkLabel(framePrincipal, text=f"Endereço da Obra: {cliente['addresObra']}", font=("roboto", 20, "bold"), text_color=corFonte)
    labelEndereçoObra.grid(row=2, column=0, padx=80, pady=15)

    labelCpfCliente = CTkLabel(framePrincipal, text=f"CPF do cliente: {cliente['cpf']}", font=("roboto", 20, "bold"), text_color=corFonte)
    labelCpfCliente.grid(row=3, column=0, padx=80, pady=15)

    labelCnpjCliente = CTkLabel(framePrincipal, text=f"CNPJ do cliente: {cliente['cnpj']}", font=("roboto", 20, "bold"), text_color=corFonte)
    labelCnpjCliente.grid(row=4, column=0, padx=80, pady=15)

    labelFormaPagamento = CTkLabel(framePrincipal, text=f"Forma de Pagamento: {cliente['formPayment'].capitalize()}", font=("roboto", 20, "bold"), text_color=corFonte)
    labelFormaPagamento.grid(row=5, column=0, padx=80, pady=15)

    frameEsquerdoPrincipal = CTkFrame(interfaceUsuario, width=200, height=620, fg_color=corFundoFrame)
    frameEsquerdoPrincipal.grid(row=0, column=0, sticky='w')

    criaBotao(frameEsquerdoPrincipal, "Copia Nome do Cliente", lambda: copiaTexto(cliente['nome'], interfaceUsuario), 0, 1)

    criaBotao(frameEsquerdoPrincipal, "Copia Endereço do Cliente", lambda: copiaTexto(cliente['addresClient'], interfaceUsuario), 1, 1)

    criaBotao(frameEsquerdoPrincipal, "Copia Endereço da Obra", lambda: copiaTexto(cliente['addresObra'], interfaceUsuario), 2, 1)

    criaBotao(frameEsquerdoPrincipal, "Copia CPF do Cliente", lambda: copiaTexto(cliente['cpf'], interfaceUsuario), 3, 1)

    criaBotao(frameEsquerdoPrincipal, "Copia CNPJ do Cliente", lambda: copiaTexto(cliente['cnpj'], interfaceUsuario), 4, 1)

    def fechaJanela():
        interfaceUsuario.destroy()
        interface.deiconify()

    criaBotao(frameEsquerdoPrincipal, "Voltar para Tela Inicial", fechaJanela, 5, 1)
    interfaceUsuario.protocol("WM_DELETE_WINDOW", fechaJanela)