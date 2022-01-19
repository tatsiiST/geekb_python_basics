class Road:

    __length = 0
    __width = 0

    def __init__(self, length, width):

        if length <= 0 or width <= 0:
            raise ValueError("length and width must be positive numbers", length, width)
        self.__length = length
        self.__width = width

    def calc_mass(self, density, thickness):

        if density <= 0 or thickness <= 0:
            raise ValueError("density and thickness must be positive numbers", density, thickness)
        return self.__width * self.__length * density * thickness


if __name__ == '__main__':
    road = Road(500, 10)
    print(f'total mass of asphalt {road.calc_mass(9.35, 5.5)} kg')