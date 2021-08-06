import json
import requests

print(20*'----')

arq = open('config.txt')
linhas = arq.readlines()
for linha in linhas:
    print(linha)


nick = str(input('Digite seu nick: '))


url_nicks = 'https://br1.api.riotgames.com/lol/summoner/v4/summoners/by-name/'+nick+'?api_key='+linha

#url_matchs = 'https://br1.api.riotgames.com/lol/match/v4/matchlists/by-account/'+account_id+'?api_key='+linha1

r = requests.get(url_nicks)
#s = requests.get(url_nicks1)
todos = json.loads(r.content)
#todos1 = json.loads(s.content)

#print(f'a {todos1}')
print('Seu nick é ' + todos['name'])
name = todos['name']
lvl = todos['summonerLevel']
account_id = todos['accountId']
print('Seu level é ' + str(todos['summonerLevel']))
#print(type(todos))

#print(todos)
print('nome é '+name)
print('lvl é '+str(lvl))
print('Id da conta é '+account_id)
url_matchs = 'https://br1.api.riotgames.com/lol/match/v4/matchlists/by-account/'+account_id+'?api_key='+linha
r_match = requests.get(url_matchs)
todos_match = json.loads(r_match.content)
print('O total de jogos é: {}'.format(+todos_match.get('totalGames')))

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
        url_matchs = 'https://br1.api.riotgames.com/lol/match/v4/matchlists/by-account/'+account_id+'?api_key='+linha
        r_match = requests.get(url_matchs)
        todos_match = json.loads(r_match.content)
        print('O total de jogos é: {}'.format(+todos_match.get('totalGames')))
        contador = 1
        
    else:
        print('Programa encerrado!')
        break

'''url_matchs = 'https://br1.api.riotgames.com/lol/match/v4/matchlists/by-account/'+account_id+'?api_key='+linha
r_match = requests.get(url_matchs)
todos_match = json.loads(r_match.content)
print(todos_match.get('totalGames'))'''