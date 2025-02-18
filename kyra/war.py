class EtreVivant:
    TYPE_ALIMENTATION = ('carnivore', 'herbivore', 'omnivore')

    def __init__(self, nom, type_alimentation):
        """
        Initialise un être vivant avec un nom et un type d'alimentation.
        
        :param nom: nom de l'être vivant
        :param type_alimentation: type d'alimentation (carnivore, herbivore, omnivore)
        """
        self.nom = nom

        if type_alimentation in self.TYPE_ALIMENTATION:
            self.type_alimentation = type_alimentation
        else:
            raise Exception(f"Les types d'alimentation acceptes sont {', '.join(self.TYPE_ALIMENTATION)}")
    
    def peut_manger(self, autre):
        """
        Vérifie si l'être vivant peut manger un autre être vivant basé sur leur type d'alimentation.
        
        :param autre: l'autre être vivant à vérifier
        :return: True si l'être vivant peut manger l'autre, sinon False
        """
        if self.type_alimentation == 'carnivore' and isinstance(autre, (Animal, Humain)):
            return True
        elif self.type_alimentation == 'herbivore' and isinstance(autre, Plante):
            return True  # Un herbivore ne mangera pas un autre herbivore
        elif self.type_alimentation == 'omnivore':
            return True
        return False

    def __str__(self):
        return f"{self.nom} ({self.type_alimentation})"
    

class Animal(EtreVivant):
    pass


class Humain(EtreVivant):
    pass


class Plante(EtreVivant):
    pass


# Création des êtres vivants
ecosysteme = [
    Animal('Lion', 'carnivore'),
    Animal('Antilope', 'herbivore'),
    Animal('Ours', 'omnivore'),
    Animal('Zèbre', 'herbivore'),
    Plante('Herbe', 'omnivore'),
    Humain('Homme', 'omnivore'),
    Humain('Femme', 'omnivore'),
]

for a in ecosysteme:
    for b in ecosysteme:
        print(f"{a} peut-il manger {b}? {'Oui' if a.peut_manger(b) else 'Non'}")
