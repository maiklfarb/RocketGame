# класс Rocket такой-же как и в прошлой
# обрати внимание: подгрузка изображения (нужно указать правильное название файла), должны быть флаги на движение вверх и вниз
import pygame
class Rocket:
    def __init__(self, screen, settings):
        self.screen = screen
        self.scrinRect = screen.get_rect()
        self.settings = settings
        self.image = pygame.image.load("Images/ROCKET.png")
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.scrinRect.midbottom

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.isRight = False
        self.isLeft = False
        self.isUp = False
        self.isDown = False
    def Update(self):
        if self.isLeft and self.rect.left > 0:
            self.x -= self.settings.speed
        if self.isRight and self.rect.right < self.scrinRect.right:
            self.x += self.settings.speed
        if self.isDown and self.rect.bottom < self.scrinRect.bottom:
            self.y += self.settings.speed
        if self.isUp and self.rect.top > self.scrinRect.top:
            self.y -= self.settings.speed
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        self.screen.blit(self.image, self.rect)