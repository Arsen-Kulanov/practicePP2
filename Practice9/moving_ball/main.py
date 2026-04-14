import pygame
from ball import Ball

pygame.init()

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
pygame.display.set_caption("Moving Ball")
ball = Ball()

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break
        ball.move()

    screen.fill((0, 0, 0))
    screen.blit(ball.image, ball.rect)
    pygame.display.update()

    clock.tick(60)

pygame.quit()