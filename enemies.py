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
    pygame.image.load('graphics/beetle1.png'),
    pygame.image.load('graphics/beetle2.png')
]


class Fly(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.frames = FLY_FRAMES
        self.frame_index = 0
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect(midbottom=(random.randint(900, 1100), 210))

    def update(self):
        self.frame_index += 0.1
        if self.frame_index >= len(self.frames):
            self.frame_index = 0

        self.image = self.frames[int(self.frame_index)]

        self.rect.x -= 7
        if self.rect.right < 0:
            self.kill()


class Snail(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.frames = SNAIL_FRAMES
        self.frame_index = 0
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect(midbottom=(random.randint(900, 1100), 300))

    def update(self):
        self.frame_index += 0.1
        if self.frame_index >= len(self.frames):
            self.frame_index = 0

        self.image = self.frames[int(self.frame_index)]

        self.rect.x -= 5
        if self.rect.right < 0:
            self.kill()

class Beetle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.frames = BEETLE_FRAMES
        self.frame_index = 0
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect(midbottom=(random.randint(900, 1100), 210))

    def update(self):
        self.frame_index += 0.1
        if self.frame_index >= len(self.frames):
            self.frame_index = 0

        self.image = self.frames[int(self.frame_index)]

        self.rect.x -= 7
        if self.rect.right < 0:
            self.kill()