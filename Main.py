from customtkinter import *
import customtkinter
from Interface.CoresInterface import *
from VerificaçõesDeDados.VerificaçõesEstoque import *
from Interface.CriaBotao import *
from FunçõesPrincipais.InsereClientes import *
from FunçõesPrincipais.AlteraClientes import *
from FunçõesPrincipais.CriaRelatorio import *
from FunçõesPrincipais.VerLucroTotal import *
from Interface.VerTodosOsClientes import *
from FunçõesPrincipais.DevoluçãoEstoque import *
from FunçõesPrincipais.ResetaBanco import *
from FunçõesPrincipais.FinalizaContrato import *
from FunçõesPrincipais.RenovarContrato import *
from FunçõesPrincipais.ConfirmarPagamento import *
from Interface.menuOpçõesUsuario import menuOpcoesUsuario
import datetime
import locale

def resetaWidgets(window):
    for widget in window.winfo_children():
        widget.destroy()

def mostraClientesNoFrame(frameTabela, interfacePrincipal):
    cont = 0
    el = db.all()
    for i in range(len(db)):
        datas = el[i]
        mesAtual = datetime.datetime.now()
        mesVencimentoContrato = datetime.datetime.strptime(datas['paymentDate'], '%d/%m/%Y')

        if(mesVencimentoContrato.month == mesAtual.month):
            corVencimento = corInterfacePrincipal
            corFonteVencimento = corFonte
            corBordaVencimento = corBordas

            if(mesVencimentoContrato.day == mesAtual.day and datas['statePayment'] == "Pendente"):
                corVencimento = "#BDAD1C"
                corFonteVencimento = "white"
                corBordaVencimento = "#FAE40F"

            elif(mesAtual.day > mesVencimentoContrato.day and datas['statePayment'] == "Pendente"):
                corVencimento = "#8F0E07"
                corFonteVencimento = "white"
                corBordaVencimento = "#EC170C"
                
            elif(mesAtual.day >= mesVencimentoContrato.day and datas['statePayment'] == "Pago" or datas['statePayment'] == "Pago"):
                corVencimento = "#0A5217"
                corFonteVencimento = "white"
                corBordaVencimento = "#14A32E"

            frameDataVencimento = CTkFrame(frameTabela, width=300, height=150, fg_color=corVencimento, border_color=corBordaVencimento, border_width=2)
            frameDataVencimento.grid(row=cont, column=0, padx=20, pady=20)

            lucroTotalText = CTkLabel(frameDataVencimento, text=f"Dia do vencimento: {mesVencimentoContrato.day}", font=("roboto", 20), text_color=corFonteVencimento)
            lucroTotalText.grid(padx=15, pady=10)

            botaoCliente = CTkButton(frameTabela, text=f"{datas['nome']}", text_color=corFonteVencimento, font=("roboto", 19), command=lambda id = datas['id']: menuOpcoesUsuario(id, interfacePrincipal), border_color=corBordaVencimento, border_width=2, fg_color=corVencimento, width=150, height=50)
            botaoCliente.grid(row=cont, column=1, padx=10, pady=20, sticky="ew")
            cont += 1
            
def main():
    locale.setlocale(locale.LC_TIME, 'pt_BR.utf8')
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("dark-blue")

    interfacePrincipal = CTk()
    interfacePrincipal.title("Gerenciador de Dados - LH Locações")
    interfacePrincipal.geometry("900x540")
    interfacePrincipal.resizable(False, False)
    interfacePrincipal.configure(fg_color=corInterfacePrincipal)

    def fechaJanela():
        interfacePrincipal.destroy()
        exit()

    interfacePrincipal.protocol("WM_DELETE_WINDOW", fechaJanela)

    frameEsquerdoPrincipal = CTkFrame(interfacePrincipal, width=200, height=620, fg_color=corFundoFrame)
    frameEsquerdoPrincipal.grid(row=0, column=0, sticky='w')

    def insereClientesEReseta():
        insereClientes(interfacePrincipal)
        resetaWidgets(frameTabela)
        mostraClientesNoFrame(frameTabela, interfacePrincipal)

    criaBotao(frameEsquerdoPrincipal, "Insere Cliente", lambda: insereClientesEReseta(), 0, 0)

    criaBotao(frameEsquerdoPrincipal, "Ver Estoque Disponível", lambda: EstoqueDisponivel(interfacePrincipal), 1, 0)

    criaBotao(frameEsquerdoPrincipal, "Lucro Total do Mes", lambda: lucroTotal(interfacePrincipal), 2, 0)

    def resetaBancoEReseta():
        resetaBanco(interfacePrincipal)
        resetaWidgets(frameTabela)
        mostraClientesNoFrame(frameTabela, interfacePrincipal)

    criaBotao(frameEsquerdoPrincipal, "Resetar Dados", lambda: resetaBancoEReseta(), 3, 0)

    criaBotao(frameEsquerdoPrincipal, "Ver Todos os Contratos", lambda: verPrazoEntrega(interfacePrincipal), 4, 0)

    def fechaJanela():
        interfacePrincipal.destroy()

    criaBotao(frameEsquerdoPrincipal, "Fechar Programa", lambda: fechaJanela(), 5, 0)

    def limpaBotaoCliente(window):
        for widget in window.winfo_children():
            widget.destroy()
        mostraClientesNoFrame(frameTabela, interfacePrincipal)

    botaoResetar = CTkButton(interfacePrincipal, text="Atualizar Valores", command=lambda: limpaBotaoCliente(frameTabela), font=("roboto", 16), border_width=2, width=150, height=40, text_color=corFonte, fg_color=corFundoFrame, border_color=corBordas)
    botaoResetar.grid(row=0, column=1, padx=80, pady=10, sticky='s')
    
    textoTabela = CTkLabel(interfacePrincipal, text=f"Contrato de clientes que vencem no mês de: {datetime.datetime.now().strftime('%B').capitalize()}", font=("roboto", 20), text_color=corFonte)
    textoTabela.grid(row=0, column=1, padx=80, sticky='n')
    
    frameTabela = CTkScrollableFrame(interfacePrincipal, width=640, height=400, fg_color=corFundoFrame, border_color=corBordas, border_width=2)
    frameTabela.grid(row=0, column=1, padx=30, pady=0)

    mostraClientesNoFrame(frameTabela, interfacePrincipal)
    interfacePrincipal.mainloop()
main()