from tinydb import TinyDB
db = TinyDB('DB.json')

def mostraEstoqueDisponivel(estoque: int, campo: str):
    estoqueCampo = 0
    el = db.all()
    for i in range(len(db)):
        estoqueProdutos = el[i]
        estoqueCampo += int(estoqueProdutos[campo])
    contaEstoque = estoque - estoqueCampo
    return contaEstoque