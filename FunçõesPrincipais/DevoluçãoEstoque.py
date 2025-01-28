from customtkinter import *
from Interface.CoresInterface import *
from Interface.CriaPerguntas import *
from Interface.MostraMensagem import *
from VerificaçõesDeDados.VerificaçõesCliente import *
from tinydb import Query

Cliente = Query()

#faz a devoluçao de escoras pelo id do cliente
def devolução(interface, id):
    interface.withdraw()
    janela = CTkToplevel()
    janela.resizable(False, False)
    janela.geometry("740x400")
    janela.title("Estoque")
    textoAviso = CTkLabel(janela, text="Clique em um dos botões para fazer a ação desejada!", font=("roboto", 20), text_color=corFonte)
    textoAviso.grid(padx=10, pady=13)

    janela.configure(fg_color=corInterfacePrincipal)
    frame = CTkFrame(janela, width=570, height=160, fg_color=corFundoFrame, border_color=corBordas, border_width=2)
    frame.grid(padx=25, pady=30)

    def validaDevolução(tipoCampo):
        cliente = db.get(Cliente.id == int(id))
        if(int(cliente[tipoCampo]) == 0):
            mostraMensagem("Ação não permitida", "Este cliente não alugou este produto.\n Portanto não é possível devolver ao estoque.")
            janela.deiconify()
            return False
        else:
            return True

    def funçaoDevolveProduto(perguntaDeDevoluçao: str, campoDeDevoluçao: str, mensagemFinal: str, id: int):

        try:
            quantidadeDevolvida = criaPerguntas("Pergunta", perguntaDeDevoluçao, verificaçãoNUMERO)
            devolveProdutoPorId(id, campoDeDevoluçao, int(quantidadeDevolvida))
            mostraMensagem("Ação bem-sucedida", mensagemFinal)
        except TypeError:
            interface.deiconify()
            janela.destroy()

    def funçaoDevolveEscoras():
        janela.withdraw()
        teste = validaDevolução('quantity')
        if(teste):
            pass
        else:
            return 0
        
        funçaoDevolveProduto("Digite quantas escoras serão devolvidas", 'quantity', "As escoras foram devolvidas com sucesso para o estoque!", id)
        janela.deiconify()
    
    def funçaoDevolveAndaimes():
        janela.withdraw()
        teste = validaDevolução('quantityAndaimes')
        if(teste):
            pass
        else:
            return 0
        funçaoDevolveProduto("Digite quantos andaimes serão devolvidos", 'quantityAndaimes', "Os andaimes foram devolvidos com sucesso para o estoque!", id)
        janela.deiconify()

    def funçaoDevolveBetoneiras():
        janela.withdraw()
        teste = validaDevolução('quantityBetoneira')
        if(teste):
            pass
        else:
            return 0
        funçaoDevolveProduto("Digite quantas betoneiras serão devolvidas", 'quantityBetoneira', "A(s) betoneira(s) foram devolvidos com sucesso para o estoque!", id)
        janela.deiconify()

    def funçaoDevolvePlataformas():
        janela.withdraw()
        teste = validaDevolução('quantityPlataforma')
        if(teste):
            pass
        else:
            return 0
        
        funçaoDevolveProduto("Digite quantas plataformas serão devolvidas", 'quantityPlataforma', "As plataformas foram devolvidos com sucesso para o estoque!", id)
        janela.deiconify()

    def funçaoDevolveRoldanas():
        janela.withdraw()
        teste = validaDevolução('quantityRoldana')
        if(teste):
            pass
        else:
            return 0
        
        funçaoDevolveProduto("Digite quantas roldanas serão devolvidas", 'quantityRoldana', "As roldanas foram devolvidos com sucesso para o estoque!", id)
        janela.deiconify()

    def funçaoDevolveReguladores():
        janela.withdraw()
        teste = validaDevolução('quantityRegulador')
        if(teste):
            pass
        else:
            return 0
        funçaoDevolveProduto("Digite quantos reguladores serão devolvidos", 'quantityRegulador', "Os reguladores foram devolvidos com sucesso para o estoque!", id)
        janela.deiconify()

    criaBotao(frame, "Devolução de Escoras", funçaoDevolveEscoras, 0, 0)
    criaBotao(frame, "Devolução de Andaimes", funçaoDevolveAndaimes, 0, 1)
    criaBotao(frame, "Devolução de Betoneiras", funçaoDevolveBetoneiras, 0, 2)
    criaBotao(frame, "Devolução de Plataformas", funçaoDevolvePlataformas, 1, 0)
    criaBotao(frame, "Devolução de Roldanas", funçaoDevolveRoldanas, 1, 1)
    criaBotao(frame, "Devolução de Reguladores", funçaoDevolveReguladores, 1, 2)

    def fechaJanela():
        janela.destroy()
        interface.deiconify()
    criaBotao(frame, "Voltar para o Inicio", fechaJanela, 2, 1)
    
    janela.protocol("WM_DELETE_WINDOW", fechaJanela)

    def devolveProdutoPorId(id: str, tipoDevoluçao: str, valorAlterado: int):
        cliente = db.get(Cliente.id == int(id))         
        conta = int(cliente[tipoDevoluçao]) - valorAlterado
        db.update({tipoDevoluçao: conta}, Cliente.id == int(id))