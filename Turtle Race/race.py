import turtle
import time
import random

SCREEN_WIDTH, SCREEN_HEIGHT = 700, 600
COLORS = ['red', 'green', 'blue', 'orange', 'yellow', 'black', 'purple', 'pink', 'brown', 'cyan']


def get_number_of_racers():
    racer = 0
    while True:
        racer = input('Enter the number of racers(2 - 10): ')
        if racer.isdigit():
            racer = int(racer)
            if 2 <= racer <= 10:
                return racer
            else:
                print('Number not in range 2-10. Please Try Again!')
        else:
            print('Input is not numeric... Please Try Again!')


def race(color):
    turtles = create_turtles(color)

    while True:
        for racer in turtles:
            distance = random.randrange(1, 20)
            racer.forward(distance)

            x, y = racer.pos()
            if y >= SCREEN_HEIGHT // 2 - 10:
                return color[turtles.index(racer)]


def create_turtles(color):
    turtles = []
    spacingX = SCREEN_WIDTH // (len(color) + 1)
    for i, col in enumerate(color):
        racer = turtle.Turtle()
        racer.color(col)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        racer.setpos(- SCREEN_WIDTH // 2 + (i + 1) * spacingX, - SCREEN_HEIGHT // 2 + 20)
        racer.pendown()
        turtles.append(racer)

    return turtles


def init_turtle():
    screen = turtle.Screen()
    screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
    screen.title('Turtle Racing!')


def main():
    while True:
        racers = get_number_of_racers()
        init_turtle()

        random.shuffle(COLORS)
        colors = COLORS[:racers]

        winner = race(colors)
        print("The winner is the turtle with color:", winner)
        time.sleep(2)

        ans = input("Do you wanna play again? (Y/N): ")
        ans = ans.lower()
        if ans == 'n' or ans == 'no':
            break


if __name__ == "__main__":
    main()