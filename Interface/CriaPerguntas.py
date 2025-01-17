from customtkinter import *
from Interface.CoresInterface import *

#cria perguntas e retorna o valor digitado pelo usuário
def criaPerguntas(titulo: str, texto: str, funçao):
    caixaPergunta = CTkInputDialog(title=titulo, text=texto, fg_color=corInterfacePrincipal, entry_fg_color=corFundoFrame, entry_border_color=corBordas, entry_text_color=corFonte)
    caixaPergunta.transient()
    valorObtido = caixaPergunta.get_input()
    return funçao(valorObtido)

#mesma coisa do de cima, só que sem a verificaçao de alguma funçao no final
def criaPerguntasSemFunçao(titulo: str, texto: str):
    caixaPergunta = CTkInputDialog(title=titulo, text=texto, fg_color=corInterfacePrincipal, entry_fg_color=corFundoFrame, entry_border_color=corBordas, entry_text_color=corFonte)
    valorObtido = caixaPergunta.get_input()
    return valorObtido