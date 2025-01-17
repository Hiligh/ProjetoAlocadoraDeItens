from customtkinter import *
from Interface.CoresInterface import *

#usado em interfaces com frame.    
def criaBotao(interface: str, nomeBotao: str, Funcao, row: int, column: int):
    botoes = CTkButton(interface, text=nomeBotao, text_color=corFonte, font=("roboto", 16), command=Funcao, border_color=corBordas, border_width=2, fg_color=corBotao, width=150, height=50)
    botoes.grid(row=row, column=column, padx=10, pady=20, sticky="ew")