hoorntje = 0
bakje = 0
totaalBolletjes = 0

def stap1():
    global bakje
    smaakjesLijst = []
    try:
        bolletjes = int(input("Hoeveel bolletjes wilt u?\n"))
        if bolletjes >= 1 and bolletjes <= 3:
            for x in range(1, bolletjes+1):
                smaak = smaakjes(x)
                smaakjesLijst.append(smaak)
            stap2(str(bolletjes))
        elif bolletjes >= 4 and bolletjes <= 8:
            print("Dan krijgt u van mij een bakje met " + str(bolletjes) + " bolletjes")
            bakje += 1
            for x in range(1, bolletjes+1):
                smaak = smaakjes(x)
                smaakjesLijst.append(smaak)
            stap3(str(bolletjes), "bakje")
        else:
            print("Sorry, zulke grote bakken hebben we niet")
            stap1()
    except:
        print("Sorry dat snap ik niet...")
        stap1()

def smaakjes(bolletjeNummer):
    smaak = input("Welke smaak wilt u voor bolletje nummer " + str(bolletjeNummer) + "? A) Aardbei, C) Chocolade, M) Munt of V) Vanille?\n").lower()
    if smaak == "a":
        return "aardbei"
    elif smaak == "c":
        return "chocolade"
    elif smaak == "m":
        return "munt"
    elif smaak == "v":
        return "vanille"
    else:
        print("Sorry dat snap ik niet...")
        smaakjes(bolletjeNummer)

def stap2(bolletjes):
    global hoorntje
    global bakje
    hoorntjeOfBakje = input("Wilt u deze " + bolletjes + " bolletje(s) in A) een hoorntje of B) een bakje?\n").lower()
    if hoorntjeOfBakje != "b" and hoorntjeOfBakje != "a":
        print("Sorry dat snap ik niet...")
        stap2(bolletjes)
    else:
        hoorntje = hoorntje + 1 if hoorntjeOfBakje == "hoorntje" else hoorntje + 0
        bakje = bakje + 1 if hoorntjeOfBakje == "bakje" else bakje + 0
        stap3(bolletjes, hoorntjeOfBakje)

def stap3(bolletjes, hoorntjeOfBakje):
    global totaalBolletjes
    choice = input("Hier is uw " + hoorntjeOfBakje + " met " + bolletjes + " bolletje(s). Wilt u nog meer bestellen? (Y/N)\n").lower()
    if choice == "y":
        totaalBolletjes += int(bolletjes)
        stap1()
    elif choice == "n":
        totaalBolletjes += int(bolletjes)
        print("Bedankt en tot ziens!")
        bonnetje(int(bolletjes), hoorntjeOfBakje)
    else:
        print("Sorry dat snap ik niet...")
        stap3(bolletjes, hoorntjeOfBakje)

def bonnetje(bolletjes, hoorntjeOfBakje):
    totaalBolletjesPrijs = round(totaalBolletjes * 1.1, 2)
    totaalHorntjesPrijs = round(hoorntje * 1.25, 2)
    totaalBakjesPrijs = round(bakje * 0.75, 2)
    totaal = totaalBolletjesPrijs + totaalHorntjesPrijs + totaalBakjesPrijs
    print('---------["Papi Gelato"]---------')
    a = print("Bolletjes    " + str(totaalBolletjes) + " x 1.10   = " + str(totaalBolletjesPrijs)) if bolletjes > 0 else 0
    b = print("Horrentje    " + str(hoorntje) + " x 1.25   = " + str(totaalHorntjesPrijs)) if hoorntje > 0 else 0
    c = print("Bakje        " + str(bakje) + " x 0.75   = " + str(totaalBakjesPrijs)) if bakje > 0 else 0
    print("                        ------ +\nTotaal                  = " + str(totaal))

print("Welkom bij Papi Gelato")

stap1()