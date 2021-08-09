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
    puuid = str(todos['puuid'])
    data_busca_dados_player = datetime.today()
    
    return name,lvl,acc_id,data_busca_dados_player,puuid

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
    name,lvl,acc_id,data_busca_dados_player,puuid = buscarDadosPlayer(nick)
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




def buscarGameID(puuid):
    inicio = 0
    fim = 100
    url_buscaGameID = 'https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/'+puuid+'/ids?type=ranked&start='+str(inicio)+'&count='+str(fim)+'&api_key='+str(linha)
    r = requests.get(url_buscaGameID)
    todos = json.loads(r.content)
    print(todos)


def buscarDadosGame():
    url_buscaDadosGame = 'https://americas.api.riotgames.com/lol/match/v5/matches/BR1_2315962146?api_key=RGAPI-688ed697-d75d-4685-81c0-77ef7b4d2899'
    r = requests.get(url_buscaDadosGame)
    todos = json.loads(r.content)
    matchId = todos['metadata']['matchId']
    player1 = todos['metadata']['participants'][0]
    player2 = todos['metadata']['participants'][1]
    player3 = todos['metadata']['participants'][2]
    player4 = todos['metadata']['participants'][3]
    player5 = todos['metadata']['participants'][4]
    player6 = todos['metadata']['participants'][5]
    player7 = todos['metadata']['participants'][6]
    player8 = todos['metadata']['participants'][7]
    player9 = todos['metadata']['participants'][8]
    player10 = todos['metadata']['participants'][9]

    return      matchId,player1,player2,player3,player4,player5,player6,player7,player8,player9,player10 
    
 

def gravarMatchesBase(matchId,player1,player2,player3,player4,player5,player6,player7,player8,player9,player10):
    con = mysql.connector.connect(host='localhost',database='loldb',user='root',password='6471Bernssl!')
    if con.is_connected():
        db_info = con.get_server_info()
        print("Conectado ao servidor MySQL versão ",db_info)
        cursor = con.cursor()
        cursor.execute("INSERT INTO matches (IdmatcheApi, player1, player2, player3, player4, player5, player6, player7, player8, player9, player10) VALUES (%s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s);" , 
        (matchId,player1,player2,player3,player4,player5,player6,player7,player8,player9,player10))
        con.commit()
        linha = cursor.fetchone()
        print("Dados da Partida Salva ",linha)
    if con.is_connected():
        cursor.close()
        con.close()
        print("Conexão ao MySQL foi encerrada")

#buscarHerois()
#BR1_2315962146
buscarGameID(puuid)
matchId,player1,player2,player3,player4,player5,player6,player7,player8,player9,player10 = buscarDadosGame()
gravarMatchesBase(matchId,player1,player2,player3,player4,player5,player6,player7,player8,player9,player10)
