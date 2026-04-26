import pygame
import random
import json
from db import get_top10

file = "TSIS/snake_game/settings.json"
def load_settings():
    with open(file, 'r') as f:
        return json.load(f)
    
def save_settings(settings):
    with open(file, 'w') as f:
        json.dump(settings, f)

def toggle(settings, key):
    settings[key] = not settings[key]
    save_settings(settings)

def next_color(settings, COLOR_PALETTE):
    settings["color_index"] += 1
    if settings["color_index"] >= len(COLOR_PALETTE):
        settings["color_index"] = 0
    save_settings(settings)

def set_color(settings, color):
    settings["snake_color"] = color
    save_settings(settings)

def draw_grid(screen, cell_size=20, width=600, height=600):
    color = (40, 40, 40)
    for x in range(0, width, cell_size):
        pygame.draw.line(screen, color, (x, 0), (x, height))
    for y in range(0, height, cell_size):
        pygame.draw.line(screen, color, (0, y), (width, y))


def settings_menu(screen, font, settings, COLOR_PALETTE):
    screen.fill((0, 0, 0))
    current_color = COLOR_PALETTE[settings["color_index"]]
    color_text = font.render(f"C - COLOR {current_color}", True, current_color)
    grid_text = font.render(f"Z - GRID ({settings['grid']})", True, (255, 0, 0))
    sound_text = font.render(f"X - SOUND ({settings['sound']})", True, (255, 0, 0))
    back_text = font.render("B - BACK", True, (255, 0, 0))

    screen.blit(color_text, (200, 100))
    screen.blit(grid_text, (200, 150))
    screen.blit(sound_text, (200, 200))
    screen.blit(back_text, (200, 250))

    pygame.draw.rect(screen, current_color, (450, 100, 40, 40))

def leaderboard(screen, font):
    screen.fill((0, 0, 0))
    title = font.render("TOP 10", True, (255, 255, 0))
    screen.blit(title, (250, 50))

    data = get_top10()

    y = 120
    rank = 1

    for row in data:
        text = font.render(
            f"{rank}. {row[0]} | Score: {row[1]} | Level: {row[2]}",
            True,
            (255, 255, 255)
        )
        screen.blit(text, (100, y))
        y += 30
        rank += 1



class Snake():
    def __init__(self):
        self.body = [(300, 300)]
        self.dx = 20
        self.dy = 0
        self.is_grow = False

        self.collide_sound = "TSIS/snake_game/assets/gameover.mp3"
        self.eat_sound = "TSIS/snake_game/assets/food.mp3"
        self.powerup_sound = "TSIS/snake_game/assets/powerup.mp3"

        self.effects = {}

    def move(self):
        head = (self.body[0][0] + self.dx, self.body[0][1] + self.dy)
        self.body.insert(0, head)
        if not self.is_grow:
            self.body.pop()
        else:
            self.is_grow = False

    def grow(self):
        self.is_grow = True

    def shrink(self):
        for i in range(2):
            if len(self.body) > 1:
                self.body.pop()
            else:
                return True
        return False
    
    def apply_powerup(self, power_type):
        current_time = pygame.time.get_ticks()

        if power_type == "speed":
            self.effects["speed"] = current_time + 5000

        elif power_type == "slow":
            self.effects["slow"] = current_time + 5000

        elif power_type == "shield":
            self.effects["shield"] = True

    def update_effects(self):
        current_time = pygame.time.get_ticks()

        for effect in list(self.effects):
            if effect != "shield":
                if current_time > self.effects[effect]:
                    del self.effects[effect]

    def controls(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP] and self.dy == 0:
            self.dx, self.dy = 0, -20
        if keys[pygame.K_DOWN] and self.dy == 0:
            self.dx, self.dy = 0, 20
        if keys[pygame.K_LEFT] and self.dx == 0:
            self.dx, self.dy = -20, 0
        if keys[pygame.K_RIGHT] and self.dx == 0:
            self.dx, self.dy = 20, 0

    def draw(self, screen, color):
        for segment in self.body:
            pygame.draw.rect(screen, color, (*segment, 20, 20))

class Food():
    def __init__(self):
        self.position = self.random_pos()

        self.types = [
            {"value" : 1, "color" : (255, 0, 0)},
            {"value" : 2, "color" : (0, 0, 255)},
            {"value" : 3, "color" : (255, 255, 0)},
            {"value" : -2, "color" : (128, 0, 128)}
        ]
        
        self.respawn()
        self.lifetime = 5000

    def random_pos(self):
        return (random.randrange(0, 600, 20), random.randrange(60, 500, 20))
    
    def random_type(self):
        return (random.choice(self.types))
    
    def respawn(self):
        self.position = self.random_pos()
        self.type = self.random_type()
        self.spawn_time = pygame.time.get_ticks()

    def spawn_update(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.spawn_time > self.lifetime:
            self.respawn()

    def draw(self, screen):
        pygame.draw.rect(screen, self.type['color'], (*self.position, 20, 20))

class PowerUp():
    def __init__(self):
        self.types = [
            {"type": "speed", "color": (255, 255, 255)},
            {"type": "slow", "color": (255, 165, 0)},
            {"type": "shield", "color": (0, 165, 255)}
        ]

        self.lifetime = 8000
        self.respawn()

    def random_pos(self):
        return (random.randrange(0, 600, 20), random.randrange(60, 500, 20))

    def respawn(self):
        self.position = self.random_pos()
        self.type = random.choice(self.types)
        self.spawn_time = pygame.time.get_ticks()

    def update(self):
        current_time = pygame.time.get_ticks()

        if current_time - self.spawn_time >= self.lifetime:
            self.respawn()

    def draw(self, screen):
        pygame.draw.rect(screen, self.type["color"], (*self.position, 20, 20))

class Walls():
    def __init__(self, width, height, cell_size):
        self.width = width
        self.height = height
        self.cell = cell_size
        self.blocks = []

    def generate(self, level, snake_body, food_pos, powerup_pos=None):
        self.blocks = []

        if level < 3:
            return

        count = level * 4

        for _ in range(count):
            while True:
                pos = (random.randrange(0, self.width, self.cell), random.randrange(0, self.height, self.cell))

                if pos in snake_body:
                    continue
                if pos == food_pos:
                    continue
                if powerup_pos and pos == powerup_pos:
                    continue

                self.blocks.append(pos)
                break

    def check_collision(self, head):
        return head in self.blocks

    def draw(self, screen):
        for block in self.blocks:
            pygame.draw.rect(screen, (120, 120, 120), (*block, self.cell, self.cell))

