import json
import requests
from urllib.request import urlopen

print(20*'----')

arq = open('config.txt')
linhas = arq.readlines()
for linha in linhas:
    print(linha)



nick = str(input('Digite seu nick: '))


url_nicks = 'https://br1.api.riotgames.com/lol/summoner/v4/summoners/by-name/'+nick+'?api_key='+linha

r = requests.get(url_nicks)
todos = json.loads(r.content)

print('Seu nick é ' + todos['name'])
print('Seu level é ' + str(todos['summonerLevel']))
#print(type(todos))

#print(todos)


contador = 0

def buscarDadosPlayer(nick):
    url_nicks = 'https://br1.api.riotgames.com/lol/summoner/v4/summoners/by-name/'+nick+'?api_key='+linha
    r = requests.get(url_nicks)
    todos = json.loads(r.content)
    print(todos)
    print('Seu nick é ' + todos['name'])
    name = str(todos['name'])
    print('Seu level é ' + str(todos['summonerLevel']))
    lvl = str(todos['summonerLevel'])
    acc_id = str(todos['accountId'])

def buscarHerois():
    champions = 'http://ddragon.leagueoflegends.com/cdn/11.15.1/data/en_US/champion.json'
    response = urlopen(champions)
    data_json = json.loads(response.read())
    print(type(data_json))
    #print(data_json)
    print(type(champions))
    print(champions)
    #for n in data_json['data']:
    #    print(n)

while (contador < 999):
    resultado = str(input('Deseja consultar outro Nick? (S/N) ')).strip() .upper()[0]
    if resultado == 'S':
        nick = str(input('Digite outro nick: '))

        buscarDadosPlayer(nick)

    else:
        print('Programa encerrado!')
        break



buscarHerois()