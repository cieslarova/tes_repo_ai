import pygame # Importuje knihovnu Pygame pro tvorbu her.
import os # Importuje modul os pro práci s cestami k souborům.
import time # Importuje modul time pro práci s časem, použitý pro omezení střelby.

# --- Herní konstanty ---
SCREEN_WIDTH = 800 # Šířka herního okna v pixelech.
SCREEN_HEIGHT = 600 # Výška herního okna v pixelech.
PLAYER_SPEED = 5 # Rychlost pohybu hráče.
ENEMY_SPEED = 1 # Rychlost pohybu nepřátel.
BULLET_SPEED = 7 # Rychlost pohybu střel.
PLAYER_LIVES = 3 # Počet životů hráče.
PLAYER_SHOT_COOLDOWN = 0.5 # Prodleva mezi střelami hráče v sekundách.
ENEMY_DROP_DISTANCE = 20 # Vzdálenost, o kterou nepřátelé klesnou po dosažení okraje.

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
        self.speed_x = 0 # Počáteční rychlost pohybu hráče ve směru X.
        self.last_shot_time = 0 # Čas posledního výstřelu pro cooldown.

    def update(self):
        """
        Aktualizuje pozici hráče na základě jeho rychlosti.
        Zajišťuje, že hráč zůstane v rámci obrazovky.
        """
        self.rect.x += self.speed_x # Pohne hráčem o hodnotu speed_x.
        # Omezení pohybu hráče na levý okraj obrazovky.
        if self.rect.left < 0:
            self.rect.left = 0
        # Omezení pohybu hráče na pravý okraj obrazovky.
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH

    def shoot(self):
        """
        Vytvoří novou střelu, pokud uplynul dostatečný čas od posledního výstřelu.
        :return: Nová instance Bullet, nebo None, pokud je cooldown aktivní.
        """
        current_time = time.time() # Získá aktuální čas.
        # Kontroluje, zda uplynul dostatečný čas od posledního výstřelu.
        if current_time - self.last_shot_time > PLAYER_SHOT_COOLDOWN:
            self.last_shot_time = current_time # Aktualizuje čas posledního výstřelu.
            # Vytvoří novou střelu uprostřed hráče, směr nahoru (-1).
            return Bullet(self.rect.centerx, self.rect.top, -1)
        return None

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

    def update(self, direction):
        """
        Aktualizuje pozici nepřítele.
        :param direction: Směr pohybu nepřátel (1 pro doprava, -1 pro doleva).
        """
        self.rect.x += ENEMY_SPEED * direction # Pohne nepřítelem ve směru X.

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
        self.rect.bottom = y if direction == -1 else y + 10 # Upraví pozici pro nepřátelské střely.
        self.direction = direction # Uloží směr pohybu střely.

    def update(self):
        """
        Aktualizuje pozici střely.
        """
        self.rect.y += self.direction * BULLET_SPEED # Pohne střelou ve směru Y.

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

    # Hodiny pro řízení snímkové frekvence.
    clock = pygame.time.Clock()

    # Vytvoření instancí herních entit.
    player = Player() # Vytvoří instanci hráče.
    # Vytvoří skupinu nepřátel.
    enemies = pygame.sprite.Group() # Používá pygame.sprite.Group pro efektivnější správu.
    for row in range(3):
        for col in range(10):
            enemy = Enemy(50 + col * 60, 50 + row * 40)
            enemies.add(enemy) # Přidá nepřítele do skupiny.

    player_bullets = pygame.sprite.Group() # Skupina pro střely hráče.
    enemy_bullets = pygame.sprite.Group() # Skupina pro střely nepřátel (zatím nepoužito).

    enemy_direction = 1 # Počáteční směr pohybu nepřátel (1 = doprava, -1 = doleva).

    running = True # Proměnná pro řízení herní smyčky.
    while running:
        # --- Zpracování událostí ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # Pokud uživatel zavře okno.
                running = False # Ukončí herní smyčku.
            elif event.type == pygame.KEYDOWN: # Pokud je stisknuta klávesa.
                if event.key == pygame.K_LEFT: # Šipka doleva.
                    player.speed_x = -PLAYER_SPEED # Nastaví rychlost hráče doleva.
                elif event.key == pygame.K_RIGHT: # Šipka doprava.
                    player.speed_x = PLAYER_SPEED # Nastaví rychlost hráče doprava.
                elif event.key == pygame.K_SPACE: # Mezerník.
                    new_bullet = player.shoot() # Pokusí se vystřelit.
                    if new_bullet: # Pokud byla střela vytvořena (není cooldown).
                        player_bullets.add(new_bullet) # Přidá střelu do skupiny.
            elif event.type == pygame.KEYUP: # Pokud je klávesa uvolněna.
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    player.speed_x = 0 # Zastaví pohyb hráče.

        # --- Aktualizace herního stavu ---
        player.update() # Aktualizuje pozici hráče.

        # Aktualizace nepřátel a změna směru.
        move_down = False # Příznak, zda se mají nepřátelé posunout dolů.
        for enemy in enemies:
            enemy.update(enemy_direction) # Aktualizuje pozici nepřítele.
            # Kontrola, zda nepřítel dosáhl okraje obrazovky.
            if enemy.rect.right >= SCREEN_WIDTH or enemy.rect.left <= 0:
                move_down = True # Nastaví příznak pro posun dolů.

        if move_down: # Pokud se mají nepřátelé posunout dolů.
            enemy_direction *= -1 # Obrátí směr pohybu nepřátel.
            for enemy in enemies:
                enemy.rect.y += ENEMY_DROP_DISTANCE # Posune nepřítele dolů.

        # Aktualizace střel hráče.
        player_bullets.update()
        # Odstranění střel, které opustily obrazovku.
        for bullet in player_bullets:
            if bullet.rect.bottom < 0:
                player_bullets.remove(bullet)

        # --- Vykreslování ---
        screen.fill(BLACK) # Vyplní celou obrazovku černou barvou (pozadí).

        player.draw(screen) # Vykreslí hráče.
        for enemy in enemies: # Projde všechny nepřátele.
            enemy.draw(screen) # Vykreslí každého nepřítele.
        for bullet in player_bullets: # Projde všechny střely hráče.
            bullet.draw(screen) # Vykreslí každou střelu.
        for bullet in enemy_bullets: # Projde všechny střely nepřátel (zatím prázdné).
            bullet.draw(screen)

        pygame.display.flip() # Aktualizuje celý obsah obrazovky.

        # Omezení snímkové frekvence.
        clock.tick(60) # Hra poběží maximálně na 60 snímků za sekundu.

    pygame.quit() # Odinicializuje Pygame moduly.

if __name__ == "__main__":
    main() # Spustí hlavní herní funkci, pokud je skript spuštěn přímo.
