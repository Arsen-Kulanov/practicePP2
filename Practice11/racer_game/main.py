import pygame, sys
from pygame.locals import *
import random, time

pygame.init()

FPS = 60
FramePerSec = pygame.time.Clock()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED   = (255, 0, 0)

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

BASE_SPEED = 5
SPEED = BASE_SPEED

SCORE = 0
COINS = 0

COINS_FOR_SPEED_UP = 5

font_small = pygame.font.SysFont("Verdana", 20)
font_big = pygame.font.SysFont("Verdana", 60)

game_over = font_big.render("Game Over", True, BLACK)

background = pygame.image.load("Practice10/racer_game/images/racer_bg.jpg")
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Racer Game")


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("Practice10/racer_game/images/Car_Enemy.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 100))

        self.rect = self.image.get_rect()
        self.reset()

    def reset(self):
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        global SCORE

        self.rect.move_ip(0, SPEED)

        if self.rect.top > SCREEN_HEIGHT:
            SCORE += 1
            self.reset()


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("Practice10/racer_game/images/Car_Player.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 100))

        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()

        if self.rect.left > 0 and pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)

        if self.rect.right < SCREEN_WIDTH and pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)


class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.types = [
            {"value": 1, "size": 25},
            {"value": 3, "size": 30},
            {"value": 5, "size": 35},
        ]

        self.load_new_coin()

    def load_new_coin(self):
        coin_type = random.choice(self.types)

        self.value = coin_type["value"]

        self.image = pygame.image.load("Practice10/racer_game/images/coin.png").convert_alpha()

        self.image = pygame.transform.scale(self.image, (coin_type["size"], coin_type["size"]))

        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), random.randint(-600, -50))

    def move(self):
        self.rect.move_ip(0, SPEED)

        if self.rect.top > SCREEN_HEIGHT:
            self.load_new_coin()


P1 = Player()
E1 = Enemy()
C1 = Coin()

enemies = pygame.sprite.Group(E1)
coins = pygame.sprite.Group(C1)

all_sprites = pygame.sprite.Group(P1, E1, C1)

crash_sound = pygame.mixer.Sound("Practice10/racer_game/images/crash.mp3")


while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    DISPLAYSURF.blit(background, (0, 0))

    score_text = font_small.render(f"Score: {SCORE}", True, BLACK)
    DISPLAYSURF.blit(score_text, (10, 10))

    coin_text = font_small.render(f"Coins: {COINS}", True, BLACK)
    DISPLAYSURF.blit(coin_text, (SCREEN_WIDTH - 120, 10))

    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()

    if pygame.sprite.spritecollideany(P1, enemies):
        crash_sound.play()
        time.sleep(0.5)

        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30, 250))

        pygame.display.update()
        time.sleep(2)

        pygame.quit()
        sys.exit()

    if pygame.sprite.spritecollideany(P1, coins):
        COINS += C1.value
        C1.load_new_coin()

        SPEED = BASE_SPEED + (COINS // COINS_FOR_SPEED_UP)

    pygame.display.update()
    FramePerSec.tick(FPS)