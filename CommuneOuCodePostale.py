donneesGeographiques = {
    "Paris":"75000",
    "Marseille":"13000",
    "Lyon":"69000"
}

def afficherInfos(dictionnaire):
    for clef,valeur in dictionnaire.items():
        print(f"{clef} : {valeur}")


def rechercherCommune(dictionnaire):
    codePostale= input("Saisir la code postale: ")
    found = False
    for ville, code in dictionnaire.items():
        if codePostale == code:
            print(f"le code {codePostale} coresspond à {ville}")
            found = True
            break 
    if not found:
        print(f"Aucune cummune correspond à {codePostale}".upper())


def rechercherZipCode(dictionnaire):
    commune = input("saisir le nom de la commune: ")
    if commune in dictionnaire.keys():
        print(f"le code de {commune} est {dictionnaire[commune]}")
    else:
        print(f"La commune {commune} est introuvable!".upper())


def ajouterVille(dictionnaire):
    commune = input("saisir le nom de la commune: ")
    codePostale= input("Saisir la code postale: ")
    dictionnaire[commune]= codePostale


continuer =""
while continuer != "q":
    choix = int(input("""
1- Afficher les informations
2- Ajouter une commune
3- chercher nom de commune
4- Chercher par code postal
5- Quitter l'application                
>> """))
    if choix == 1:
        afficherInfos(donneesGeographiques)
    elif choix == 2:
        ajouterVille(donneesGeographiques)
    elif choix == 3:
        rechercherZipCode(donneesGeographiques)
    elif choix == 4:
        rechercherCommune(donneesGeographiques)
    elif choix == 5:
        print("Vous venez de quitter le programme")
        continuer = "q"
    else:
        print("Je n'ai pas compris votre choix!")









    
