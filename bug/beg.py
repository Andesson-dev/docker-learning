#Nous importons le module math pour utiliser des fonctions mathématiques plus tard
import math

class Point:
    def __init__(self, nom="", x=0.0, y=0.0, couleur="noir"):
        self.nom = nom
        self.x = x
        self.y = y
        self.couleur = couleur

#Chaque méthode retourne la valeur de son attribut correspondant.
    def get_nom(self):
        return self.nom

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_couleur(self):
        return self.couleur

#Ces méthodes permettent de changer les valeurs des attributs nom, x, y et couleur.
    def set_nom(self, nouveau_nom):
        self.nom = nouveau_nom

    def set_x(self, nouvelle_position):
        self.x = nouvelle_position

    def set_y(self, nouvelle_position):
        self.y = nouvelle_position

    def set_couleur(self, nouvelle_couleur):
        self.couleur = nouvelle_couleur

#Cette méthode ajoute dx à la position x et dy à la position y, déplaçant ainsi le point.
    def deplacer(self, dx, dy):
        self.x += dx
        self.y += dy

#Cette méthode affiche les informations du point dans un format lisible
    def afficher(self):
        print(f"Point {self.nom}: (x={self.x}, y={self.y}), Couleur={self.couleur}")

#This method calculates the Euclidean distance between the current point and another point using the Pythagorean theorem.
    def distance(self, autre_point):
        return math.sqrt((self.x - autre_point.get_x())**2 + (self.y - autre_point.get_y())**2)
    import math

#This ensures the following code runs only if the script is executed directly, not if it's imported as a module.
if __name__ == "__main__":
    # Création de deux points
    point1 = Point("A", 2.0, 3.0, "rouge")
    point2 = Point("B", 5.0, 7.0, "bleu")

    # Affichage des points
    point1.afficher()
    point2.afficher()

    # Calcul de la distance entre les deux points
    dist = point1.distance(point2)
    print(f"La distance entre {point1.get_nom()} et {point2.get_nom()} est de {dist:.2f}")

    # Test des autres méthodes
    point1.deplacer(1.0, -1.0)
    point1.set_couleur("vert")
    point1.afficher()

