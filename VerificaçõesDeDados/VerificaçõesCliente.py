from tinydb import TinyDB
from Interface.CoresInterface import *
from customtkinter import *
from Interface.CriaPerguntas import *
from VerificaçõesDeDados.VerificaçõesEntrada import verificaçãoNUMERO

db = TinyDB('DB.json')

def existeMultiplosContratos(nome):
    el = db.all()
    for i in range(len(db)):
        clientes = el[i]
        if(clientes['nome'].lower() == nome.lower()):
            print(clientes['id'])
    return 0

def mostraContratosMesmoCliente(cpf, interface):
    interface.withdraw()
    janela = CTkToplevel()
    janela.geometry("870x400")
    janela.title("Estoque")
    janela.configure(fg_color=corInterfacePrincipal)
    texto = CTkLabel(janela, text="Contratos feitos por esse cliente: ", font=("roboto", 20), text_color=corFonte)
    texto.grid(row=0, column=0, padx = 10, pady = 13)
    frame = CTkFrame(janela, width=500, height=250, fg_color=corFundoFrame, border_color=corBordas, border_width=2)
    frame.grid(row=1, column=0, padx = 25, pady = 30)
    
    el = db.all()
    contadorLinha = 0
    for i in range(len(db)):
        dados = el[i]
        if(cpf == dados['cpf']):
            texto = CTkLabel(frame, text=f"{dados['id']} - O Cliente {dados['nome']} alugou os seguintes produtos: \n{dados['quantity']} escoras, {dados['quantityAndaime']} andaimes, {dados['quantityBetoneira']} betoneiras, {dados['quantityPlataforma']} plataformas, {dados['quantityRoldana']} roldanas e {dados['quantityRegulador']} reguladores.\n Período de Contrato: {dados['todayDate']} a {dados['paymentDate']}\n Estado do Pagamento: {dados['statePayment']}", font=("roboto", 20), text_color=corFonte)
            texto.grid(row=contadorLinha, column=0, padx=15, pady=9)
            contadorLinha += 1

    def fechaJanela():
        janela.destroy()
    janela.protocol("WM_DELETE_WINDOW", fechaJanela)
    
    resposta = criaPerguntas("Pergunta", "Digite o número abaixo correspondente ao contrato que vai ser escolhido:", verificaçãoNUMERO)
    janela.destroy()
    return resposta