from turtle import Turtle
import random

CAR_WIDTH = 2

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5
NUM_OF_CARS = 20


class Car(Turtle):

    def __init__(self, color, start_pos):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=CAR_WIDTH)
        self.setpos(start_pos)
        self.setheading(180)
        self.color(color)

    def change_car(self, color, pos):
        self.setpos(pos)
        self.color(color)


class CarManager:

    def __init__(self, screen_width):
        self.cars = []
        self.collision = False
        for x in range(NUM_OF_CARS):
            self.cars.append(Car(random.choice(COLORS), (random.randint(-300, 300), random.randint(-250, 250))))

    def move_cars(self, player, points):
        for car in self.cars:
            car.fd(STARTING_MOVE_DISTANCE + (MOVE_INCREMENT * points))
            if car.xcor() < -350:
                car.change_car(random.choice(COLORS), (350, random.randint(-250, 250)))
            if abs(player.xcor() - car.xcor()) < 27 and abs((player.ycor() + 3) - car.ycor()) < 20:
                self.collision = True
