import pygame, random
from pygame.locals import *
from sys import exit
import math
import os, time, sys

screen_size_x = 650
screen_size_y = 680
screen = pygame.display.set_mode((screen_size_x, screen_size_y))
font = r"C:\Users\peyton.hecht\Downloads\Python - Pygame Simple Main Menu Selection\Retro.ttf"
clock = pygame.time.Clock()
level = 1

# Text Renderer
def text_format(message, textFont, textSize, textColor):
    newFont = pygame.font.Font(textFont, textSize)
    newText = newFont.render(message, 0, textColor)
    return newText


def game_over():
    my_font = pygame.font.SysFont("times new roman", 90)
    game_over_surface = my_font.render("YOU DIED", True, red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (screen_size_x / 2, screen_size_y / 4)
    screen.fill(black)
    screen.blit(game_over_surface, game_over_rect)
    show_score(0, red, "times", 20)
    pygame.display.flip()
    time.sleep(3)
    pygame.quit()
    sys.exit()


def show_score(choice, color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render(
        "                  Score : " + str(score) + " Level :" + str(level), True, color
    )
    score_rect = score_surface.get_rect()
    if choice == 1:
        score_rect.midtop = (screen_size_x / 10, 15)
    else:
        score_rect.midtop = (screen_size_x / 2, screen_size_y / 1.25)
    screen.blit(score_surface, score_rect)
    # pygame.display.flip()


# just some declarations
difficulty = 30  # 5 easy 20 medium 50 hard for obstacles
fps = 10
FPS = 30
il = 5
windowtiles = 80
CELLSIZE = 8

winsize = CELLSIZE * windowtiles
pygame.init()

# Center the Game Application
os.environ["SDL_VIDEO_CENTERED"] = "1"


black = (0, 0, 0)
white = (255, 255, 255)
bodycolor = (100, 200, 150)
foodcolor = (200, 23, 23)
obscolor = (23, 23, 200)
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
gray = pygame.Color(50, 50, 50)
yellow = pygame.Color(255, 255, 0)
burnt = pygame.Color(138, 54, 15)
darkblue = pygame.Color(72, 61, 139)

# direction of snake
left = -1, 0
right = 1, 0
up = 0, -1
down = 0, 1

snake = [(0, 0)] * il
foodpos = (0, 0)
newdirection = direction = right  # snake is moving right by default
score = 0
obstacles = []


def main_menu():

    menu = True

    selected = "start"

    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected = "start"
                elif event.key == pygame.K_DOWN:
                    selected = "quit"
                if event.key == pygame.K_RETURN:
                    if selected == "start":
                        print("Start")
                        menu = False
                    if selected == "quit":
                        pygame.quit()
                        quit()

        # Main Menu UI
        screen.fill(burnt)
        title = text_format("Wormy!", font, 90, darkblue)
        if selected == "start":
            text_start = text_format("START", font, 75, white)
        else:
            text_start = text_format("START", font, 75, black)
        if selected == "quit":
            text_quit = text_format("QUIT", font, 75, white)
        else:
            text_quit = text_format("QUIT", font, 75, black)

        title_rect = title.get_rect()
        start_rect = text_start.get_rect()
        quit_rect = text_quit.get_rect()

        # Main Menu Text
        screen.blit(title, (screen_size_x / 2 - (title_rect[2] / 2), 80))
        screen.blit(text_start, (screen_size_x / 2 - (start_rect[2] / 2), 300))
        screen.blit(text_quit, (screen_size_x / 2 - (quit_rect[2] / 2), 360))
        pygame.display.update()
        clock.tick(FPS)
        pygame.display.set_caption("Wormy - Peyton Hecht")


# Initialize the Game


main_menu()


pygame.init()

pygame.mixer.init(44100, -16, 2, 2048)

pygame.mixer.music.load(r"C:\Users\peyton.hecht\Downloads\bensound-epic.mp3")
pygame.mixer.music.play(100)
pygame.mixer.music.set_volume(0.6)


for i in range(1, difficulty):
    lo = random.randrange(1, windowtiles), random.randrange(
        1, windowtiles
    )  # last obstacle
    obstacles.append(lo)
    for j in range(1, random.randint(1, int(difficulty / 2))):
        if random.randint(1, 2) == 1:
            lo = (lo[0] + 1, lo[1])
        else:
            lo = (lo[0], lo[1] + 1)
        if 0 < lo[0] <= windowtiles and 0 < lo[1] <= windowtiles:
            obstacles.append(lo)


def rendertext(surface, text):
    font = pygame.font.Font(None, 22)
    text = font.render(text, 1, white)
    textpos = text.get_rect(centerx=surface.get_width() / 2, y=winsize + CELLSIZE)
    surface.blit(text, textpos)







if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((winsize, winsize + 35))
    pygame.display.set_caption("Python Snake")
    dead = False
    clock = pygame.time.Clock()
    while dead == False:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == K_UP:
                    if direction != down:
                        newdirection = up
                elif event.key == K_DOWN:
                    if direction != up:
                        newdirection = down
                elif event.key == K_LEFT:
                    if direction != right:
                        newdirection = left
                elif event.key == K_RIGHT:
                    if direction != left:
                        newdirection = right

        screen.fill(black)
        # update the snake
        # check if there is food
        direction = newdirection
        if foodpos == (0, 0):
            foodpos = random.randrange(1, windowtiles), random.randrange(1, windowtiles)
            while foodpos in snake or foodpos in obstacles:
                foodpos = random.randrange(1, windowtiles), random.randrange(
                    1, windowtiles
                )
        # update the snake
        head = snake[0]  # head of snake
        head = (head[0] + direction[0], head[1] + direction[1])
        # wrap the snake around the window
        headx = windowtiles if head[0] < 0 else 0 if head[0] > windowtiles else head[0]
        heady = windowtiles if head[1] < 0 else 0 if head[1] > windowtiles else head[1]
        head = (headx, heady)
        if head in snake or head in obstacles:
            level = 1
            game_over()

        else:
            if head == foodpos:
                foodpos = 0, 0
                score += 1
                snake.append(head)
            rendertext(screen, "Score : " + str(score) + " Level :" + str(level))
        snake = [head] + [snake[i - 1] for i in range(1, len(snake))]
        # draw world
        pygame.draw.rect(
            screen,
            foodcolor,
            (foodpos[0] * CELLSIZE, foodpos[1] * CELLSIZE, CELLSIZE, CELLSIZE),
            0,
        )
        for block in snake:
            pygame.draw.rect(
                screen,
                bodycolor,
                (block[0] * CELLSIZE, block[1] * CELLSIZE, CELLSIZE, CELLSIZE),
                0,
            )
        for block in obstacles:
            pygame.draw.rect(
                screen,
                obscolor,
                (block[0] * CELLSIZE, block[1] * CELLSIZE, CELLSIZE, CELLSIZE),
                0,
            )
        pygame.display.update()

        if level == 1 and score == 10:
            level += 1
            fps = 15
        if level == 2 and score == 20:
            level += 1
            fps = 20
        if level == 3 and score == 30:
            level += 1
            fps = 30
        if level == 4 and score == 40:
            level += 1
            fps = 40
        if level == 5 and score == 50:
            level += 1
            fps = 50
        if level == 6 and score == 60:
            level += 1
            fps = 75
        if level == 7 and score == 70:
            level += 1
            fps = 100
        show_score(1, white, "consolas", 20)



    while True:  # wait till the user clicks close button
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
