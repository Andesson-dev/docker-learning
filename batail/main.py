#Defines a new class called Weapon
class Weapon:

    #Initializes the Weapon class with the attributes nom and attack_ability.
    def __init__(self, nom, attack_ability):

        #Sets the instance variables self.nom and self.attack_ability to the values passed when creating a Weapon object.
        self.nom = nom
        self.attack_ability = attack_ability

#Defines a new class called PowerUp
class PowerUp:

#Initializes the PowerUp class with the attributes nom  and power_cost    
    def __init__(self, nom, power_cost):

        #Sets the instance variables self.nom and self.power_cost to the values passed when creating a PowerUp object.
        self.nom = nom
        self.power_cost = power_cost

#Defines a new class called Player
class Player:

#itializes the Player class with the attribute nom.
    def __init__(self, nom):

#Sets the instance variables for the Player class. Each player starts with 10 lives, no power-up, and no weapon.
        self.nom = nom
        self.nombre_de_vies = 10
        self.power_up = None
        self.weapon = None

 #Defines a method for the Player class called attack. This method takes another player (autre_joueur) and a damage amount as parameters.
    def attack(self, autre_joueur, damage):

       #Reduces the number of lives of the other player (autre_joueur) by the damage amount
        autre_joueur.nombre_de_vies -= damage

        #Prints a message indicating that the player is attacking another player and reducing their lives.
        print(f"{self.nom} attaque {autre_joueur.nom} et coupe {damage} points de vie!")

#Defines a method for the Player class called utiliser_power_up (use power-up). This method takes a power_up and another player (autre_joueur) as parameters.
    def utiliser_power_up(self, power_up, autre_joueur):

        #Checks if the power_cost of the power_up is equal to 10.
        if power_up.power_cost == 10:

            #Sets the player's power-up, calculates the damage, reduces the other player's lives by the damage, and prints a message indicating the use of the power-up and the attack.
            self.power_up = power_up
            damage = 7
            autre_joueur.nombre_de_vies -= damage
            print(f"{self.nom} utilise {power_up.nom} et attaque {autre_joueur.nom}, coupant {damage} points de vie!")

#Defines a method for the Player class called equip_weapon. This method takes a weapon as a parameter.
    def equip_weapon(self, weapon):

        #Sets the player's weapon and prints a message indicating that the player has equipped a weapon.
        self.weapon = weapon
        print(f"{self.nom} s'équipe de {weapon.nom} avec un pouvoir d'attaque de {weapon.attack_ability}.")

#Defines a method for the Player class called check_vie (check life).
    def check_vie(self):

        #Checks if the player's lives are less than or equal to 0 and prints a message indicating that the player is eliminated if true.
        if self.nombre_de_vies <= 0:
            print(f"{self.nom} est éliminé!")


# Création des joueurs
joueur1 = Player("kyler")
joueur2 = Player("kyra")

# Combat
joueur1.attack(joueur2, 5)
joueur2.check_vie()

#Creates a power-up called "united state of smash" with a power cost of 10. Joueur 2 uses this power-up to attack Joueur 1, reducing their lives by 7, and then checks if Joueur 1 is eliminated.
power_up = PowerUp("united state of smash", 10)
joueur2.utiliser_power_up(power_up, joueur1)
joueur1.check_vie()
#Creates a weapon called "Riyujin Jakka" with an attack ability of 5. Joueur 1 equips this weapon and attacks Joueur 2, reducing their lives by 5, and then checks if Joueur 2 is eliminated.

weapon = Weapon(" Riyujin Jakka", 5)
joueur1.equip_weapon(weapon)
joueur1.attack(joueur2, weapon.attack_ability)
joueur2.check_vie()
