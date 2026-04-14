import pygame

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((100, 100))
        pygame.draw.circle(self.image, "red", (50, 50), 50)

        self.rect = self.image.get_rect(center=(400, 300))

    def move(self):
        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[pygame.K_UP]:
            self.rect.move_ip(0, -20)
        if pressed_keys[pygame.K_DOWN]:
            self.rect.move_ip(0, 20)
        if pressed_keys[pygame.K_LEFT]:
            self.rect.move_ip(-20, 0)
        if pressed_keys[pygame.K_RIGHT]:
            self.rect.move_ip(20, 0)

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > 800:
            self.rect.right = 800
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > 600:
            self.rect.bottom = 600