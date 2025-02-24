import os
from random import randrange
from math import ceil

argent = 1000
continuer_partie = True

print("vous vous installe a la table de roullete avec", argent, "$.")

while continuer_partie:
    nombre_mise = -1

    while nombre_mise < 0 or nombre_mise > 49:
        nombre_mise = input("Tapez le nombre sur le quel vous voulez miser entre(0 et 49) :")

        try:
            nombre_mise = int(nombre_mise)
        except ValueError:
            print("vous n'avez pas saisis le nombre")
            nombre_mise = -1
            continue
        if nombre_mise < 0:
            print("nombre mise est negatif")
        if nombre_mise  > 49:
            print("nombre_saisie is greater than 49")


    mise = 0

    while mise <= 0 or mise > argent:
        mise = input(" Tapez le montant de votre mise : ")
        try:
            mise = int(mise)
        except ValueError:
            print("vous n'avez pas saisis de nombre")
            mise = -1
            continue
        if mise <= 0:
            print("La mise saisie est negatif ou null")
        if mise > argent:
            print("Vous ne pouvez pas mise autant, vous n'avez", argent, "$")

    numero_gagnant = randrange(50)

    print("la roulete tourne.... ... et s'arrete sur le numero", numero_gagnant)
    if numero_gagnant == nombre_mise:
        print("Felicitation ! vous obtenez", mise * 3, "$ !")
        argent += mise * 3
    elif numero_gagnant % 2 == nombre_mise % 2:
        mise =ceil(mise * 0.5)
        print( "vous avez mise sur la bonne couleur. vous obtenez", mise, "$")
        argent += mise
    else:
        print("Desole l'amie c'est pas pour cette fois vous perder votre mise.")
        argent -= mise
        

    if argent <= 0:
        print("vous ete ruine ! c'est la fin por vous")
        continuer_partie = False
    else:
        print("vous avez a present", argent, "$")
        quitter = input("souhaitez vous quiter le casino (o/n) ? ")
        if quitter == "o" or quitter =="O":
            print("vous avez quitter le casino avec vos gain.")
            continuer_partie = False

        
        
        

                      
            
            
                
                

        
        

