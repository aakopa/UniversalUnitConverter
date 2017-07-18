import PerttuInfo

def Lampotilamuutokset(temp):
    tempin1float = float(temp)  # muuttaa lämpötilan floatiksi stringistä
    #region CelsiusFarenheit
    if StartUnit == "c" and TargetUnit == "f": #valitsee oikein muunnoskaavan yksiköiden perusteella
        # F = (9/5)*C+32
        tempin2 = (9 / 5) * tempin1float + 32 # suorittaa muuntokaavan
        tempin2string = str(tempin2) # muunta uuden arvon takaisin stringiksi

    elif StartUnit == "f" and TargetUnit == "c":
        # C = (5/9)*(F-32)
        tempin2 = (5 / 9) * (tempin1float - 32)
        tempin2string = str(tempin2)

    elif StartUnit == "f" and TargetUnit == "k":
        # T(K) = (T(°F) + 459.67) × 5/9
        tempin2 = (tempin1float+459.67)*5/9
        tempin2string = str(tempin2)

    elif StartUnit == "k" and TargetUnit == "f":
        # T(°F) = T(K) × 9/5 - 459.67
        tempin2 = tempin1float * 9 / 5 - 459.67
        tempin2string = str(tempin2)

    elif StartUnit == "c" and TargetUnit == "k":
        # T(K) = T(°C) + 273.15
        tempin2 = tempin1float + 273.15
        tempin2string = str(tempin2)

    elif StartUnit == "k" and TargetUnit == "c":
        # T(°C) = T(K) - 273.15
        tempin2 = tempin1float - 273.15
        tempin2string = str(tempin2)

    if TargetUnit == "c":     # tulostaa vastauksen
        return tempin2string + " °C"
    elif TargetUnit == "k":
        return tempin2string + " K"
    elif TargetUnit == "f":
        return tempin2string + " °F"

def Tehomuutokset(power):
    powerin1float = float(power)
    if StartUnit == "kw" and TargetUnit == "hv":
        # P(hp) = P(kW) / 0.745699872
        powerin2 = powerin1float / 0.745699872
        powerin2string = str(powerin2)
    elif StartUnit == "hv" and TargetUnit == "kw":
        # P(kW) = 0.745699872 · P(hp)
        powerin2 = powerin1float * 0.745699872
        powerin2string = str(powerin2)

    if TargetUnit == "hv":     # tulostaa vastauksen
        return powerin2string + " hv"
    elif TargetUnit == "kw":
        return powerin2string + " kw"

def Tallennustilamuutokset(size):

    newsize = float(size)
    if (StartUnit == "Gb" and TargetUnit == "GB") or (StartUnit == "Mb" and TargetUnit == "MB"):
        finalsize = newsize / 8
        finalsizestring = str(finalsize)

    elif (StartUnit == "GB" and TargetUnit == "Gb") or (StartUnit == "MB" and TargetUnit == "Mb"):
        finalsize = newsize * 8
        finalsizestring = str(finalsize)

    elif (StartUnit == "MB" and TargetUnit == "GB") or (StartUnit == "Mb" and TargetUnit == "Gb"):
        finalsize = newsize / 1024
        finalsizestring = str(finalsize)

    elif (StartUnit == "GB" and TargetUnit == "MB") or (StartUnit == "Gb" and TargetUnit == "Mb"):
        finalsize = newsize * 1024
        finalsizestring = str(finalsize)

    elif (StartUnit == "MB" and TargetUnit == "Gb") or (StartUnit == "GB" and TargetUnit == "Mb"):
        finalsize = (newsize / 1024) * 8
        finalsizestring = str(finalsize)

    elif (StartUnit == "Mb" and TargetUnit == "GB") or (StartUnit == "Gb" and TargetUnit == "MB"):
        finalsize = (newsize / 1024) / 8
        finalsizestring = str(finalsize)

    if TargetUnit == "GB":
        return finalsizestring + " GB"
    elif TargetUnit == "MB":
        return finalsizestring + " MB"
    elif TargetUnit == "Gb":
        return finalsizestring + " Gb"
    elif TargetUnit == "Mb":
        return finalsizestring + " Mb"

def Laskin(numero1, numero2, operaattori):

    lasku = numero1+operaattori+numero2
    tulos = eval(lasku)
    return tulos

