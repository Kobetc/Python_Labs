import uuid
import turtle
import time
import math


def drawText(text):
    textPen.clear()
    textPen.color("blue", "blue")
    textPen.penup()
    textPen.setpos(-400, 280)
    textPen.write(text, move=False, align="left", font=("Arial", 20, "normal"))


def printMessage(text):
    try:
        if not isinstance(text, str):
            raise ValueError(
                "Параметр text должен иметь тип str !")

        drawText(text)
        print(text)

    except ValueError as e:
        print(e)
        return


class Figure:

    #
    # Сдвиг многоугольника по X и Y
    #
    def move(self,  shiftX=0, shiftY=0):
        printMessage("Сдвиг фигуры")

        for point in range(self.nPoints):
            self.points[point] = (self.points[point][0] +
                                  shiftX, self.points[point][1] + shiftY)

    #
    # Рисование многоугольника
    #
    def draw(self):
        pen.up()
        pen.setpos(self.points[0][0],
                   self.points[0][1])
        pen.down()

        for index in range(1, self.nPoints):
            pen.setpos(self.points[index][0],
                       self.points[index][1])
        pen.setpos(self.points[0][0],
                   self.points[0][1])

    #
    # Проверка, включена ли фигура anotherFigure в self фигуру методом площадей
    #
    def is_include(self,  anotherFigure):

        try:
            if not (len(anotherFigure.points) > 0):
                raise ValueError(
                    "Фигура anotherFigure не имеет вершин !")

            if not (len(self.points) > 0):
                raise ValueError(
                    "Фигура self не имеет вершин !")

        except ValueError as e:
            printMessage(e)
            return

        # Беруться координаты X и Y вершин фигуры anotherFigure
        for anotherFigurePoint in range(anotherFigure.nPoints):
            try:
                anotherFigurePointX = anotherFigure.points[anotherFigurePoint][0]
                anotherFigurePointY = anotherFigure.points[anotherFigurePoint][1]
            except IndexError:
                printMessage("Что то пошло не так !")

            pointS = 0  # Площадь треугольников между вершинами фигуры anotherFigure и двумя вершинами self фигуры

            # Беруться координаты X и Y 2-х вершин self фигуры
            for point in range(self.nPoints):
                try:
                    pointX = self.points[point][0]
                    pointY = self.points[point][1]
                    pointX_prev = self.points[point - 1][0]
                    pointY_prev = self.points[point - 1][1]
                except IndexError:
                    printMessage("Что то пошло не так !")

                # Вычисляется площадь треугольника из 3-х точек, одной вершины фигуры anotherFigure и 2-х вершин self фигуры
                s = 0.5 * abs(((pointX - anotherFigurePointX) * (pointY_prev - anotherFigurePointY)) - (
                    (pointX_prev - anotherFigurePointX) * (pointY - anotherFigurePointY)))

                # Площади треугольников складываются
                pointS = pointS + s

            # Площадь треугольников хоть для одной вершины фигуры anotherFigure получится больше прощади self фигуры
            # значит фигура anotherFigure не полностью входит в self фигуру
            if pointS > self.s:
                printMessage("Другая фигура НЕ включена в текущую фигуру")

                return

        printMessage("Другая фигура включена в текущую фигуру")

        return


class Rectangle (Figure):

    #
    # Конструктор класса прямоугольника
    #
    def __init__(self, width, height, posX=0, posY=0):
        self.id = uuid.uuid4()              # Уникальный идентификатор
        self.nPoints = 4                    # Число вершин

        try:
            if width <= 0 or height <= 0:
                raise ValueError(
                    "Значения длины и ширины должны быть больше 0 !")

            self.width = width      # Ширина прямоугольника
            self.height = height    # Высота прямоугольника

        except ValueError as e:
            printMessage(e)
            self.width = 500     # Ширина прямоугольника при ошибке ввода
            self.height = 400    # Высота прямоугольника при ошибке ввода

        self.s = self.width * self.height   # Площадь прямоугольника

        # Начальная координата X нижней левой вершины прямоугольника
        self.posX = posX
        # Начальная координата Y нижней левой вершины прямоугольника
        self.posY = posY

        # Координаты верщин прямоугольника
        self.points = [(self.posX, self.posY), (self.posX + self.width, self.posY), (self.posX + self.width,
                                                                                     self.posY + self.height), (self.posX, self.posY + self.height)]


class Pentagon (Figure):

    #
    # Конструктор класса пятиугольника
    #
    def __init__(self, radius, posX=0, posY=0, startAngle=0):
        self.id = uuid.uuid4()      # Уникальный идентификатор
        self.nPoints = 5            # Число вершин

        try:
            if radius <= 0:
                raise ValueError(
                    "Значение описанного радиуса пятиугольника должно быть больше 0 !")

            self.radius = radius    # Радиус описанной окружности пятиугольника

        except ValueError as e:
            printMessage(e)
            self.radius = 100    # Радиус описанной окружности пятиугольника при ошибке ввода

        # Площадь аятиугольника
        self.s = (self.nPoints/2 * (self.radius ** 2)
                  * math.sin(2 * math.pi / self.nPoints))

        self.points = []            # координаты верщин пятиугольника

        rad = 2 * math.pi / 360
        angle = 0 + startAngle

        # Вычисляем координаты верщин пятиугольника
        for _ in range(self.nPoints):
            try:
                coordX = int(math.sin(angle * rad) * self.radius) + posX
                coordY = int(math.cos(angle * rad) * self.radius) + posY

                self.points.append((coordX, coordY))

                angle = angle + 360 // 5
            except:
                printMessage("Что то пошло не так !")


textPen = turtle.Turtle()
pen = turtle.Turtle()

turtle.screensize(900, 600)

rectangle = Rectangle(450, 350, -250, -150)
pentagon = Pentagon(100, -100, -100)

rectangle.draw()
pentagon.draw()
rectangle.is_include(pentagon)

for count in range(4):
    time.sleep(2)
    pentagon.move(100, 50)
    pentagon.draw()
    rectangle.is_include(pentagon)

turtle.done()
