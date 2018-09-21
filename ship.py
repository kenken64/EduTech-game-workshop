from pygame import *

class Ship(sprite.Sprite):
    def __init__(self, shipImage):
        sprite.Sprite.__init__(self)
        self.image = shipImage
        self.rect = self.image.get_rect(topleft=(375, 540))
        self.speed = 5

    def update(self, keys, game, *args):
        if keys[K_LEFT] and self.rect.x > 10:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < 740:
            self.rect.x += self.speed
        game.blit(self.image, self.rect)