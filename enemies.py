import random

import pygame

FLY_FRAMES = [
    pygame.image.load('graphics/Fly/Fly1.png'),
    pygame.image.load('graphics/Fly/Fly2.png')
]

SNAIL_FRAMES = [
    pygame.image.load('graphics/snail/snail1.png'),
    pygame.image.load('graphics/snail/snail2.png')
]
BEETLE_FRAMES = [
    pygame.image.load('graphics/Beetle/beetle1.png'),
    pygame.image.load('graphics/Beetle/beetle2.png')
]

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, kind: str):
        super().__init__()
        self.kind = kind

        if kind == 'fly':
            self.frames = FLY_FRAMES
            y = 210
        elif kind == 'snail':
            self.frames = SNAIL_FRAMES
            y = 300
        else:
            self.frames = BEETLE_FRAMES
            y = 300

        self.frame_index = 0
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect(midbottom=(random.randint(900, 1100), y))

    def update(self):
        self.frame_index += 0.1
        if self.frame_index >= len(self.frames):
            self.frame_index = 0

        self.image = self.frames[int(self.frame_index)]

        self.rect.x -= 8 if self.kind == 'fly' else 5
        if self.rect.right < 0:
            self.kill()