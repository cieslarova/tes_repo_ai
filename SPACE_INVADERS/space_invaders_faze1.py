import pygame # Importuje knihovnu Pygame pro tvorbu her.
import os # Importuje modul os pro práci s cestami k souborům.

# --- Herní konstanty ---
SCREEN_WIDTH = 800 # Šířka herního okna v pixelech.
SCREEN_HEIGHT = 600 # Výška herního okna v pixelech.
PLAYER_SPEED = 5 # Rychlost pohybu hráče.
ENEMY_SPEED = 1 # Rychlost pohybu nepřátel.
BULLET_SPEED = 7 # Rychlost pohybu střel.
PLAYER_LIVES = 3 # Počet životů hráče.

# --- Barvy ---
WHITE = (255, 255, 255) # Bílá barva.
BLACK = (0, 0, 0) # Černá barva.
GREEN = (0, 255, 0) # Zelená barva.
RED = (255, 0, 0) # Červená barva.
BLUE = (0, 0, 255) # Modrá barva.

# --- Cesty k obrázkům (pro budoucí použití, zatím jen placeholder) ---
# Získání absolutní cesty ke složce, kde se skript nachází.
current_dir = os.path.dirname(os.path.abspath(__file__))
# Cesta k obrázku hráče.
PLAYER_IMAGE_PATH = os.path.join(current_dir, "assets", "player.png")
# Cesta k obrázku nepřítele.
ENEMY_IMAGE_PATH = os.path.join(current_dir, "assets", "enemy.png")
# Cesta k obrázku střely.
BULLET_IMAGE_PATH = os.path.join(current_dir, "assets", "bullet.png")

# --- Třída pro hráče ---
class Player(pygame.sprite.Sprite):
    """
    Reprezentuje hráčovu loď ve hře.
    Dědí od pygame.sprite.Sprite pro snadnější správu kolizí a vykreslování.
    """
    def __init__(self):
        """
        Inicializuje hráče s jeho počáteční pozicí a vzhledem.
        """
        super().__init__() # Volá konstruktor rodičovské třídy Sprite.
        # Vytvoří povrch (surface) pro hráče, zatím obdélník.
        self.image = pygame.Surface([50, 40])
        self.image.fill(BLUE) # Vyplní obdélník modrou barvou.
        # Získá obdélníkovou oblast (rect) z obrázku hráče.
        self.rect = self.image.get_rect()
        # Nastaví počáteční pozici hráče dole uprostřed obrazovky.
        self.rect.centerx = SCREEN_WIDTH // 2
        self.rect.bottom = SCREEN_HEIGHT - 10

    def draw(self, screen):
        """
        Vykreslí hráče na danou obrazovku.
        :param screen: Objekt obrazovky Pygame, na kterou se má hráč vykreslit.
        """
        screen.blit(self.image, self.rect) # Vykreslí obrázek hráče na jeho pozici.

# --- Třída pro nepřítele (Invadera) ---
class Enemy(pygame.sprite.Sprite):
    """
    Reprezentuje nepřátelskou loď (invadera) ve hře.
    Dědí od pygame.sprite.Sprite.
    """
    def __init__(self, x, y):
        """
        Inicializuje nepřítele s danou pozicí.
        :param x: Počáteční x-ová souřadnice nepřítele.
        :param y: Počáteční y-ová souřadnice nepřítele.
        """
        super().__init__() # Volá konstruktor rodičovské třídy Sprite.
        # Vytvoří povrch pro nepřítele, zatím obdélník.
        self.image = pygame.Surface([40, 30])
        self.image.fill(GREEN) # Vyplní obdélník zelenou barvou.
        # Získá obdélníkovou oblast (rect) z obrázku nepřítele.
        self.rect = self.image.get_rect()
        # Nastaví počáteční pozici nepřítele.
        self.rect.x = x
        self.rect.y = y

    def draw(self, screen):
        """
        Vykreslí nepřítele na danou obrazovku.
        :param screen: Objekt obrazovky Pygame, na kterou se má nepřítel vykreslit.
        """
        screen.blit(self.image, self.rect) # Vykreslí obrázek nepřítele na jeho pozici.

# --- Třída pro střelu ---
class Bullet(pygame.sprite.Sprite):
    """
    Reprezentuje střelu vystřelenou hráčem nebo nepřítelem.
    Dědí od pygame.sprite.Sprite.
    """
    def __init__(self, x, y, direction):
        """
        Inicializuje střelu s danou pozicí a směrem.
        :param x: Počáteční x-ová souřadnice střely.
        :param y: Počáteční y-ová souřadnice střely.
        :param direction: Směr pohybu střely (např. -1 pro nahoru, 1 pro dolů).
        """
        super().__init__() # Volá konstruktor rodičovské třídy Sprite.
        # Vytvoří povrch pro střelu, obdélník.
        self.image = pygame.Surface([5, 10])
        self.image.fill(WHITE) # Vyplní obdélník bílou barvou.
        # Získá obdélníkovou oblast (rect) ze střely.
        self.rect = self.image.get_rect()
        # Nastaví počáteční pozici střely.
        self.rect.centerx = x
        self.rect.bottom = y
        self.direction = direction # Uloží směr pohybu střely.

    def draw(self, screen):
        """
        Vykreslí střelu na danou obrazovku.
        :param screen: Objekt obrazovky Pygame, na kterou se má střela vykreslit.
        """
        screen.blit(self.image, self.rect) # Vykreslí obrázek střely na její pozici.

# --- Hlavní herní funkce ---
def main():
    """
    Hlavní funkce, která inicializuje hru a spouští herní smyčku.
    """
    pygame.init() # Inicializuje všechny moduly Pygame.

    # Nastavení herního okna.
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # Vytvoří herní okno.
    pygame.display.set_caption("Space Invaders") # Nastaví titulek okna.

    # Vytvoření instancí herních entit.
    player = Player() # Vytvoří instanci hráče.
    # Vytvoří několik instancí nepřátel pro ukázku.
    enemies = [Enemy(50 + i * 60, 50 + j * 40) for i in range(10) for j in range(3)]
    bullets = [] # Seznam pro ukládání aktivních střel.

    running = True # Proměnná pro řízení herní smyčky.
    while running:
        # --- Zpracování událostí ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # Pokud uživatel zavře okno.
                running = False # Ukončí herní smyčku.

        # --- Aktualizace herního stavu (zatím prázdné) ---
        # V této fázi se nic neaktualizuje, pouze se vykresluje.

        # --- Vykreslování ---
        screen.fill(BLACK) # Vyplní celou obrazovku černou barvou (pozadí).

        player.draw(screen) # Vykreslí hráče.
        for enemy in enemies: # Projde všechny nepřátele.
            enemy.draw(screen) # Vykreslí každého nepřítele.
        for bullet in bullets: # Projde všechny střely.
            bullet.draw(screen) # Vykreslí každou střelu.

        pygame.display.flip() # Aktualizuje celý obsah obrazovky.

    pygame.quit() # Odinicializuje Pygame moduly.

if __name__ == "__main__":
    main() # Spustí hlavní herní funkci, pokud je skript spuštěn přímo.
