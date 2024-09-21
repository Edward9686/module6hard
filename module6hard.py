import math


class Figure:
    sides_count = 0

    def __init__(self, color=None, *sides):
        self._sides = []
        self.__color = color if color is not None else []
        self.filled = False
        self.set_sides(*sides)

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        return all(isinstance(x, int) and 0 <= x <= 255 for x in (r, g, b))

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = (r, g, b)

    def __is_valid_sides(self, *new_sides):
        return len(new_sides) == self.sides_count and all(isinstance(side, int) and side > 0 for side in new_sides)

    def get_sides(self):
        return self._sides

    def __len__(self):
        return sum(self._sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self._sides = list(new_sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color=None, circumference=1):
        super().__init__(color, circumference)
        self.__radius = circumference / (2 * math.pi)

    def get_square(self):
        return math.pi * (self.__radius ** 2)

    def get_radius(self):
        return self.__radius


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color=None, *sides):
        super().__init__(color, *sides)

    def get_square(self):
        """Возвращает площадь треугольника по формуле Герона"""
        a, b, c = self._sides
        s = (a + b + c) / 2
        return math.sqrt(s * (s - a) * (s - b) * (s - c))


class Cube(Figure):
    sides_count = 12

    def __init__(self, color=None, side_length=1):
        sides = [side_length] * Cube.sides_count
        super().__init__(color, *sides)

    def get_volume(self):
        return self._sides[0] ** 3


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
# кароче капец, _sides с одним подчёркиванием у меня, иначе ошибку выдаёт
