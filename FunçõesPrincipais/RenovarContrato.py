from VerificaçõesDeDados.VerificaçõesCliente import *
from Interface.CriaPerguntas import *
from VerificaçõesDeDados.VerificaçõesEntrada import verificaçãoDATA
from tinydb import Query
from datetime import date
from Interface.MostraMensagem import *
from FunçõesPrincipais.DevoluçãoEstoque import *

Cliente = Query()

def renovarContrato(interface, id):
    try:
        interface.withdraw()
        dataAtual = date.today().strftime('%d/%m/%Y')
        novoPrazo = criaPerguntas("Renovar Contrato", "Digite a nova data em que o novo contrato irá vencer:\nExemplos:\n23/09/2023\n02/05/2022", verificaçãoDATA)
        db.update({'paymentDate': novoPrazo}, Cliente.id == int(id))
        db.update({'todayDate': dataAtual}, Cliente.id == int(id))

        formaPagamento = criaPerguntasSemFunçao("Renovar Contrato", "Qual é a forma de pagamento escolhida pelo cliente?(INICIO/VENCIMENTO): ")
        if(formaPagamento.lower() == 'inicio'):
            db.update({'statePayment': "Pago"}, Cliente.id == int(id))
        else:
            db.update({'statePayment': "Pendente"}, Cliente.id == int(id))

        resposta = criaPerguntas("Renovar Contrato", "O Cliente fez alguma devoluçao?\n1 - SIM / 2 - NAO", verificaçãoNUMERO)
        if(resposta != '1'):
            interface.deiconify()
            mostraMensagem("Açao Bem-sucedida!", "O contrato foi renovado com sucesso!")
        else:
            devolução(interface, id)
        
    except TypeError:
        interface.deiconify()