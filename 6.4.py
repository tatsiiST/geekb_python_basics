class WordSide:

    __possible_sides = ['NORTH', 'EAST', 'SOUTH', 'WEST']
    __current_idx = 0

    def __init__(self, side='NORTH'):
        self.side = side

    def __set_side(self, side: str):
        if not side.upper() in WordSide.__possible_sides:
            raise TypeError('Wrong side', side)
        else:
            self.__current_idx = WordSide.__possible_sides.index(side.upper())

    def __get_side(self):
        return WordSide.__possible_sides[self.__current_idx]

    def turn(self, str_direction: str):
        if str_direction.lower() == 'right':
            self.__current_idx += 1

        elif str_direction.lower() == 'left':
            self.__current_idx -= 1
        else:
            raise TypeError(f"Wrong direction {str_direction} Should be 'left' or 'right'")
        self.__current_idx %= 4
    side = property(__get_side, __set_side)


class Car:

    speed = 0
    color = 'black'
    name = 'Some car'
    is_police = False

    __current_direction = WordSide()

    def __init__(self, name, **kwargs):
        # todo check kwargs
        for k, v in kwargs.items():
            setattr(self, k, v)
        self.name = name

    def __set_direction(self, direction):
        self.__current_direction.side = direction

    def go(self, speed):

        if not type(speed) in (float, int):
            raise TypeError('Only numeric speed supported')
        if speed < 0:
            raise ValueError('Only positive speed supported')
        self.speed = speed
        print(f'"{self.name}" started')

    def stop(self):

        self.speed = 0
        print(f'"{self.name}" stopped')

    def __get_direction(self):
        return self.__current_direction.side

    def turn(self, direction: str):

        self.__current_direction.turn(direction)
        print(f'"{self.name}" going to the {self.direction}')

    def show_speed(self):

        print(f'"{self.name}" have current speed {self.speed} km/h')

    direction = property(__get_direction, __set_direction)


class TownCar(Car):
    _speed_limit = 60

    def show_speed(self):
        super().show_speed()
        if self.speed > self._speed_limit:
            print(f'!!!Speed limit!!!')


class WorkCar(TownCar):
    _speed_limit = 40


class SportCar(Car):
    pass


class PoliceCar(Car):
    is_police = True


if __name__ == '__main__':
    tc = TownCar('Kia Rio', color='blue')
    tc.go(40)
    tc.show_speed()
    tc.turn('left')
    tc.show_speed()
    tc.go(90)
    tc.show_speed()
    tc.stop()
    tc.show_speed()

    wc = WorkCar('Gaz', color='yellow', direction='north')
    wc.go(40)
    wc.show_speed()
    print(wc.direction)
    wc.turn('right')
    wc.turn('right')
    wc.turn('left')
    wc.go(41)
    wc.show_speed()