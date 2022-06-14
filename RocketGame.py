# импортируем движок pygame
import pygame
# импортируем библиотеку sys
import sys
# импортируем класс Settings
from Settings import Settings
# импортируем класс Rocket
from Rocket import Rocket


# Создаем класс RocketGame
class RocketGame:
    # Метод init
    def __init__(self):
        # Инициализация игры и движка pygame
        pygame.init()
        # Создай объект Settings и сохрани ее в переменную класса
        self.settings = Settings()
        # Установи полноэкранный режим дисплея
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # Измени объект настроек (его высоту) на основе текущего разрешения экрана
        self.settings.scrinWidth = self.screen.get_rect().width
        # Измени объект настроек (его ширину) на основе текущего разрешения экрана
        self.settings.scrinHeight = self.screen.get_rect().height
        pygame.display.set_caption("Rocket Game")
        # Создай объект Rocket и сохрани его в переменную класса
        self.ship = Rocket(self.screen, self.settings)

    # Метод проверки нажатия клавиши
    def CheckDown(self, event):
        # Реализуй проверку клавиш w,a,s,d (или стрелки) (как в прошлой игре, только теперь корабль двигается еще и вверх, и в низ)
        if event.key == pygame.K_RIGHT:
            self.ship.isRight = True
        elif event.key == pygame.K_LEFT:
            self.ship.isLeft = True
        elif event.key == pygame.K_UP:
            self.ship.isUp = True
        elif event.key == pygame.K_DOWN:
            self.ship.isDown = True
        elif event.key == pygame.K_ESCAPE:
            sys.exit()

    def CheckUp(self,event):
        # Метод проверки отпускания клавиши
        if event.key == pygame.K_RIGHT:
            self.ship.isRight = False
        elif event.key == pygame.K_LEFT:
            self.ship.isLeft = False
        elif event.key == pygame.K_UP:
            self.ship.isUp = False
        elif event.key == pygame.K_DOWN:
            self.ship.isDown = False


    def CheckEvent(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.CheckDown(event)
            elif event.type == pygame.KEYUP:
                self.CheckUp(event)

    def UpdateScreen(self):
        self.screen.fill(self.settings.colour)

        self.ship.blitme()

        pygame.display.flip()

    def start(self):
        while True:
            self.CheckEvent()
            self.ship.Update()
            self.UpdateScreen()

if __name__ == '__main__':
    game = RocketGame()
    game.start()
