import json
import requests
from urllib.request import urlopen
import mysql.connector
from datetime import datetime

data_atual = print(datetime.today())
print(20*'----')

######## Criação da connect com banco
'''con = mysql.connector.connect(host='localhost',database='loldb',user='root',password='6471Bernssl!')
if con.is_connected():
    db_info = con.get_server_info()
    print("Conectado ao servidor MySQL versão ",db_info)
    cursor = con.cursor()
    cursor.execute("select database();")
    linha = cursor.fetchone()
    print("Conectado ao banco de dados ",linha)
if con.is_connected():
    cursor.close()
    con.close()
    print("Conexão ao MySQL foi encerrada")'''

####### Criação do arquivo de config
arq = open('config.txt')
linhas = arq.readlines()
for linha in linhas:
    print(linha)

#r = requests.get(url_nicks)
#todos = json.loads(r.content)

#print('Seu nick é ' + todos['name'])
#print('Seu level é ' + str(todos['summonerLevel']))
#print(type(todos))

#print(todos)

 # Insert some data into table



contador = 0
def gravarUsuarioBase(nickPlayer,accountId,summonerLevel,data_busca_dados_player):
    con = mysql.connector.connect(host='localhost',database='loldb',user='root',password='6471Bernssl!')
    if con.is_connected():
        db_info = con.get_server_info()
        print("Conectado ao servidor MySQL versão ",db_info)
        cursor = con.cursor()
        cursor.execute("INSERT INTO players (nickPlayer, accountId, nickLvl, dt_pesquisa) VALUES (%s, %s, %s, %s);" , (nickPlayer , accountId ,summonerLevel,data_busca_dados_player))
        con.commit()
        linha = cursor.fetchone()
        print("Conectado ao banco de dados ",linha)
    if con.is_connected():
        cursor.close()
        con.close()
        print("Conexão ao MySQL foi encerrada")


def gravarHeroisBase(idheroi,nomeHeroi,titulo,img):
    con = mysql.connector.connect(host='localhost',database='loldb',user='root',password='6471Bernssl!')
    if con.is_connected():
        db_info = con.get_server_info()
        print("Conectado ao servidor MySQL versão ",db_info)
        cursor = con.cursor()
        cursor.execute("INSERT INTO heroi (idheroi, nomeHeroi, titulo, img) VALUES (%s, %s, %s, %s);" , (idheroi , nomeHeroi ,titulo,img))
        con.commit()
        linha = cursor.fetchone()
        print("Conectado ao banco de dados ",linha)
    if con.is_connected():
        cursor.close()
        con.close()
        print("Conexão ao MySQL foi encerrada")

def buscarDadosPlayer(nick):
    url_nicks = 'https://br1.api.riotgames.com/lol/summoner/v4/summoners/by-name/'+nick+'?api_key='+str(linha)
    r = requests.get(url_nicks)
    todos = json.loads(r.content)
    print(todos)
    print('Seu nick é ' + todos['name'])
    name = str(todos['name'])
    print('Seu level é ' + str(todos['summonerLevel']))
    lvl = str(todos['summonerLevel'])
    acc_id = str(todos['accountId'])
    data_busca_dados_player = datetime.today()
    
    return name,lvl,acc_id,data_busca_dados_player

def buscarHerois():
    champions = 'http://ddragon.leagueoflegends.com/cdn/11.15.1/data/en_US/champion.json'
    response = urlopen(champions)
    data_json = json.loads(response.read())
    print(type(data_json))
    #print(data_json)
    print(type(champions))
    #print(champions)
    for n in data_json['data']:
        #print(n)
        nomeHeroi = n
        #print(data_json['data'][n]['key'])
        idheroi = data_json['data'][n]['key']
        #print(data_json['data'][n]['title'])
        titulo = data_json['data'][n]['title']
        #print(data_json['data'][n]['image']['full'])
        img = data_json['data'][n]['image']['full']
        gravarHeroisBase(idheroi,nomeHeroi,titulo,img)
        

while (contador < 999):
    nick = str(input('Digite o nick que deseja obter informações? '))
    name,lvl,acc_id,data_busca_dados_player = buscarDadosPlayer(nick)
    gravarUsuarioBase(nick,acc_id,lvl,data_busca_dados_player)

    resultado = str(input('Deseja buscar informações sobre outro player? (S/N) ')).strip() .upper()[0]

    if resultado == 'S':
        nick = str(input('Digite outro nick: '))

        name,lvl,acc_id,data_busca_dados_player = buscarDadosPlayer(nick)
        print('============ Antes do Gravar==============')
        print(nick)
        print(lvl)
        print(acc_id)
        gravarUsuarioBase(nick,acc_id,lvl,data_busca_dados_player)

    else:
        print('Programa encerrado!')
        break


buscarHerois()
