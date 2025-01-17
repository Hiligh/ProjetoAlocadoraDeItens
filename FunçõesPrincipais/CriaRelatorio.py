from Interface.CriaPerguntas import *
from VerificaçõesDeDados.VerificaçõesCliente import *
from Interface.MostraMensagem import *
from tinydb import Query
import pandas as pd

Cliente = Query()

def criaRelatorio(interface, id):
    interface.withdraw()
    def formatoData(produto):
            data = {
                    "Quantidade": [produto['quantity'], 
                                produto['quantityAndaimes'], 
                                produto['quantityBetoneira'], 
                                produto['quantityPlataforma'], 
                                produto['quantityRoldana'], 
                                produto['quantityRegulador']],
                    "Preço(1 Unidade)": [produto['valueEscora'],
                                        produto['valueAndaimes'],
                                        produto['valueBetoneira'],
                                        produto['valuePlataforma'],
                                        produto['valueRoldana'],
                                        produto['valueRegulador']],
                    "Tamanho": [produto['sizeEscora'], 
                                "-", 
                                "-", 
                                produto['sizePlataforma'], 
                                "-",
                                "-"]
                }
            return data
    try:
        produto = db.get(Cliente.id == int(id))
        df = pd.DataFrame(formatoData(produto), index = ["Escora", "Andaime", "Betoneira", "Plataforma", "Roldana", "Regulador"])
        df.to_excel(f"C:\\Users\\vinic\\OneDrive\\Documentos\\Área de Trabalho\\DocumentosClientes\\RelatoriosClientes\\resumo{produto['nome']}.xlsx")
        mostraMensagem("Açao bem-sucedida!", "O resumo do contrato foi criado com sucesso!")
        interface.deiconify()
    except OSError:
        mostraMensagem("Erro!", "Não foi possível criar o relatório do cliente.")
        interface.deiconify()