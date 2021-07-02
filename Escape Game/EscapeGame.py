import pygame
import sys
import random

screen_size = [360, 640]
screen = pygame.display.set_mode(screen_size)

background = pygame.image.load("background.png")
user = pygame.image.load("user.png")
chicken = pygame.image.load("chicken.png")


def display_game(s):
    pygame.init()
    myfont = pygame.font.SysFont("monospace", 30)
    text_img = myfont.render("Score: {0}".format(s), 1, (0, 255, 0))
    screen.blit(text_img, [20, 10])


def random_offset():
    return random.randint(100, 1500)


chicken_y = [random_offset(), random_offset(), random_offset(), random_offset()]
score = 0


def crashed(idx):
    global score
    global keep_alive
    score = score - 10
    chicken_y[idx] = random_offset()*-1
    if score < -800:
        keep_alive = False


def update_chicken(idx):
    global score
    if chicken_y[idx] > 640:
        chicken_y[idx] = random_offset()*-1
        score = score + 10
    else:
        chicken_y[idx] = chicken_y[idx] + 5


keep_alive = True


def main():
    user_x = 150
    while keep_alive:
        pygame.event.get()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] and user_x < 280:
            user_x = user_x + 10
        elif keys[pygame.K_LEFT] and user_x > 0:
            user_x = user_x - 10

        update_chicken(0)
        update_chicken(1)
        update_chicken(2)
        update_chicken(3)

        clock = pygame.time.Clock()
        screen.blit(background, (0, 0))
        screen.blit(user, (user_x, 555))
        screen.blit(chicken, (10, chicken_y[0]))
        screen.blit(chicken, (100, chicken_y[1]))
        screen.blit(chicken, (185, chicken_y[2]))
        screen.blit(chicken, (270, chicken_y[3]))
        clock.tick(60)

        if chicken_y[0] > 490 and user_x < 70:
            crashed(0)
        if chicken_y[1] > 490 and user_x > 75 and user_x < 165:
            crashed(1)
        if chicken_y[2] > 490 and user_x > 170 and user_x < 260:
            crashed(2)
        if chicken_y[3] > 490 and user_x > 265:
            crashed(3)

        display_game(score)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


main()