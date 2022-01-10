print("Welkom bij Papi Gelato")

def bolletjes():
    askQuestion = True
    while askQuestion:
        hoeveelBolletjes = input("Hoeveel bolletjes wilt u? ")
        if hoeveelBolletjes.isdigit():
            hoeveelBolletjes = int(hoeveelBolletjes)

            if hoeveelBolletjes >= 4 and hoeveelBolletjes <= 8:
                print(f"Dan krijgt u van mij een bakje met {hoeveelBolletjes} bolletjes")
                bolletjeHoorntje = "Bakje"
                stap3(bolletjeHoorntje, hoeveelBolletjes)
                
            elif hoeveelBolletjes > 8:
                print("Sorry, zulke grote bakken hebben we niet")

            if hoeveelBolletjes >= 1 and hoeveelBolletjes <= 8:
                askQuestion = False

        else:
            print("Sorry dat snap ik niet...")

    return hoeveelBolletjes


def stap2(aantalBolletjes):
    askQuestion = True
    while askQuestion:
        bolletjeHoorntje = input(f"Wilt u deze {aantalBolletjes} bolletje(s) in A) een hoorntje of B) een bakje? ").lower()
        if bolletjeHoorntje == "a" or bolletjeHoorntje == "b":
            bolletjeHoorntje = "bakje" if bolletjeHoorntje == "b" else "hoorntje"
            stap3(bolletjeHoorntje, aantalBolletjes)

        else:
            print("Sorry, dat snap ik niet...")
        


def stap3(bolletjeHoorntje, aantalBolletjes):
    askQuestion = True
    while askQuestion:
        totaalBolletjes = input(f"Hier is uw {bolletjeHoorntje} met {aantalBolletjes} bolletje(s). Wilt u nog meer bestellen? (Y/N) ").lower()
        if totaalBolletjes == "y":
            bolletjes()
            
        elif totaalBolletjes == "n":
            print("Bedankt en tot ziens!")
            askQuestion = False
            
        else:
            print("Sorry, dat snap ik niet...")
        


def main():
    aantalBolletjes = bolletjes()

    if aantalBolletjes >= 1 and aantalBolletjes <= 3:
        stap2(aantalBolletjes)

if __name__ == "__main__":
    main()



def smaken():
    for x in range(1, bolletjes+1):
        askQuestion = True
        while askQuestion:
            bolletjeSmaak = input(f"Welke smaak wilt u voor bolletje nummer {x}? A) Aardbei, C) Chocolade, M) Munt of V) Vanille?").upper()
            if bolletjeSmaak == "A" or bolletjeSmaak == "C" or bolletjeSmaak == "M" or bolletjeSmaak == "V":
                print("")
                askQuestion = False

            else:
                print("Sorry dat snap ik niet...")
    