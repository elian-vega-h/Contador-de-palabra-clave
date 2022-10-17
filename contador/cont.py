import re

tweets = []
with open('tweets.csv', 'r', newline='', encoding="utf8") as csvfile:
    for line in csvfile:
       tweets.append(line)
       # print(tweets)

# print(tweets)
contadorFelicidad = 0
contadorEnojo = 0
contadorAmor = 0
contadorHumor = 0
contadorInfidelidad = 0
contadorAmigo = 0
contadorHttps = 0
contadorEmojis= 0
regexp = re.compile(r'(\u00a9|\u00ae|[\u2000-\u3300]|\ud83c[\ud000-\udfff]|\ud83d[\ud000-\udfff]|\ud83e[\ud000-\udfff])')

n = 0
for n in tweets:
    print(n)

    if(n.__contains__("feliz")):
        contadorFelicidad = contadorFelicidad + 1
    if(n.__contains__("culpa")):
        contadorEnojo = contadorEnojo + 1
    if(n.__contains__("amor")):
        contadorAmor = contadorAmor + 1
    if(n.__contains__("sentimientos")):
        contadorHumor = contadorHumor + 1
    if(n.__contains__("infidelidad")):
        contadorInfidelidad = contadorInfidelidad + 1
    if(n.__contains__("miedo")):
        contadorAmigo = contadorAmigo + 1
    if(n.__contains__("https")):
       contadorHttps =contadorHttps + 1
    if regexp.search(n):
       contadorEmojis =contadorEmojis + 1

    
print(contadorFelicidad , "feliz")
print(contadorEnojo , "culpa")
print(contadorAmor , "amor")
print(contadorHumor , "sentimientos")
print(contadorInfidelidad , "infidelidad")
print(contadorAmigo , "miedo")
print(contadorHttps , "URL")
print(contadorEmojis , "Emojis")