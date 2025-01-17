from Interface.CriaPerguntas import criaPerguntas
from VerificaçõesDeDados.VerificaçõesEntrada import verificaçãoNUMERO

#pode ser modificado para mostrar qualquer tipo de erro no codigo 
def criaBoxDeErro(texto: str):
    resultado = criaPerguntas(f"Erro ao Alugar {texto}", f"Nao foi possivel alocar {texto} para este cliente, pois o estoque ficou vazio.\n\nDeseja continuar mesmo assim?\nDigite:\n1 - PARA SIM / 2 - PARA NAO", verificaçãoNUMERO)
    return int(resultado)