# JRBlacK

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

Este é o JRBlacK um bot feito para o discord. Ele conta com diversos sistemas, tais como Level e XP, Welcome, Logs, Economy, Funny e mais...

# Novidades!

  - Módulo: hacking | checks
  - Comandos: nmap | whois
  - Código: Otimizado!

Está nova atualização conta com dois módulos novos e três novos comandos, sendo que um é sub_comando do `nmap`.

### Configuração & Instalação

JrBlack requer [Python3](https://python.org/) v3.6.6+ para poder rodar o bot perfeitamente.

#### **Etapa 1:** Baixando código e dependências
```sh
$ git clone https://github.com/blkzy/JRBlacK
$ cd JRBlacK
$ python3 -m pip install -r requirements.txt
$ sudo apt-get install nmap # Isso no caso do seu sistema ser baseado no Debian ou Ubuntu.
```

#### **Etapa 2:** Database
O JRBlacK Utiliza banco de dados NoSQL ou melhor... MongoDB.
Estarei disponibilizando a baixo um site que disponibiliza essas database gratuitamente.
Caso não tenha muita familiaridade com MongoDB, basta procurar algum tutorial/curso no youtube que você irá entender perfeitamente o funcionamento e como utilizar o database NoSQL.

- MongoDB Atlas: https://www.mongodb.com/cloud/atlas

#### **Etapa 3:** Icon's
Sim! O bot tem sistema de icone personalizado...
Mas um pequeno probleminha que esse tipo de coisa faz é a falta de paciência para colocar todos os iconês.
Para que você consiga colocar todos os iconês, basta você criar alguns grupos. Acho que na faixa de uns 5 (até o momento).

- Icons8: https://icons8.com/icon/new-icons/color

#### **Etapa 4:** Api's necessárias
O bot utiliza de algumas API's para funcionar alguns comandos. Tais como: `news` e `film`.
Para ter acesso as Key's dessas api basta você entrar nos links abaixo e se cadastrar nos sites, que ele irá te fornecer a Key.
Com as Key's em mãos basta ir no arquivo [Database/__init__.py](https://github.com/BlackZacky/JRBlacK-BOT/blob/master/Database/__init__.py), e colocar as key's lá!

- OMDbApi: https://www.omdbapi.com/
- NewsApi: https://newsapi.org/
- Weather: https://openweathermap.org/api

#### *Etapa Final:** inicie o bot

```sh
$ python3 main.py
```

### Bibliotecas

Eu utilizo algumas bibliotecas para facilitar o desenvolvimento e melhorar a experiência.

| Bibliotecas | Link's |
| ------ | ------ |
| discor py | [pypi][url_discordpy] |
| requests | [pypi][url_requests] |
| datetime | [docs][url_datetime] |
| pymongo | [pypi][url_pymongo] |
| psutil | [pypi][url_psutil] |
| pillow | [ppypi][url_pillow] |
| wikipedia | [pypi][url_wikipedia] |
| humanize | [pypi][url_humanize] |
| beautifulsoup4 | [pypi][url_beautifulsoup4] |
| discord-ext-menus | [github][url_discord_ext_menus] |
| newsapi-python | [pypi][url_newsapi_python] |
| python-whois | [pypi][url_python_whois] |


### Desenvolvimento

Quer contribuir? Ótimo!

Me chame nas minhas redes sociais:
- Discord: blkz#0001
- Instagram: blkz.y

Caso não queira chamar, basta mandar um pull requests que irei analisar o código.

License
----
MIT

**Software livre, claro que sim!!**

  [url_discordpy]: <https://pypi.org/project/discord.py/>
  [url_requests]: <https://pypi.org/project/requests/>
  [url_datetime]: <https://docs.python.org/3/library/datetime.html>
  [url_pymongo]: <https://pypi.org/project/pymongo/>
  [url_psutil]: <https://pypi.org/project/psutil/>
  [url_pillow]: <https://pypi.org/project/Pillow/>
  [url_wikipedia]: <https://pypi.org/project/wikipedia/>
  [url_humanize]: <https://pypi.org/project/humanize/>
  [url_beautifulsoup4]: <https://pypi.org/project/beautifulsoup4/>
  [url_discord_ext_menus]: <https://github.com/Rapptz/discord-ext-menus>
  [url_newsapi_python]: <https://pypi.org/project/newsapi-python/>
  [url_python_whois]: <https://pypi.org/project/python-whois/>