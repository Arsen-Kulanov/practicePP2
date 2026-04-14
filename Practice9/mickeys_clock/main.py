import pygame
from datetime import datetime
from clock import rotate

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Mickeys Clock")
clock = pygame.time.Clock()
background = pygame.image.load("Practice9/mickeys_clock/images/mickeyclock.png")
background = pygame.transform.scale(background, (800, 600))
center = (400, 300)

right_hand = pygame.image.load("Practice9/mickeys_clock/images/rightarm.png")
left_hand = pygame.image.load("Practice9/mickeys_clock/images/leftarm.png")
right_hand = pygame.transform.scale(right_hand, (800, 600))
left_hand = pygame.transform.scale(left_hand, (40, 500))
right_rect = right_hand.get_rect(center=center)
left_rect = left_hand.get_rect(center=center)

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break

    screen.fill((255, 255, 255))
    now = datetime.now()
    minutes = now.minute
    seconds = now.second
    min_angle = -(minutes * 6 + seconds * 0.1)
    sec_angle = -(seconds * 6)

    rotated_right_hand = rotate(right_hand, min_angle)
    rotated_left_hand = rotate(left_hand, sec_angle)

    rect_r = rotated_right_hand.get_rect(center=center)
    rect_l = rotated_left_hand.get_rect(center=center)

    screen.blit(background, (0, 0))
    screen.blit(rotated_right_hand, rect_r)
    screen.blit(rotated_left_hand, rect_l)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
