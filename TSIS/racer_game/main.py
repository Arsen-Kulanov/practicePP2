import pygame, sys, random
from pygame.locals import *

from racer import *
from ui import *
from persistence import *

pygame.init()

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
LANES = [80, 200, 320]

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Racer")

clock = pygame.time.Clock()
font = pygame.font.SysFont("Verdana", 20)
big_font = pygame.font.SysFont("Verdana", 50)

bg = pygame.image.load("TSIS/racer_game/assets/racer_bg.png")
bg = pygame.transform.scale(bg, (SCREEN_WIDTH, SCREEN_HEIGHT))

settings = load_settings()


def get_name():
    name = ""
    while True:
        screen.fill((255,255,255))
        draw_text(screen, "Enter name:", font, 120, 200)
        draw_text(screen, name, font, 120, 250)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if event.key == K_RETURN and name:
                    return name
                elif event.key == K_BACKSPACE:
                    name = name[:-1]
                else:
                    if len(name) < 10:
                        name += event.unicode

        pygame.display.update()
        clock.tick(60)


def game(username):

    P1 = Player(LANES)
    enemies = pygame.sprite.Group(Enemy(LANES))
    coins = pygame.sprite.Group(Coin(LANES))
    obstacles = pygame.sprite.Group(Obstacle(LANES))
    powerups = pygame.sprite.Group(PowerUp(LANES))

    SCORE = 0
    COINS = 0
    distance = 0

    SPEED = 5

    active_power = None
    power_end = 0

    while True:

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        screen.blit(bg, (0,0))

        P1.move()

        SPEED = 5 + COINS // 5

        if active_power == "nitro":
            SPEED += 5

        distance += SPEED * 0.1

        for e in enemies:
            if e.move(SPEED, SCREEN_HEIGHT):
                SCORE += 10

        for c in coins:
            c.move(SPEED, SCREEN_HEIGHT)

        for o in obstacles:
            o.move(SPEED, SCREEN_HEIGHT)

        for p in powerups:
            p.move(SPEED, SCREEN_HEIGHT)

        if pygame.sprite.spritecollideany(P1, enemies):
            if active_power != "shield":
                if settings['sound']:
                    pygame.mixer.music.load("TSIS/racer_game/assets/crash.mp3")
                    pygame.mixer.music.play()
                add_score(username, SCORE, distance)
                return SCORE, COINS, distance
            else:
                active_power = None

        hit_coin = pygame.sprite.spritecollideany(P1, coins)
        if hit_coin:
            COINS += hit_coin.value
            SCORE += hit_coin.value * 5
            hit_coin.load()

        hit_ob = pygame.sprite.spritecollideany(P1, obstacles)
        if hit_ob:
            if hit_ob.effect == "crash":
                if active_power != "shield":
                    if settings['sound']:
                        pygame.mixer.music.load("TSIS/racer_game/assets/crash.mp3")
                        pygame.mixer.music.play()
                    add_score(username, SCORE, distance)
                    return SCORE, COINS, distance
                else:
                    active_power = None

            elif hit_ob.effect == "slow":
                SPEED = max(2, SPEED - 2)

            elif hit_ob.effect == "slip":
                P1.lane_index = max(0, min(2, P1.lane_index + random.choice([-1,1])))

            hit_ob.load()

        hit_power = pygame.sprite.spritecollideany(P1, powerups)
        if hit_power and active_power is None:
            active_power = hit_power.name

            if hit_power.duration:
                power_end = pygame.time.get_ticks() + hit_power.duration

            if hit_power.name == "repair":
                active_power = "repair"
                power_end = pygame.time.get_ticks() + 1000

            hit_power.load()

        if active_power and power_end:
            if pygame.time.get_ticks() > power_end:
                active_power = None

        if active_power:
            draw_text(screen, active_power.upper(), font, 160, 70)
            
        for e in enemies:
            screen.blit(e.image, e.rect)

        for c in coins:
            screen.blit(c.image, c.rect)

        for o in obstacles:
            screen.blit(o.image, o.rect)

        for p in powerups:
            screen.blit(p.image, p.rect)

        screen.blit(P1.image, P1.rect)

        draw_text(screen, f"Score: {SCORE}", font, 10, 10)
        draw_text(screen, f"Coins: {COINS}", font, 250, 10)
        draw_text(screen, f"Dist: {int(distance)}", font, 140, 10)

        if active_power:
            draw_text(screen, f"Power: {active_power}", font, 120, 40)

        if active_power == "repair":
            draw_text(screen, "REPAIR", font, 160, 70)

        pygame.display.update()
        clock.tick(60)


def game_over_screen(username, score, coins, distance):
    while True:
        screen.fill((255,255,255))

        draw_text(screen, "GAME OVER", big_font, 80, 80)

        draw_text(screen, f"Score: {score}", font, 120, 180)
        draw_text(screen, f"Coins: {coins}", font, 120, 220)
        draw_text(screen, f"Distance: {int(distance)}", font, 120, 260)

        draw_text(screen, "R - Retry | M - Menu", font, 90, 500)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if event.key == pygame.K_r:
                    return "retry"

                if event.key == pygame.K_m:
                    return "menu"

        pygame.display.update()
        clock.tick(60)


def leaderboard_screen():
    data = load_leaderboard()

    while True:
        screen.fill((255,255,255))
        draw_text(screen, "TOP 10", big_font, 120, 50)

        y = 120
        for i, d in enumerate(data):
            draw_text(screen, f"{i+1}. {d['name']} {d['score']} ({d['distance']})", font, 50, y)
            y += 30

        draw_text(screen, "B - Back", font, 100, 500)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if event.key == K_b:
                    return

        pygame.display.update()


def settings_screen():
    while True:
        screen.fill((255,255,255))

        draw_text(screen, "SETTINGS", big_font, 100, 80)

        draw_text(screen, f"S - Sound: {settings['sound']}", font, 100, 180)
        draw_text(screen, f"D - Difficulty: {settings['difficulty']}", font, 100, 220)
        draw_text(screen, "B - Back", font, 100, 300)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if event.key == K_s:
                    settings["sound"] = not settings["sound"]
                    save_settings(settings)

                elif event.key == K_d:
                    if settings["difficulty"] == "easy":
                        settings["difficulty"] = "medium"
                    elif settings["difficulty"] == "medium":
                        settings["difficulty"] = "hard"
                    else:
                        settings["difficulty"] = "easy"

                    save_settings(settings)

                elif event.key == K_b:
                    return

        pygame.display.update()


def main_menu():
    while True:
        screen.fill((255,255,255))

        draw_text(screen, "P - Play", font, 120, 180)
        draw_text(screen, "L - Leaderboard", font, 120, 220)
        draw_text(screen, "S - Settings", font, 120, 260)
        draw_text(screen, "Q - Quit", font, 120, 300)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:

                if event.key == K_p:
                    name = get_name()
                    result = game(name)
                    score, coins, dist = result
                    action = game_over_screen(name, score, coins, dist)
                    if action == "retry":
                        name = get_name()
                        result = game(name)
                        score, coins, dist = result
                        game_over_screen(name, score, coins, dist)

                elif event.key == K_l:
                    leaderboard_screen()

                elif event.key == K_s:
                    settings_screen()

                elif event.key == K_q:
                    pygame.quit()
                    sys.exit()

        pygame.display.update()
        clock.tick(60)


main_menu()