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



'''' Fazer ficar perguntando o nick ate o usuario informar que deseja sair
##### e sempre exibir apos o usuario digitiar seu nick
######## Guardar accountID nick e lvl
#exibir somente o Nick e LVL '''


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
