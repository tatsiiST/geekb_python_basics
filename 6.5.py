class Stationery:
    title = 'Stationery'

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    title = 'Pen'

    def draw(self):
        super().draw()
        print('\tрисуем ручкой')


class Pencil(Stationery):
    title = 'Pencil'

    def draw(self):
        super().draw()
        print('\tрисуем карандашом')


class Handle(Stationery):
    title = 'Handle'

    def draw(self):
        super().draw()
        print('\tрисуем маркером')


if __name__ == '__main__':
    pen = Pen()
    print(f'Инструмент: {pen.title}')
    pen.draw()

    pencil = Pencil()
    print(f'Инструмент: {pencil.title}')
    pencil.draw()

    handle = Handle()
    print(f'Инструмент: {handle.title}')
    handle.draw()