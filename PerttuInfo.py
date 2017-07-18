import datetime

def InfoTekija(year):
    yearstr = str(year)
    print("Made by Perttu Antikainen,", yearstr+".", "Released under MIT License.")
    paivamaara = datetime.datetime.now()
    print(paivamaara.day, end=".")
    print(paivamaara.month, end=".")
    print(paivamaara.year)