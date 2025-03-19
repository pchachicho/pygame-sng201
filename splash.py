"""Provides the SplashScreen class for drawing the game's intro screen."""
import pygame

TEXT_COLOR = (111, 196, 169)
BACKGROUND_COLOR = (94, 129, 162)


class SplashScreen:
    """This class configures the layout and draws the splash screen to a specified surface."""

    def __init__(self, font: pygame.font.Font, screen_width: int, screen_height: int):
        """
        Initializes the layout of the screen. The layout is relative to the screen dimensions passed.
        Must call the draw() method to actually display.
        :param font: the font for the text on the screen.
        :param screen_width: integer width of the screen
        :param screen_height: integer height of the screen
        """
        self.font = font
        self.CENTER_X = screen_width // 2
        center_y = screen_height // 2

        # Get the player image and scale to 1/2 the screen height. Positing in the center of the screen.
        player = pygame.image.load('graphics/player/player_stand.png').convert_alpha()
        self.player_stand = pygame.transform.rotozoom(player, 0, (screen_height // 2) / player.get_height())
        player_height = self.player_stand.get_height()
        self.player_stand_rect = self.player_stand.get_rect(center=(self.CENTER_X, center_y))

        # Title of the game above the player image.
        self.game_name = font.render('Pixel Runner', False, TEXT_COLOR)
        self.game_name_rect = self.game_name.get_rect(
            center=(self.CENTER_X, center_y - player_height // 2 - font.get_height()))

        # Message showing "Press space to run" or the most recent score positioned just below the player image.
        self.MESSAGE_BASELINE = center_y + player_height // 2 + font.get_height()
        self.game_message = font.render('Press space to run', False, TEXT_COLOR)
        self.game_message_rect = self.game_message.get_rect(center=(self.CENTER_X, self.MESSAGE_BASELINE))

    def draw(self, screen: pygame.surface.Surface, score: int = 0):
        """
        Draws the splash screen to the screen.
        :param screen: the surface on which to render the screen.
        :param score: the score to display. a score !=0 will display the score in text, else the instructions are shown.
        """
        screen.fill(BACKGROUND_COLOR)
        screen.blit(self.game_name, self.game_name_rect)
        screen.blit(self.player_stand, self.player_stand_rect)

        if score == 0:
            screen.blit(self.game_message, self.game_message_rect)
        else:
            score_message = self.font.render(f'Your score: {score}', False, TEXT_COLOR)
            score_message_rect = score_message.get_rect(center=(self.CENTER_X, self.MESSAGE_BASELINE))
            screen.blit(score_message, score_message_rect)
