import json
import requests

print(15*'----')

nick = str(input('Digite seu Nick: '))
print(f'Seu nick é {nick}')

#ler o arquivo.txt
#api = resultado do arquivo

#http://riot.api.com/+'api'

arq = open('config.txt')
linhas = arq.readlines()
for linha in linhas:
    print(linha)

url_nicks = 'https://br1.api.riotgames.com/lol/summoner/v4/summoners/by-name/'+nick+'?api_key='+linha

r = requests.get(url_nicks)
todos = json.loads(r.content)

print(type(todos))

print(todos)
