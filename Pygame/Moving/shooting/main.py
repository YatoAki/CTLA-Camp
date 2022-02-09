import pygame, sys
from shooter import Shooter
from bullet import Bullet

class Game:

    def __init__(self,width,height):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width,height))
        self.clock = pygame.time.Clock()
        self.bullets = []
        self.shooter = Shooter(self,width/2,height - 30)
        pygame.display.set_caption('Shooting Game')

    def run(self):

        while True:
            self.screen.fill((255,255,255))

            pressed = pygame.key.get_pressed()

            if pressed[pygame.K_LEFT]:
                self.shooter.x -= 10 if self.shooter.x > 0 else 0
            elif pressed[pygame.K_RIGHT]:
                self.shooter.x += 10 if self.shooter.x < self.width - 20 else 0

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    self.bullets.append(Bullet(self,self.shooter.x,self.shooter.y))

            for bullet in self.bullets:
                bullet.draw()

            self.shooter.draw()
            pygame.display.update()
            self.clock.tick(60)


if __name__ == '__main__':
    game = Game(600,400)
    game.run()
