from Interface.MostraMensagem import *
from VerificaçõesDeDados.VerificaçõesCliente import *
from tinydb import Query
import pandas as pd

from FunçõesPrincipais.DevoluçãoEstoque import devolucao

Devolucao = Query()
Cliente = Query()

devolucao_table = devolucao.table("_default")

#retira o cliente do DB.json e coloca suas informaçoes principais em um arquivo .csv
def finalizaContrato(interface, id, interfacePrincipal):
    interface.withdraw()
    listaNome = []
    listaEndC = []
    listaEndO = []
    listaCpf = []
    listaCnpj = []
    try:
        dadosCliente = db.get(Cliente.id == int(id))
        listaNome.append(dadosCliente['nome'])
        listaEndC.append(dadosCliente['addresClient'])
        listaEndO.append(dadosCliente['addresObra'])
        listaCpf.append(dadosCliente['cpf'])
        listaCnpj.append(dadosCliente['cnpj'])
        db.remove(Cliente.id == int(id))

        devolucao_table.remove(Devolucao.id == int(id))
        
        mostraMensagem("Ação bem sucessida!", "Contrato foi finalizado com sucesso!\nSuas informaçoes estão no arquivo Clientes Finalizados!")

        resetaIds = 1
        
        bd = db.all()
        bdDevolucao = devolucao_table.all()
        for cliente in bd:
            db.update({'id': resetaIds}, Cliente.id == cliente['id'])
            resetaIds += 1

        resetaIds = 1

        for devolucao in bdDevolucao:
            devolucao_table.update({'id': resetaIds}, Devolucao.id == devolucao['id'])
            resetaIds += 1

        interfacePrincipal.deiconify()

    except OSError:
        mostraMensagem("Erro!", "Ocorreu algum problema na hora de salvar os dados do cliente.")
        interfacePrincipal.deiconify()