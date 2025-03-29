import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Класс, представляющий одного пришельца."""

    def __init__(self, ai_game):
        """Инициализирует пришельца и задает его начальную позицию."""
        super().__init__()
        self.screen = ai_game.screen

        # Загрузка изображения пришельца и назначение атрибута rect
        original_image = pygame.image.load('/mnt/test disk/Python/Game/images/alien.png')
        self.image = pygame.transform.scale(original_image, (60, 50))

        self.rect = self.image.get_rect()

        # Каждый новый пришелец появляется в левом верхнем углу экрана.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # Сохранение точной горизонтальной позиции пришельца.
        self.x = float(self.rect.x)
        