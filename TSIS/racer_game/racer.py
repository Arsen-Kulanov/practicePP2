import pygame
import random


class Player(pygame.sprite.Sprite):
    def __init__(self, lanes):
        super().__init__()
        self.lanes = lanes
        self.lane_index = 1

        self.image = pygame.image.load("TSIS/racer_game/assets/Car_Player.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 100))

        self.rect = self.image.get_rect()
        self.rect.center = (self.lanes[self.lane_index], 520)

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and self.lane_index > 0:
            self.lane_index -= 1
            pygame.time.wait(120)

        if keys[pygame.K_RIGHT] and self.lane_index < len(self.lanes) - 1:
            self.lane_index += 1
            pygame.time.wait(120)

        self.rect.centerx = self.lanes[self.lane_index]

class Enemy(pygame.sprite.Sprite):
    def __init__(self, lanes):
        super().__init__()
        self.lanes = lanes

        self.image = pygame.image.load("TSIS/racer_game/assets/Car_Enemy.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 100))

        self.rect = self.image.get_rect()
        self.reset()

    def reset(self):
        self.rect.center = (random.choice(self.lanes), 0)

    def move(self, speed, height):
        self.rect.move_ip(0, speed)
        if self.rect.top > height:
            self.reset()
            return True
        return False

class Coin(pygame.sprite.Sprite):
    def __init__(self, lanes):
        super().__init__()
        self.lanes = lanes
        self.load()

    def load(self):
        self.value = random.choice([1,3,5])
        self.image = pygame.image.load("TSIS/racer_game/assets/coin.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (30,30))
        self.rect = self.image.get_rect()
        self.rect.center = (random.choice(self.lanes), random.randint(-600,-50))

    def move(self, speed, height):
        self.rect.move_ip(0, speed)
        if self.rect.top > height:
            self.load()

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, lanes):
        super().__init__()
        self.lanes = lanes

        self.types = [
            {"effect": "crash"},
            {"effect": "slow"},
            {"effect": "slip"},
        ]

        self.load()

    def load(self):
        t = random.choice(self.types)
        self.effect = t["effect"]

        self.image = pygame.image.load("TSIS/racer_game/assets/oil.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))

        self.rect = self.image.get_rect()
        self.rect.center = (random.choice(self.lanes), random.randint(-600, -50))

    def move(self, speed, height):
        self.rect.move_ip(0, speed)

        if self.rect.top > height:
            self.load()

class PowerUp(pygame.sprite.Sprite):
    def __init__(self, lanes):
        super().__init__()
        self.lanes = lanes

        self.types = [
            {"name": "nitro", "time": 4000},
            {"name": "shield", "time": None},
            {"name": "repair", "time": 0},
        ]

        self.load()

    def load(self):
        t = random.choice(self.types)
        self.name = t["name"]
        self.duration = t["time"]

        self.image = pygame.image.load("TSIS/racer_game/assets/powerup.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (35, 35))

        self.rect = self.image.get_rect()
        self.rect.center = (random.choice(self.lanes), random.randint(-700, -100))

        self.spawn_time = pygame.time.get_ticks()

    def move(self, speed, height):
        self.rect.move_ip(0, speed)

        if self.rect.top > height:
            self.load()