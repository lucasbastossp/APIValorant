import json
from os import linesep
import requests

print(20*'----')

nick = str(input('Digite seu nick: '))

arq = open('config.txt')
linhas = arq.readlines()
for linha in linhas:
    print(linha)

url_nicks = 'https://br1.api.riotgames.com/lol/summoner/v4/summoners/by-name/'+nick+'?api_key='+linha

r = requests.get(url_nicks)
todos = json.loads(r.content)

print(type(todos))

print(todos)


print('Deseja fazer outra escolha? \n [1] Sim \n [2] Não ')

contador = 0
while contador == 0:
    escolha = int(input('Digite 1 ou 2: '))
    if escolha == 1:
        
        print('Digite outro Nick: ')
        arq= open('config.txt')
        linhas = arq.readlines()
        for linha in linhas:
            print(linha)
        url_nicks = 'https://br1.api.riotgames.com/lol/summoner/v4/summoners/by-name/'+nick+'?api_key='+linha

        r = requests.get(url_nicks)
        todos = json.loads(r.content)
        print(type(todos))
        print(todos)
    
    
    
    else:
        print('Programa encerrado!') 
        break