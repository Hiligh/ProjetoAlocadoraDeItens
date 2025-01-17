from Interface.MostraMensagem import *
from VerificaçõesDeDados.VerificaçõesCliente import *
from tinydb import Query

Cliente = Query()

def confirmarPagamentoContrato(interface, id):
    try:
        interface.withdraw()
        db.update({'statePayment': "Pago"}, Cliente.id == int(id))
        mostraMensagem("Açao bem-sucedida!", "O contrato foi pago com sucesso!")
        interface.deiconify()
    except TypeError:
        interface.deiconify()
        mostraMensagem("Ocorreu algum erro, tente novamente!")