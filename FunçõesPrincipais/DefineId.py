from tinydb import TinyDB
db = TinyDB('DB.json')

def defineId():
    el = db.all()
    maiorId = 0 
    for i in range(len(db)):
        clientes = el[i]
        maiorIdAchado = int(clientes['id'])
        if(maiorId <= maiorIdAchado):
            maiorId = maiorIdAchado
    return maiorId + 1