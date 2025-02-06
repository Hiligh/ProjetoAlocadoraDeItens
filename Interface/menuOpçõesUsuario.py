from customtkinter import *
from Interface.CoresInterface import *
from Interface.CriaBotao import *
from FunçõesPrincipais.AlteraClientes import *
from FunçõesPrincipais.ConfirmarPagamento import *
from FunçõesPrincipais.CriaRelatorio import *
from FunçõesPrincipais.DevoluçãoEstoque import *
from FunçõesPrincipais.FinalizaContrato import *
from FunçõesPrincipais.RenovarContrato import *
from Interface.verInformaçõesAdicionaisDoUsuario import *

def menuOpcoesUsuario(id, interfacePrincipal):
    try:
        interfacePrincipal.withdraw()
        set_appearance_mode("dark")
        set_default_color_theme("dark-blue")
        interfaceUsuario = CTkToplevel()
        interfaceUsuario.title("Gerenciador de Dados - LH Locações")
        interfaceUsuario.geometry("930x710")#930x710
        interfaceUsuario.configure(fg_color=corInterfacePrincipal)

        def resetarValores():
            interfaceUsuario.destroy()
            menuOpcoesUsuario(id, interfacePrincipal)

        frameEsquerdoPrincipal = CTkFrame(interfaceUsuario, width=200, height=620, fg_color=corFundoFrame)
        frameEsquerdoPrincipal.grid(row=0, column=0, sticky='w')

        criaBotao(frameEsquerdoPrincipal, "Alterar Valores", lambda: alteraClientes(interfaceUsuario, id), 0, 0)

        criaBotao(frameEsquerdoPrincipal, "Devolver Produtos", lambda: devolução(interfaceUsuario, id), 1, 0)

        criaBotao(frameEsquerdoPrincipal, "Finalizar Contrato", lambda: finalizaContrato(interfaceUsuario, id, interfacePrincipal), 2, 0)

        criaBotao(frameEsquerdoPrincipal, "Renovar Contrato", lambda: renovarContrato(interfaceUsuario, id), 3, 0)

        criaBotao(frameEsquerdoPrincipal, "Confirmar Pagamento", lambda: confirmarPagamentoContrato(interfaceUsuario, id), 4, 0)

        criaBotao(frameEsquerdoPrincipal, "Cria Relatório", lambda: criaRelatorio(interfaceUsuario, id), 5, 0)

        criaBotao(frameEsquerdoPrincipal, "Ver Informações Adicionais", lambda: verInformaçõesAdicionaisDoUsuario(interfaceUsuario, id), 6, 0)

        frameTabela = CTkFrame(interfaceUsuario, width=640, height=420, fg_color=corFundoFrame, border_color=corBordas, border_width=2)
        frameTabela.grid(row=0, column=1, padx=30, pady=0)
        
        cliente = db.get(Cliente.id == int(id))
        textoTabela = CTkLabel(interfaceUsuario, text=f"Nome do Cliente: {cliente['nome']}\n\nData de vencimento do contrato: {cliente['paymentDate']}", font=("roboto", 20), text_color=corFonte)
        textoTabela.grid(row=0, column=1, padx=80, pady=10, sticky='n')

        botaoResetar = CTkButton(interfaceUsuario, text="Atualizar Valores", command=resetarValores, font=("roboto", 16), border_width=2, width=150, height=40, text_color=corFonte, fg_color=corFundoFrame, border_color=corBordas)
        botaoResetar.grid(row=0, column=1, padx=80, pady=94, sticky='n')

        textoTabelaEmbaixo = CTkLabel(interfaceUsuario, text=f"Estado de pagamento: {cliente['statePayment']}", font=("roboto", 22), text_color=corFonte)
        textoTabelaEmbaixo.grid(row=0, column=1, padx=80, pady=40, sticky="s")

        mostraWidgetsNoFrame(frameTabela, cliente)

        def fechaJanela():
            interfaceUsuario.destroy()
            interfacePrincipal.deiconify()

        criaBotao(frameEsquerdoPrincipal, "Voltar para Tela Inicial", fechaJanela, 7, 0)
        interfaceUsuario.protocol("WM_DELETE_WINDOW", fechaJanela)
    except TypeError:
        mostraMensagem("Erro!", "Não foi possível fazer esta ação, aperte no botão Atualizar valores para tentar resolver o problema!")
        interfaceUsuario.destroy()
        interfacePrincipal.deiconify()

def mostraWidgetsNoFrame(frameTabela, cliente):
    criaFrameProduto(frameTabela, f"Quant. Escoras {cliente['sizeEscora']} Metro\n\n{cliente['quantity']}", corInterfacePrincipal, corFonte, 0, 0)

    criaFrameProduto(frameTabela, f"Quant. Andaimes {cliente['sizeAndaime']} Metro\n\n{cliente['quantityAndaime']}", corInterfacePrincipal, corFonte, 1, 0)

    criaFrameProduto(frameTabela, f"Quantidade de Betoneiras\n\n{cliente['quantityBetoneira']}", corInterfacePrincipal, corFonte, 2, 0)

    criaFrameProduto(frameTabela, f"Quantidade de Roldanas\n\n{cliente['quantityRoldana']}", corInterfacePrincipal, corFonte, 0, 1)

    criaFrameProduto(frameTabela, f"Quant. Plataformas {cliente['sizePlataforma']} Metro\n\n{cliente['quantityPlataforma']}", corInterfacePrincipal, corFonte, 1, 1)

    criaFrameProduto(frameTabela, f"Quantidade de Reguladores\n\n{cliente['quantityRegulador']}", corInterfacePrincipal, corFonte, 2, 1)

def criaFrameProduto(interface, texto, corFundo, corFonte, row, column):
    frameQuantProduto = CTkFrame(interface, width=300, height=150, fg_color=corFundo, border_color=corBordas, border_width=2)
    frameQuantProduto.grid(row=row, column=column, padx=20, pady=20)

    lucroTotalText = CTkLabel(frameQuantProduto, text=texto, font=("roboto", 22), text_color=corFonte)
    lucroTotalText.grid(padx=15, pady=10)