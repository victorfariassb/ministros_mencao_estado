import pandas as pd

estados = ['acre|ac', 'alagoas|al', 'amapá|ap', 'amazonas|am', 'bahia|ba', 'ceará|ce', 'espírito santo|es', 'goiás|go', 'maranhão|ma', 'mato grosso|mt', 'mato grosso do sul|ms', 'goiás|go',
           'maranhão|ma', 'minas gerais|mg', 'pará|pa', 'paraíba|pb', 'paraná|pr', 'pernambuco|pe', 'piauí|pi', 'rio de janeiro|rj', 'rio grande do norte|rn', 'rio grande do sul|rs',
           'rondônia|ro', 'roraima|rr', 'santa catarina|sc', 'são paulo|sp', 'sergipe|se', 'tocantins|to', 'distrito federal|df']

def contagem_palavras_especificas(arquivo, palavras):
    """Conta como mais de um caso os termos tenham sido mencionados no mesmo tweet. Além disso, Mato Grosso conta os dados de MS"""
    dados = {}
    df = pd.read_csv(arquivo)
    df = df[['date', 'tweet']]
    df['count'] = 1
    df['tweet'] = df['tweet'].str.lower()
    for palavra in palavras:
        termo = df.loc[df['tweet'].str.contains(fr"\b({palavra})\b")].sum()
        termo['estado'] = palavra
        dados[f'{termo["estado"]}'] = termo['count']
    for i in sorted(dados, key= dados.get, reverse=True):
        print(i, dados[i])
    #contagem.to_csv(novo_doc)

print('Tarcisio')
contagem_palavras_especificas('tarcisio.csv', estados)
print('\n')
print('onyx')
contagem_palavras_especificas('onyx.csv', estados)
print('\n')

print('marinho')
contagem_palavras_especificas('marinho.csv', estados)
print('\n')

print('TerezaCrisMS')
contagem_palavras_especificas('tereza.csv', estados)
print('\n')
print('andersongtorres')
contagem_palavras_especificas('torres.csv', estados)
print('\n')
print('João Roma')
contagem_palavras_especificas('joao_roma.csv', estados)
print('\n')
print('fabiofaria')
contagem_palavras_especificas('fabiofaria.csv', estados)