def LokiTallennus(Choise, asiaa):
    filename = "output.log" #antaa tiedostonimen
    output = open(filename, 'a') #lataa tiedoston
    output.write(asiaa+" = ") #Kirjoittaa lausekkeen lokiin
    output.write(Choise+"\n") #Kirjoittaa vastauksen lokiin
    output.close() #sulkee

def main(): # pää loop
    tarkistus = 0 #Tarkistaa suoriutuiko ohjelma läpi oikein
    while True:
        try:
            Muunnosrivi = input("Kirjoita haluamasi muutos: ")
            Inputvalues = Muunnosrivi.split()
            global Value
            global StartUnit
            global TargetUnit
            Value = Inputvalues[0]
            StartUnit = Inputvalues[1]
            TargetUnit = Inputvalues[2]
            break
        except IndexError:
            print("Sinun täytyy antaa 3 arvoa")
            continue
    Value = Value.lower()
    if StartUnit == "Gb" or StartUnit == "GB" or StartUnit == "MB" or StartUnit == "Mb":
        if TargetUnit == "Gb" or TargetUnit == "GB" or TargetUnit == "MB" or TargetUnit == "Mb":
            Muutos = Tallennustilamuutokset(Value)
            LokiTallennus(Muutos, Muunnosrivi)
            print(Muutos)
            tarkistus = tarkistus + 1
    StartUnit = StartUnit.lower()
    TargetUnit = TargetUnit.lower()
    if StartUnit == "c" or StartUnit == "f" or StartUnit == "k":
        if TargetUnit == "c" or TargetUnit == "f" or TargetUnit == "k":
            Muutos = Lampotilamuutokset(Value)
            LokiTallennus(Muutos, Muunnosrivi)
            print(Muutos)
            tarkistus = tarkistus + 1
    if StartUnit == "kw" or StartUnit == "hv":
        if TargetUnit == "kw" or TargetUnit == "hv":
            Muutos = Tehomuutokset(Value)
            LokiTallennus(Muutos, Muunnosrivi)
            print(Muutos)
            tarkistus = tarkistus + 1
    if StartUnit == "+" or StartUnit == "-" or StartUnit == "*" or StartUnit == "/"or StartUnit == "**" or StartUnit == "^":
        LaskinOperaattori = StartUnit
        LaskinOperaattori = StartUnit.replace("^", "**")
        Lasku = Laskin(Value, TargetUnit, LaskinOperaattori)
        LaskuLauseke = str(Value)+str(LaskinOperaattori)+str(TargetUnit)+" = "+str(Lasku)
        Muutosrivi = Value, StartUnit, TargetUnit
        LokiTallennus(LaskuLauseke, Muunnosrivi)
        print(Lasku)
        tarkistus = tarkistus + 1
    if not tarkistus == 1:
        print("Et syöttänyt kelvollista muunnoslausetta")
        main()

def Lopetus(paatos):
    vastaukset = ["kyllä", "Yes", "k", "y", "kylla", "yes"]
    while True: #Kysyy haluaako käyttäjä suorittaa toisen muunnoksen
        print("Haluatko suorittaa toisen muunnoksen tai laskun?")
        valinta = input("")
        if valinta == "": #estää tyhjän vastauksen
            continue
        break
    if valinta in vastaukset: #tarkistaa käyttäjän vastauksen
        paatos = 1
    else:
        paatos = 0
    return paatos


print("Universaali Yksikkömuunnin") #Ohjelman esittely
PerttuInfo.InfoTekija(2017) #Kirjoittaa tekijän tiedot
print('Syntaksi: Anna muunoksesi muodossa {Määrä} {Lähtö yksikkö} {Kohde yksikkö}, esimerkiksi: 34 F C') #Syntaksi ohjeet
print("Voit myös syöttää yksinkertaisen laskun muodossa {ensimmäinen luku} {operaattori kuten +} {toinen luku}")
print()
jatkaa = 1 #Muuttuja joka määrittelee ohjelman jatkumisen
while True:
    if jatkaa == 1:
         main() #Ajaa pääloopin
         jatkaa = Lopetus(jatkaa) #Ajaa loptusloopin
    else:
        exit() #Sulkee ohjelman

