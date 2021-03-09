from funkce import *

if __name__ == "__main__":
    oddelovac()
    print("Vítejte v e-shopu vecerka.cz - pokud si chcete objednat nějaké dobroty, zadejte prosím pár osobních údajů a hned se do toho dáme!")
    oddelovac()

    jmeno = input("Zadejte své jmeno: ")
    prijmeni = input("Zadejte své příjmení: ")
    kontrola_jmena_prijmeni(jmeno, prijmeni)
    oddelovac()

    vek = input("Zadejte svůj věk: ")
    kontrola_vek(vek)
    oddelovac()

    mail = input()put("Zadejte svůj e-mail: ")
    kontrola_mail(mail)
    oddelovac()

    print("Vypadá to, že všechny Vaše údaje jsou v pořádku, pojďme se tedy dát do nakupování!")
    oddelovac()

    zadej_co_chces_koupit(jmeno,prijmeni)
    exit()