from pprint import pprint
import pymongo as pyM

# Conectando ao MongoDB
client = pyM.MongoClient("mongodb+srv://luisguilherme2021:ufAkK7lB4tvqqQlX@cluster0.zmee5wz.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

db = client.clientes
collection = db.bank

# Inserindo dados na coleção bank
posts = [{
    "nome" : "Luís Dias",
    "cpf": "045328932",
    "endereço": "Rua Presidente T., 24",
    "conta": "001",
    "agencia": "0001",
    "tipo" : "corrente",
    "saldo": 0
}, {
    "nome" : "Mariana Andrade",
    "cpf": "024567212",
    "endereço": "Rua Senador A., 34",
    "conta": "002",
    "agencia": "0001",
    "tipo" : "corrente",
    "saldo": 0
}, {
    "nome" : "Felipe Hugo",
    "cpf": "654582134",
    "endereço": "Rua Deputado M.",
    "conta": "003",
    "agencia": "0001",
    "tipo" : "corrente",
    "saldo": 0
}]

# Inserindo os dados na coleção bank
collection.insert_many(posts)

# Contando documentos na coleção
print("\nTotal de documentos na coleção:", collection.estimated_document_count())

# Contando documentos com agência "0001"
print("\nDocumentos com agência '0001':", collection.count_documents({"agencia": "0001"}))

# Exibindo documentos ordenados pelo nome
for post in collection.find({}).sort("nome"):
    pprint(post)

# Comando para deletar os documentos da database
# db['bank'].drop()