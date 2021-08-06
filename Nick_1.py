import json
import requests

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



while (contador < 999):
    resultado = str(input('Deseja consultar outro Nick? (S/N) ')).strip() .upper()[0]
    if resultado == 'S':
        nick = str(input('Digite outro nick: '))

        url_nicks = 'https://br1.api.riotgames.com/lol/summoner/v4/summoners/by-name/'+nick+'?api_key='+linha
        r = requests.get(url_nicks)
        todos = json.loads(r.content)
        print('Seu nick é ' + todos['name'])
        print('Seu level é ' + str(todos['summonerLevel']))
        contador = 1
        
    else:
        print('Programa encerrado!')
        break

