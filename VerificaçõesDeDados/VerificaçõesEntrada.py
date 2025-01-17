from Interface.CriaPerguntas import *
import re

def verificaçãoNome(nome: str):
    while not re.match(r'^[a-zA-Z ]+$', nome):
        nome = criaPerguntas("Erro, o nome está errado!", "Exemplos de nomes válidos:\nLeandro de Souza\nBreno de Oliveira", verificaçãoNome)
    return nome

def verificaçãoCPF(cpf: str):
    if(cpf == ''):
        return cpf

    if(cpf.lower().lstrip().rstrip() == "n/a"):
        return cpf

    while(
        not re.match(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$', cpf) or
        bool(re.search(r"[^\d.-]", cpf)) or
        bool(re.search(r"\s", cpf))
    ):
        if(cpf.lower().lstrip().rstrip() == "n/a"):
            return cpf
        
        cpf = criaPerguntas("Erro, o CPF está errado!", "Exemplo de CPF válidos:\n192.333.493-10\nPergunta: Digite o CPF do cliente", verificaçãoCPF)
    return cpf


def verificaçãoCNPJ(cnpj: str):
    if(cnpj == ''):
        return cnpj

    if(cnpj.lower().lstrip().rstrip() == "n/a"):
        return cnpj
    
    while not re.match(r'^\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}$', cnpj):
        if(cnpj.lower().lstrip().rstrip() == "n/a"):
            return cnpj

        cnpj = criaPerguntas("Erro, o CNPJ está errado!", "Exemplo de CNPJ válidos:\n12.345.678/0001-91\nPergunta: Digite o CNPJ do cliente", verificaçãoCNPJ)
    return cnpj

def verificaçãoDATA(data: str):
    while not re.match(r'^\d{2}/\d{2}/\d{4}$', data):
        data = criaPerguntas("Erro, a data está errada!", "Exemplos de datas válidas:\n01/12/2001\n15/05/2023\nPergunta: Digite a data de vencimento do contrato", verificaçãoDATA)
    return data

def verificaçãoNUMERO(numero: str):
    if(numero == ''):
        return numero
    
    while not re.match(r'^\d+(\.\d+)?$', numero):
        numero = criaPerguntas("Erro, o valor está errado!", "tente nao colocar letras ou 0 na frente do número, ou está colocando um valor que passa do estoque\nExemplos de números válidos:\n3.50\n3", verificaçãoNUMERO)
    return numero