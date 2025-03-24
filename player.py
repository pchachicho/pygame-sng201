import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, ground):
        super().__init__()
        self.GROUND = ground

        self.jump = pygame.image.load('graphics/Player/jump.png').convert_alpha()
        self.frames = [
            pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha(),
            pygame.image.load('graphics/Player/player_walk_2.png').convert_alpha(),
        ]
        self.walk_index = 0
        self.image = self.frames[self.walk_index]
        self.rect = self.image.get_rect(midbottom=(80, self.GROUND))
        self.gravity = 0
        self.jump_sound = pygame.mixer.Sound('audio/jump.mp3')

    def update(self):
        # first, let's handle input
        keys = pygame.key.get_pressed()
        # {
        #   K_SPACE: True,
        #   K_TAB: False,
        # }
        if keys[pygame.K_SPACE] and self.rect.bottom >= self.GROUND:
            self.gravity = -20
            self.jump_sound.play()
        # second, let's manipulate gravity
        # third, do our animation changes
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= self.GROUND:
            self.rect.bottom = self.GROUND

        # Player animation
        if self.rect.bottom < self.GROUND:
            self.image = self.jump
        else:
            self.walk_index += 0.1
            if self.walk_index >= len(self.frames):
                self.walk_index = 0
            self.image = self.frames[int(self.walk_index)]
