from produkty import *

def oddelovac():
  print(130*"-")

def kontrola_jmena_prijmeni(jmeno,prijmeni):
  if jmeno.isalpha() and prijmeni.isalpha():
     print("Zadání proběhlo v pořádku")
  else:
    print("Chyba - jméno a příjmení musí obsahovat pouze písmena. Zkuste to prosím znovu")
    exit()

def kontrola_vek(vek):
  if vek.isdigit():
    vek = int(vek)
    if vek >=12:
      print("Zadání proběhlo v pořádku - věková hranice 12 let je splněna")
    else:
      print("Chyba - pro nákup v našem obchodě musíte mít alespoň 12 let.")
      exit()
  else:
    print("Chyba - věk musí obsahovat pouze číslice")
    exit()

def kontrola_mail(mail):
  if "@" in mail:
    print("Zadání proběhlo v pořádku")
  else:
    print("Chyba - e-mail musí obsahovat symbol '@'")
    exit()

def vytvor_uctenku(jmeno,prijmeni,kosik,ceny):
  with open("ucet.txt",mode="w") as file:
    file.writelines(f"Zakaznik: {jmeno} {prijmeni} \n")
    file.writelines(130*"-"+"\n")
    for i in range(len(kosik)):
      file.writelines(f"{kosik[i]}-{ceny[i]}kc \n")
    file.writelines(130*"-"+"\n")
    file.writelines(f"Celkovy nakup {len(kosik)}ks polozek v celkove hodnote  {sum(ceny)}kc")

def zadej_co_chces_koupit(jmeno,prijmeni):
    kosik = []
    ceny = []

    while True:
        print(f"V našem obchodě si můžete vybrat z následujícího sortimentu produktů: {list(zbozi.keys())} ")
        vyber_sortimentu = input(
            "Napiste nazev sortimentu o který máte zájem pro zobrazení nabídky produktů a cen - pro ukončení zadávání (q): ").lower()
        if vyber_sortimentu in zbozi.keys():
            while True:
                oddelovac()
                print(list(zbozi[vyber_sortimentu].items()))
                vybrana_polozka = input(
                    "Zadejte název položky pro její přidání do košíku (bez diakritiky) pro návrat do volby sortimentu (q): ").lower()
                if vybrana_polozka in zbozi[vyber_sortimentu].keys():
                    mnozstvi = int(input("Zadejte počet kusů: "))
                    for kus in range(mnozstvi):
                        kosik.append(vybrana_polozka)
                        ceny.append(zbozi[vyber_sortimentu][vybrana_polozka])
                    print(f"Polozka {vybrana_polozka}-{mnozstvi}ks byla přidána do košíku.")
                elif vybrana_polozka == "q":
                    break
                else:
                    print("Zadání neodpovídá žádné položce")
        elif vyber_sortimentu == "q":
            break
        else:
            print("Zadání neodpovídá žádnému existujícímu sortimentu")
    oddelovac()

    while True:
        uctenka_volba = input("Chcete vystavit detailni elektronickou účtenku? ANO/NE: ").lower()
        if uctenka_volba == "ano":
            vytvor_uctenku(jmeno,prijmeni,kosik, ceny)
            print("Vaše účtenka byla vytvořena.")
            break
        elif uctenka_volba == "ne":
            oddelovac()
            print(f"Zákazník: {jmeno} {prijmeni}")
            print(f"Celkový nákup {len(kosik)}ks položek v celkové hodnotě  {sum(ceny)}kč.")
            break
        else:
            print("Chyba v zadání - musí být ANO/NE")
    oddelovac()
    print("Těšíme se na Váš další nákup!")
