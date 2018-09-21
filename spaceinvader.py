import platform
platform.architecture()
from pygame import *
import sys
from random import shuffle, randrange, choice
from text import Text
from ship import Ship


#        R     G    B
WHITE = (255, 255, 255)
GREEN = (78, 255, 87)
YELLOW = (241, 255, 0)
BLUE = (80, 255, 239)
PURPLE = (203, 0, 255)
RED = (237, 28, 36)


SCREEN 	= display.set_mode((800,600))
FONT = "fonts/space_invaders.ttf"
IMG_NAMES = ["ship", "mystery", "enemy1_1","enemy1_2", "enemy2_1", "enemy2_2", 
   "enemy3_1", "enemy3_2", "explosionblue", "explosiongreen", "explosionpurple", "laser", "enemylaser"]

IMAGES  = {name: image.load("images/{}.png".format(name)).convert_alpha() for name in IMG_NAMES}


class SpaceInvaders(object):
    def __init__(self):
        mixer.pre_init(44100, -16, 1,512)
        init()
        self.caption = display.set_caption("Space Invader")
        self.background = image.load('images/background.jpg').convert()
        print(self.background)
        self.screen = SCREEN
        self.mainScreen = True
        self.startGame = False
        self.gameOver = False

    ## check for keyboard input 
    def check_input(self):
        self.keys = key.get_pressed()
        for e in event.get():
          if e.type == QUIT:
            sys.exit()

    ## create game menu
    def create_main_menu(self):
        # TODO create a custom splash screen
        self.enemy1 = IMAGES["enemy3_1"]
        self.enemy1 = transform.scale(self.enemy1, (40, 40))
        self.enemy2 = IMAGES["enemy2_2"]
        self.enemy2 = transform.scale(self.enemy2 , (40, 40))
        self.enemy3 = IMAGES["enemy1_2"]
        self.enemy3 = transform.scale(self.enemy3 , (40, 40))
        self.enemy4 = IMAGES["mystery"]
        self.enemy4 = transform.scale(self.enemy4 , (80, 40))
        
        self.screen.blit(self.enemy1, (318, 270))
        self.screen.blit(self.enemy2, (318, 320))
        self.screen.blit(self.enemy3, (318, 370))
        self.screen.blit(self.enemy4, (299, 420))
        
        for e in event.get():
          if e.type == QUIT:
                sys.exit()
          if e.type == KEYUP:
                print("key up")
                self.startGame = True
                self.mainScreen = False

    def create_text(self):
        # font , scale , value, colour , x , y
        print("create text")
        self.titleText = Text(FONT, 50, "Space Invaders", WHITE, 164, 155)
        self.titleText2 = Text(FONT, 25, "Press any key to continue", WHITE, 201, 225)
        self.gameOver = Text(FONT, 50, "Game Over", WHITE, 250, 270)
        self.nextRoundText = Text(FONT, 50, "Next Round", WHITE, 240, 270)
        self.enemy1Text = Text(FONT, 25, "   =   5 pts", GREEN, 368, 270)
        self.enemy2Text = Text(FONT, 25, "   =  10 pts", BLUE, 368, 320)
        self.enemy3Text = Text(FONT, 25, "   =  15 pts", PURPLE, 368, 370)
        self.enemy4Text = Text(FONT, 25, "   =  ?????", RED, 368, 420)
        self.scoreText = Text(FONT, 20, "Score", WHITE, 5, 5)
        self.livesText = Text(FONT, 20, "Lives ", WHITE, 640, 5)
        

    def reset(self, score, lives, newGame=False):
        self.player = Ship(IMAGES["ship"])
        self.clock = time.Clock()
        self.shipTimer = time.get_ticks()
        self.create_text()
        
    def main(self):
        while True:
            if self.mainScreen:
                self.reset(0,3,True)
                self.screen.blit(self.background, (0,0))
                self.titleText.draw(self.screen)
                self.titleText2.draw(self.screen)
                self.enemy1Text.draw(self.screen)
                self.enemy2Text.draw(self.screen)
                self.enemy3Text.draw(self.screen)
                self.enemy4Text.draw(self.screen)
                self.create_main_menu()
            elif self.startGame:
                print("start game ...")
                # get current time
                currentTime = time.get_ticks()
                self.screen.blit(self.background, (0,0))
                self.check_input()
                self.player.update(self.keys, self.screen)

            elif self.gameOver :
                print("game over ...")

            display.update()
            self.clock.tick(60)