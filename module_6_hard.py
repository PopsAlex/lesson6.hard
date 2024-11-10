from math import pi


class Figure:
    sides_count = 0

    def __init__(self, __color, *__sides, filled=False):
        if len(__sides) == 1:
            self.__sides = [__sides[0] for i in range(self.sides_count)]
        elif len(__sides) != self.sides_count:
            self.__sides = [1 for i in range(self.sides_count)]
        else:
            self.__sides = list(__sides)
        self.__color = list(__color)
        self.filled = filled
        if self.__color != None:
            self.filled = True

    def get_color(self):
        return f'Цвет фигуры {type(self).__name__}: {self.__color}'

    def __is_valid_color(self, r, g, b):
        for i in (r, g, b):
            if not isinstance(i, int) or (i <= 0 or i > 255):
                return False
        return True

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *args):
        for i in args:
            if not isinstance(i, int) or len(args) != self.sides_count:
                return False
        return True

    def get_sides(self):
        return f'Стороны фигуры {type(self).__name__}: {list(self.__sides)}'

    def __len__(self):
        perimetr = 0
        for i in self.__sides:
            perimetr += i
            print(f'Периметр фигуры {type(self).__name__}: ', end='')
        return perimetr

    def set_sides(self, *new_sides):
        if len(new_sides) == self.sides_count:
            self.__sides = new_sides


class Circle(Figure):
    sides_count = 1

    def __init__(self, __color, *__sides, filled=False):
        super().__init__(__color, *__sides, filled=False)
        if len(__sides) == 1:
            self.__sides = [__sides[0] for i in range(self.sides_count)]
        elif len(__sides) != self.sides_count:
            self.__sides = [1 for i in range(self.sides_count)]
        else:
            self.__sides = list(__sides)
        self.__color = list(__color)
        self.__radius = round(self.__sides[0] / (2 * pi), 2)

    def get_square(self):
        square = round((self.__radius ** 2) * pi, 2)
        return f'Площадь фигуры {type(self).__name__}: {square} и радиус: {self.__radius}'

class Triangle(Figure):
    sides_count = 3

    def __init__(self, __color, *__sides, filled=False):
        super().__init__(__color, *__sides, filled=False)
        if len(__sides) == 1:
            self.__sides = [__sides[0] for i in range(self.sides_count)]
        elif len(__sides) != self.sides_count:
            self.__sides = [1 for i in range(self.sides_count)]
        else:
            self.__sides = list(__sides)

    def get_square(self):
        a, b, c = self.__sides[0], self.__sides[1], self.__sides[2]
        p = (a + b + c) * (1/2)
        square = round((((p - a) * (p - b) * (p - c)) * p) ** (1/2), 2)  # Формула Герона, вроде
        print(f'Площадь фигуры {type(self).__name__}: ', end='')
        return square


class Cube(Figure):
    sides_count = 12

    def __init__(self, __color, *__sides, filled=False):
        super().__init__(__color, *__sides, filled=False)
        if len(__sides) == 1:
            self.__sides = [__sides[0] for i in range(self.sides_count)]
        elif len(__sides) != self.sides_count:
            self.__sides = [1 for i in range(self.sides_count)]
        else:
            self.__sides = list(__sides)

    def get_volume(self):
        volume = self.__sides[0] ** 3
        print(f'Объём фигуры {type(self).__name__}: ', end='')
        return volume


circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)
triangle1 = Triangle((31, 24, 246), 7)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())
triangle1.set_color(233, 244, 211)
print(triangle1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())
triangle1.set_sides(12)
print(triangle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())

# Проверка площади (круга)
print(circle1.get_square())

# Проверка площади (треугольника)
print(triangle1.get_square())

# Проверка закрашенности фигур (честно, не понял, зачем они вообще здесь, если цвет присутствует в любом случае)
print(circle1.filled)
print(triangle1.filled)
print(cube1.filled)