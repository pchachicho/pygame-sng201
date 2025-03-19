import random
from operator import truediv
import pygame
import sys
import time
import splash
from enemies import Fly, Snail
from player import Player
pygame.init()

WIDTH = 800
HEIGHT = 400
GROUND = int(HEIGHT * .75)



def display_score(screen, score: int, font: pygame.font.Font):
    score_surface = font.render(f'Score: {score}', False, (64, 64, 64))
    score_rect = score_surface.get_rect(center=(WIDTH // 2, 50))
    screen.blit(score_surface, score_rect)

def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('PixelRunner')
    clock = pygame.time.Clock()
    test_font = pygame.font.Font('font/Pixeltype.ttf', 50)
    game_active = False

    # test_surface = pygame.Surface((100, 200))
    # test_surface.fill('blue')
    test_surface = pygame.image.load('graphics/Sky.png').convert()
    ground_surface = pygame.image.load('graphics/ground.png').convert()

    start_time = 0
    score = 0

    splash_screen = splash.SplashScreen(test_font, WIDTH, HEIGHT)

    # Set up the sprites here
    player = pygame.sprite.GroupSingle()
    player.add(Player(GROUND))
    enemies = pygame.sprite.Group()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not game_active:
                    game_active = True
                    start_time = pygame.time.get_ticks()
        if game_active:
            # draw all our elements
            # update what's on the screen
            screen.blit(test_surface, (0, 0))
            screen.blit(ground_surface, (0, 300))

            score = (pygame.time.get_ticks() - start_time) // 1000
            display_score(screen, score, test_font)

            #Draw a random enemy
            x = random.randint(1,300)
            if x == 1:
                enemies.add(Fly())
            elif x == 2:
                enemies.add(Snail())
            enemies.update()
            enemies.draw(screen)

            # Draw the Player
            player.update()
            player.draw(screen)

            if pygame.sprite.spritecollideany(player.sprite, enemies):
                game_active = False
                enemies.empty()

        else:
            # screen.fill('yellow')
            splash_screen.draw(screen, score)
        pygame.display.update()
        clock.tick(60)

if __name__ == '__main__':
    main()