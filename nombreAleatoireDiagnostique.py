from random import randint
# from saisie import saisir

def saisir (message , limite):
    valeur_int = 0
    while valeur_int == 0:
        valeur_str = input(f"Quel est votre {message}? : ")
        try:
            valeur_int = float(valeur_str) # si le cast fonctionne je passe à la suite :(else) et je saute except
        except: # si le cast ne fonctionne pas je lève une exception
            print("Vous n'avez pas saisi une valeur numérique")
        else:
            if valeur_int == 0: # si la valeur saisie est = zéro
                print("Vous avez saisi zéro")
            elif valeur_int < 0: # si la valeur saisie est négative
                print("Vous avez saisi une valeur négative")
                valeur_int = 0   #je réaffecte 0 à valeur_int pour revenir à la condition initiale
            elif valeur_int > limite:
                print(f"Vous avez saisi une valeur > {limite}")
                valeur_int = 0
            else: # si la valeur saisi est correcte (différente de zéro, n'est pas négative et une valeur numérique)
                print("Vous avez saisi {}".format(valeur_int))
    return valeur_int


nb1 = randint(1,10)
print(f"le nombre aléatoire généré: {nb1}")
continuer =""
compteur = 0

while continuer != "q":
    saisie = saisir("nombre",10)
    # saisie = int(input("Devinez un nombre compris entre 1 et 10: "))
    compteur+= 1
    if saisie == nb1:
        print(f"Bravo! Vous avez réussi au bout de {compteur} essais")
        continuer = "q"
    else:
        if compteur < 3:
            print(f"Vous avez perdu! Il vous reste {3-1}")
            continuer = input("q pur quitter ou autre pour continuer: ")
        else:
            print("Vous avez atteint le nombre d'essais")
            continuer = "q"
