class Point:
    def __init__(self, x: float, y: float):
        """
        initialisre un point geometric avec ses coordone x y
        """

        self.x = x
        self.y = y

class Space:
    def __init__(self, points: list[Point] = []):
        """
        initialise a geometric space with his point
        """

        self.points = points

    def __str__(self):
        space = ""
        width = max(self.points, key=lambda p: p.x).x
        height = max(self.points, key=lambda p: p.y).y

        for y in range(height+1):
            for x in range(width+1):
                symbol = '   '

                for point in self.points:
                    if (point.x, point.y) == (x, y):
                        symbol = 'x'
                        break
                
                space += symbol
                    
            space += '\n'
        
        return space

    def merge(self, space: "Space"):
        """
        merge 2 space in 1
        """

        self.points += space.points


class Polygone(Space):
    pass

class Rectangle(Polygone):
    def __init__(self, width: float, length: float):
        """
        initiale a rectangle base on his length and width
        """
            
        super().__init__([Point(0, 0), Point(0, length), Point(width, 0), Point(width, length)])

class Square(Polygone):
    def __init__(self, wide: float):
        """
        initialise a square base on his side
        """

        super().__init__([Point(0, 0), Point(0, wide), Point(wide, 0), Point(wide, wide)])


########################
space = Space()

space.merge(Rectangle(10, 2))
space.merge(Square(5))

print(space)