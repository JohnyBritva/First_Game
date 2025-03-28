import sys
import pygame
# Убедитесь, что файлы settings.py и ship.py находятся в той же директории
# или что Python может их найти (например, через PYTHONPATH)
from settings import Settings
from ship import Ship
from bullet import Bullet

class AlienInvasion:
    """Класс для управления ресурсами и поведением игры."""
    def __init__(self):
        """Инициализирует игру и создает игровые ресурсы."""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self) # Передаем экземпляр AlienInvasion в Ship
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        """Запуск основного цикла игры."""
        while True:
            self._check_events()
            self.ship.update() # Обновляем состояние корабля
            self.bullets.update()
            self._update_bullets()
            self._update_screen() # Обновляем экран после всех изменений
            # Удаление снарядов, вышедших за край экрана.
            print(len(self.bullets))
            

    def _check_events(self):
        """Обрабатывает нажатия клавиш и события мыши."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                # Вызываем метод класса _check_keydown_events
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                # Вызываем метод класса _check_keyup_events
                self._check_keyup_events(event)

    # --- ИСПРАВЛЕНИЕ: Уменьшен отступ для следующих двух методов ---
    def _check_keydown_events(self, event):
        """Реагирует на нажатие клавиш."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q: # Нажатие Q для выхода
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Реагирует на отпускание клавиш."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
    
    def _fire_bullet(self):
        """Создание нового снаряда и включение его в группу bullets."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
    
    def _update_bullets(self):
        """Обновляет позиции снарядов и уничтожает старые снаряды."""
        # Обновление позиций снарядов.    
        self.bullets.update()
        # Удаление снарядов, вышедших за край экрана.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                 self.bullets.remove(bullet)

    def _update_screen(self):
        """Обновляет изображения на экране и отображает новый экран."""
        # При каждом проходе цикла — закрашивать экран
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme() # Рисуем корабль на экране
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        # Отображение последнего прорисованного экрана.
        pygame.display.flip()

if __name__ == '__main__':
    # Создание экземпляра и запуск игры.
    ai = AlienInvasion()
    ai.run_game()