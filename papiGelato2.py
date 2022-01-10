print("Welkom bij Papi Gelato je mag alle smaken kiezen zolang het maar vanille ijs is.")

def bolletjes():
    askQuestion = True
    while askQuestion:
        hoeveelBolletjes = input("Hoeveel bolletjes wilt u? ")
        if hoeveelBolletjes.isdigit():
            hoeveelBolletjes = int(hoeveelBolletjes)

            if hoeveelBolletjes >= 4 and hoeveelBolletjes <= 8:
                print(f"Dan krijgt u van mij een bakje met {hoeveelBolletjes} bolletjes")

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
        bolletjeHoorntje = input(f"Wilt u deze {aantalBolletjes} bolletje(s) in A) een hoorntje of B) een bakje?").lower()
        if bolletjeHoorntje == "a" or bolletjeHoorntje == "b":
            stap3()

        else:
            print("Sorry, dat snap ik niet...")
        


def stap3(bolletjeHoorntje, hoeveelBolletjes):
    askQuestion = True
    while askQuestion:
        totaalBolletjes = input(f"Hier is uw {bolletjeHoorntje} met {hoeveelBolletjes} bolletje(s). Wilt u nog meer bestellen? (Y/N)").lower()
        if totaalBolletjes == "y":
            bolletjes()

        elif totaalBolletjes == "n":
            print("Bedankt en tot ziens!")

        else:
            print("Sorry, dat snap ik niet...")
        


def main():
    aantalBolletjes = bolletjes()

    if aantalBolletjes >= 1 and aantalBolletjes <= 3:
        stap2(aantalBolletjes)

if __name__ == "__main__":
    main()
    