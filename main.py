import csv
import requests
import pandas as pd
from config import URL, ARQUIVO_CSV

# Requisição para o Link do arquivo .csv
response = requests.get(URL)
print(response)

# Criando um arquivo chamado 'covid19.csv' e salvando no pc local
with open('covid19.csv', 'w', newline='\n') as novo_arquivo:
    writer = csv.writer(novo_arquivo)
    for linha in response.iter_lines():
        writer.writerow(linha.decode('utf-8').split(','))

# Abrir um arquivo .csv a partir do projeto raiz
with open(ARQUIVO_CSV) as arquivo:
    leitor_exemplo = csv.reader(arquivo)
    for linha in leitor_exemplo:
        #print(linha)
        if linha[2] == 'Brazil':
            print(f"Linha # {leitor_exemplo.line_num} {linha}")

# Usando o módulo Pandas para ler arquivo .csv
arquivo_csv = pd.read_csv(ARQUIVO_CSV, usecols=['location', 'date', 'total_cases', 'total_deaths'], index_col='date')

# Mostrando os 10 primeiros
print(arquivo_csv.head(10).to_string())

# Filtrar os dados
print(arquivo_csv.loc[(arquivo_csv.location == 'United States') & (arquivo_csv.index == '2020-06-12')])


