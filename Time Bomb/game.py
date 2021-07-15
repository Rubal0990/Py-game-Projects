import math
import random
import time
import pygame

# Game Variables
screen_width = 480
screen_height = 480
gridsize = 20
grid_width = screen_width / gridsize
grid_height = screen_height / gridsize

# Setup display
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height), 0, 32)
pygame.display.set_caption("Bomb Game!!")

# Fonts
myfont = pygame.font.SysFont("monospace", 40)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Choice variables
RADIUS = 20
GAP = 25
letters = []
startx = 120
# print(startx)
starty = 250
A = 49
for i in range(3):
    x = startx + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13))
    y = starty + ((i // 13) * (GAP + RADIUS * 2))
    letters.append([x, y, chr(A + i)])
# print(letters[0])

clock = pygame.time.Clock()


def no_display(t, number):
    while t:
        mins = t // 60
        secs = t % 60
        t -= 1

        drawGrid(screen)

        text = myfont.render(f'{mins}:{secs}', 1, BLACK)
        screen.blit(text, (screen_width / 2 - text.get_width() / 2, 80))
        text = myfont.render("Memorize the no.", 1, BLACK)
        screen.blit(text, (screen_width / 2 - text.get_width() / 2, 160))
        text = myfont.render(f"{number}", 1, BLACK)
        screen.blit(text, (screen_width / 2 - text.get_width() / 2, 200))

        pygame.display.update()
        pygame.time.delay(1000)


def Level_selector(lvl):
    global t

    if lvl == 1:
        t = 15
    elif lvl == 2:
        t = 10
    elif lvl == 3:
        t = 5

    return t


def drawGrid(surface):
    for y in range(0, int(grid_height)):
        for x in range(0, int(grid_width)):
            if (x + y) % 2 == 0:
                r = pygame.Rect((x * gridsize, y * gridsize), (gridsize, gridsize))
                pygame.draw.rect(surface, (93, 216, 228), r)
            else:
                rr = pygame.Rect((x * gridsize, y * gridsize),
                                 (gridsize, gridsize))
                pygame.draw.rect(surface, (84, 194, 205), rr)


def Welcome():
    screen.fill((255, 255, 255))
    text = myfont.render("Let's Play", 1, BLACK)
    screen.blit(text, (screen_width / 2 - text.get_width() / 2, 40))
    text = myfont.render("Choose a level", 1, BLACK)
    screen.blit(text, (screen_width / 2 - text.get_width() / 2, 160))
    for letter in letters:
        x, y, ltr = letter
        pygame.draw.circle(screen, BLACK, (x, y), RADIUS, 3)
        text = myfont.render(ltr, 1, BLACK)
        screen.blit(text, (x - text.get_width() / 2, y - text.get_height() / 2))

    pygame.display.update()


run = True
while run:
    clock.tick(60)
    found = True

    Welcome()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            m_x, m_y = pygame.mouse.get_pos()
            while found:
               for letter in letters:
                    x, y, ltr = letter
                    dis = math.sqrt((x - m_x)**2 + (y - m_y)**2)
                    if dis < RADIUS:
                        t = Level_selector(int(ltr))
                        found = False

            number = random.randint(10000, 99999)
            no_display(t, number)

            ans = int(input("Enter the number:"))

            if ans == number:
                print("Bomb Deactivated! Your are safe")
            else:
                print("Booommmmmmm!!!!")

            y_n = input("Do you wanna play again? (Y/N): ")
            y_n = y_n.lower()
            if y_n == 'n' or y_n == 'no':
                run = False


pygame.quit()
