import pygame
from snake import *
from db import save_game, get_top10

pygame.init()

screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

settings = load_settings()

username = ""
game_saved = False

COLOR_PALETTE = [
    [0, 255, 0],
    [255, 0, 0],
    [0, 0, 255],
    [255, 255, 0],
    [255, 165, 0],
    [128, 0, 128]
]

snake = Snake()
food = Food()
powerup = PowerUp()
walls = Walls(600, 600, 20)

state = "menu"

score = 0
level = 1
to_next_level = 4

run = True

def reset_game():
    global snake, food, powerup, walls, score, level, game_saved
    snake = Snake()
    food = Food()
    powerup = PowerUp()
    walls = Walls(600, 600, 20)
    score = 0
    level = 1
    game_saved = False


while run:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False

        if state == "menu":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and username:
                    state = "game"
                elif event.key == pygame.K_BACKSPACE:
                    username = username[:-1]
                elif event.key == pygame.K_F1:
                    state = "leaderboard"
                elif event.key == pygame.K_F2:
                    state = "settings"
                elif event.key == pygame.K_F3:
                    run = False
                else:
                    if len(username) < 12:
                        username += event.unicode

        elif state == "settings":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_z:
                    toggle(settings, "grid")
                elif event.key == pygame.K_x:
                    toggle(settings, "sound")
                elif event.key == pygame.K_c:
                    next_color(settings, COLOR_PALETTE)
                elif event.key == pygame.K_b:
                    state = "menu"

        elif state == "leaderboard":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    state = "menu"

        elif state == "game_over":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    reset_game()
                    state = "game"
                elif event.key == pygame.K_m:
                    state = "menu"

    if state == "menu":
        screen.fill((0, 0, 0))
        screen.blit(font.render("SNAKE GAME", True, (0, 255, 0)), (200, 160))
        screen.blit(font.render("ENTER NAME:", True, (255, 255, 255)), (200, 200))
        screen.blit(font.render(username, True, (0, 255, 0)), (200, 250))
        screen.blit(font.render("ENTER - PLAY", True, (150, 150, 150)), (200, 300))
        screen.blit(font.render("F1 - LEADERBOARD", True, (150, 150, 150)), (200, 340))
        screen.blit(font.render("F2 - SETTINGS", True, (150, 150, 150)), (200, 380))
        screen.blit(font.render("F3 - QUIT", True, (150, 150, 150)), (200, 420))
        pygame.display.update()
        clock.tick(10)
        continue

    elif state == "settings":
        settings_menu(screen, font, settings, COLOR_PALETTE)
        pygame.display.update()
        clock.tick(10)
        continue

    elif state == "leaderboard":
        screen.fill((0, 0, 0))
        screen.blit(font.render("TOP 10", True, (255, 255, 0)), (240, 50))

        data = get_top10()

        y = 120
        rank = 1
        for row in data:
            text = font.render(
                f"{rank}. {row[0]} | {row[1]} pts | L{row[2]}",
                True,
                (255, 255, 255)
            )
            screen.blit(text, (80, y))
            y += 30
            rank += 1

        screen.blit(font.render("B - BACK", True, (255, 0, 0)), (220, 520))

        pygame.display.update()
        clock.tick(10)
        continue

    elif state == "game":

        prev_body = snake.body.copy()

        snake.controls()
        snake.move()
        snake.update_effects()

        food.spawn_update()
        powerup.update()

        next_head = snake.body[0]

        if next_head == food.position:
            if settings['sound']:
                pygame.mixer.music.load(snake.eat_sound)
                pygame.mixer.music.play()
            if food.type["value"] == -2:
                score += food.type["value"]
                if snake.shrink():
                    state = "game_over"
            else:
                score += food.type["value"]
                snake.grow()

            food.respawn()

            if score > 0 and score % to_next_level == 0:
                level += 1
                walls.generate(level, snake.body, food.position, powerup.position)

        if next_head == powerup.position:
            if settings['sound']:
                pygame.mixer.music.load(snake.powerup_sound)
                pygame.mixer.music.play()
            snake.apply_powerup(powerup.type["type"])
            powerup.respawn()

        x, y = next_head
        dead = False

        if x < 0 or x >= 600 or y < 0 or y >= 600:
            dead = True

        if next_head in snake.body[1:] and "shield" not in snake.effects:
            dead = True

        if walls.check_collision(next_head):
            dead = True

        if dead:
            if "shield" in snake.effects:
                snake.body = prev_body
                del snake.effects["shield"]
            else:
                if settings['sound']:
                    pygame.mixer.music.load(snake.collide_sound)
                    pygame.mixer.music.play()
                state = "game_over"

        screen.fill((0, 0, 0))

        if settings['grid']:
            draw_grid(screen)

        snake.draw(screen, COLOR_PALETTE[settings['color_index']])
        food.draw(screen)
        powerup.draw(screen)
        walls.draw(screen)

        screen.blit(font.render(f"Score: {score}", True, (255, 255, 255)), (10, 10))
        screen.blit(font.render(f"Level: {level}", True, (255, 255, 255)), (10, 40))

        base_speed = 8 + level * 2
        speed = base_speed

        if "speed" in snake.effects:
            speed += 10
        elif "slow" in snake.effects:
            speed = max(3, base_speed - 3)

        pygame.display.update()
        clock.tick(speed)

    elif state == "game_over":

        if not game_saved:
            save_game(username, score, level)
            game_saved = True

        screen.fill((0, 0, 0))
        screen.blit(font.render("GAME OVER", True, (255, 0, 0)), (200, 200))
        screen.blit(font.render("R - Retry", True, (255, 255, 255)), (220, 260))
        screen.blit(font.render("M - Menu", True, (255, 255, 255)), (220, 300))
        screen.blit(font.render(f"Score: {score}", True, (255, 255, 255)), (110, 360))
        screen.blit(font.render(f"Level: {level}", True, (255, 255, 255)), (270, 360))

        pygame.display.update()
        clock.tick(10)

pygame.quit()