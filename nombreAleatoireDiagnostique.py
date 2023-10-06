from random import randint
nb1 = randint(1,10)
print(nb1)
continuer =""
compteur = 0

while continuer != "q":
    saisie = int(input("Devinez un nombre compris entre 1 et 10: "))
    compteur+= 1
    if saisie == nb1:
        print(f"Bravo! Vous avez réussi au bout de {compteur} essais")
        continuer = "q"
    else:
        if compteur < 3:
            print(f"Vous avez perdu! Il vous reste {3-compteur}")
            continuer = input("q pur quitter ou autre pour continuer: ")
        else:
            print("Vous avez atteint le nombre d'essais")
            continuer = "q"
