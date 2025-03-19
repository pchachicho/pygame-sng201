
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.jump = pygame.image.load('graphics/Player/jump.png').convert_alpha()
        self.frames = [
            pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha(),
            pygame.image.load('graphics/Player/player_walk_2.png').convert_alpha(),
        ]
        self.walk_index = 0
        self.image = self.frames[self.walk_index]
        self.rect = self.image.get_rect(midbottom=(80, 300))
        self.gravity = 0

    def update(self):
        #First, handle input
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= GROUND:
            player_gravity = -20
        #Second, manipulate gravity
        #Third, do our animation changes
        self.gravity += 1
        self.rect.y += player_gravity
        if self.rect.bottom >= GROUND:
            self.rect.bottom = GROUND
        pass

        # Player animation
        if self.rect.bottom < GROUND:
            self.image = self.jump
        else:
            self.walk_index += 0.1
            if self.walk_index >= len(self.frames):
                self.walk_index = 0
            self.image = self.frames[int(self.walk_index)]

