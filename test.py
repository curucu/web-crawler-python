from typing import SupportsRound
from bs4 import BeautifulSoup
import requests
import csv
import json





def show_result():
    for dado in dadosGeral:
        print(dado)

def save_csv():
    arquivo = open('arquivo.csv', 'w', newline='', encoding='utf-8')
    escritor = csv.writer(arquivo)
    escritor.writerows(dadosGeral)
    arquivo.close()

def save_json():
    arquivo = open('arquivo.json', 'w', newline='',encoding='utf-8')
    json.dump(dadosGeral, arquivo, indent = 6)
    arquivo.close()



URL = "https://www.vultr.com/products/cloud-compute/#pricing"

headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"}

site = requests.get(URL, headers=headers)

soup = BeautifulSoup(site.content, 'html.parser');

# content = soup.find('div', class_ = 'pt__body')

# score = content.find_all('div', class_ = "pt__score-value h4")


counter = 1

dadosGeral = []
dadosPraUm = []
for info in soup.find_all('strong'):
    dadosPraUm.append(info.get_text())    
    if(counter % 5 == 0 and counter != 0):
        # print(info.get_text())
        dadosGeral.append(dadosPraUm[:])
        dadosPraUm.clear()
        
    
    counter += 1

opcao = 0
while opcao != 1 and opcao != 2 and opcao != 3:
    print('''Selecione uma das opções
    1 - Mostrar resultado no console
    2 - Salvar resultado em um arquivo JSON
    3 - Salvar resultado em um arquivo CSV''')
    opcao = int(input())

if opcao == 1:
    show_result()
elif opcao == 2:
    save_json()
elif opcao == 3:
    save_csv()