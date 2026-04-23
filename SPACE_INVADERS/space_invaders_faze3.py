import pygame # Importuje knihovnu Pygame pro tvorbu her.
import os # Importuje modul os pro práci s cestami k souborům.
import time # Importuje modul time pro práci s časem, použitý pro omezení střelby.
import random # Importuje modul random pro generování náhodných čísel (pro střelbu nepřátel).

# --- Herní konstanty ---
SCREEN_WIDTH = 800 # Šířka herního okna v pixelech.
SCREEN_HEIGHT = 600 # Výška herního okna v pixelech.
PLAYER_SPEED = 5 # Rychlost pohybu hráče.
ENEMY_SPEED = 1 # Rychlost pohybu nepřátel.
BULLET_SPEED = 7 # Rychlost pohybu střel.
PLAYER_LIVES_START = 3 # Počáteční počet životů hráče.
PLAYER_SHOT_COOLDOWN = 0.5 # Prodleva mezi střelami hráče v sekundách.
ENEMY_DROP_DISTANCE = 20 # Vzdálenost, o kterou nepřátelé klesnou po dosažení okraje.
ENEMY_SHOT_CHANCE = 0.005 # Šance, že nepřítel vystřelí v každém snímku.
SCORE_PER_ENEMY = 10 # Body získané za zničení jednoho nepřítele.

# --- Barvy ---
WHITE = (255, 255, 255) # Bílá barva.
BLACK = (0, 0, 0) # Černá barva.
GREEN = (0, 255, 0) # Zelená barva.
RED = (255, 0, 0) # Červená barva.
BLUE = (0, 0, 255) # Modrá barva.
YELLOW = (255, 255, 0) # Žlutá barva pro text.

# --- Herní stavy ---
GAME_RUNNING = 0 # Hra běží.
GAME_OVER = 1 # Hra skončila (prohra).
GAME_WIN = 2 # Hra skončila (výhra).

# --- Cesty k obrázkům (pro budoucí použití, zatím jen placeholder) ---
current_dir = os.path.dirname(os.path.abspath(__file__))
# Vytvoření složky 'assets', pokud neexistuje.
assets_dir = os.path.join(current_dir, "assets")
if not os.path.exists(assets_dir):
    os.makedirs(assets_dir)

# Funkce pro načítání obrázků s fallbackem na placeholder.
def load_image_or_placeholder(path, size, color):
    """
    Načte obrázek z dané cesty. Pokud obrázek neexistuje, vytvoří placeholder.
    :param path: Cesta k obrázku.
    :param size: Velikost placeholderu (šířka, výška).
    :param color: Barva placeholderu.
    :return: Načtený obrázek nebo placeholder Surface.
    """
    try:
        image = pygame.image.load(path).convert_alpha() # Načte obrázek s průhledností.
        image = pygame.transform.scale(image, size) # Změní velikost obrázku.
        return image
    except pygame.error:
        print(f"Varování: Obrázek '{path}' nenalezen. Používám placeholder.")
        placeholder = pygame.Surface(size) # Vytvoří placeholder.
        placeholder.fill(color) # Vyplní placeholder barvou.
        return placeholder

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
        # Načte obrázek hráče nebo použije placeholder.
        self.image = load_image_or_placeholder(PLAYER_IMAGE_PATH, (50, 40), BLUE)
        # Získá obdélníkovou oblast (rect) z obrázku hráče.
        self.rect = self.image.get_rect()
        # Nastaví počáteční pozici hráče dole uprostřed obrazovky.
        self.rect.centerx = SCREEN_WIDTH // 2
        self.rect.bottom = SCREEN_HEIGHT - 10
        self.speed_x = 0 # Počáteční rychlost pohybu hráče ve směru X.
        self.last_shot_time = 0 # Čas posledního výstřelu pro cooldown.
        self.lives = PLAYER_LIVES_START # Počet životů hráče.

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
            return Bullet(self.rect.centerx, self.rect.top, -1, "player")
        return None

    def take_hit(self):
        """
        Sníží počet životů hráče o 1.
        :return: True, pokud hráč má ještě životy, False, pokud je hra u konce.
        """
        self.lives -= 1
        return self.lives > 0

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
        # Načte obrázek nepřítele nebo použije placeholder.
        self.image = load_image_or_placeholder(ENEMY_IMAGE_PATH, (40, 30), GREEN)
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

    def shoot(self):
        """
        Vytvoří novou střelu z pozice nepřítele.
        :return: Nová instance Bullet.
        """
        # Vytvoří novou střelu uprostřed nepřítele, směr dolů (1).
        return Bullet(self.rect.centerx, self.rect.bottom, 1, "enemy")

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
    def __init__(self, x, y, direction, owner_type):
        """
        Inicializuje střelu s danou pozicí, směrem a typem vlastníka.
        :param x: Počáteční x-ová souřadnice střely.
        :param y: Počáteční y-ová souřadnice střely.
        :param direction: Směr pohybu střely (např. -1 pro nahoru, 1 pro dolů).
        :param owner_type: Typ vlastníka střely ("player" nebo "enemy").
        """
        super().__init__() # Volá konstruktor rodičovské třídy Sprite.
        # Vytvoří povrch pro střelu, obdélník.
        self.image = pygame.Surface([5, 10])
        self.image.fill(WHITE if owner_type == "player" else RED) # Bílá pro hráče, červená pro nepřátele.
        # Získá obdélníkovou oblast (rect) ze střely.
        self.rect = self.image.get_rect()
        # Nastaví počáteční pozici střely.
        self.rect.centerx = x
        self.rect.y = y
        self.direction = direction # Uloží směr pohybu střely.
        self.owner_type = owner_type # Uloží typ vlastníka.

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

# --- Funkce pro zobrazení textu ---
def draw_text(screen, text, size, color, x, y):
    """
    Vykreslí text na obrazovku.
    :param screen: Objekt obrazovky Pygame.
    :param text: Text k zobrazení.
    :param size: Velikost písma.
    :param color: Barva textu.
    :param x: X-ová souřadnice středu textu.
    :param y: Y-ová souřadnice středu textu.
    """
    font = pygame.font.Font(None, size) # Vytvoří objekt písma.
    text_surface = font.render(text, True, color) # Vytvoří povrch s textem.
    text_rect = text_surface.get_rect() # Získá obdélníkovou oblast textu.
    text_rect.center = (x, y) # Nastaví střed textu.
    screen.blit(text_surface, text_rect) # Vykreslí text na obrazovku.

# --- Hlavní herní funkce ---
def main():
    """
    Hlavní funkce, která inicializuje hru a spouští herní smyčku.
    """
    # Pokus o inicializaci Pygame.
    try:
        pygame.init() # Inicializuje všechny moduly Pygame.
    except pygame.error as e:
        print(f"Chyba při inicializaci Pygame: {e}")
        return # Ukončí program, pokud se Pygame nepodaří inicializovat.

    # Nastavení herního okna.
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # Vytvoří herní okno.
    pygame.display.set_caption("Space Invaders") # Nastaví titulek okna.

    # Hodiny pro řízení snímkové frekvence.
    clock = pygame.time.Clock()

    # --- Inicializace herních proměnných ---
    player = Player() # Vytvoří instanci hráče.
    enemies = pygame.sprite.Group() # Skupina pro nepřátele.
    player_bullets = pygame.sprite.Group() # Skupina pro střely hráče.
    enemy_bullets = pygame.sprite.Group() # Skupina pro střely nepřátel.
    enemy_direction = 1 # Počáteční směr pohybu nepřátel (1 = doprava, -1 = doleva).
    score = 0 # Počáteční skóre hráče.
    game_state = GAME_RUNNING # Počáteční stav hry.

    # Funkce pro resetování hry.
    def reset_game():
        nonlocal player, enemies, player_bullets, enemy_bullets, enemy_direction, score, game_state
        player = Player() # Vytvoří novou instanci hráče.
        enemies.empty() # Vyprázdní skupinu nepřátel.
        player_bullets.empty() # Vyprázdní skupinu střel hráče.
        enemy_bullets.empty() # Vyprázdní skupinu střel nepřátel.
        # Znovu naplní skupinu nepřátel.
        for row in range(3):
            for col in range(10):
                enemy = Enemy(50 + col * 60, 50 + row * 40)
                enemies.add(enemy)
        enemy_direction = 1 # Resetuje směr nepřátel.
        score = 0 # Resetuje skóre.
        game_state = GAME_RUNNING # Nastaví stav hry na běží.

    # První inicializace nepřátel.
    reset_game()

    running = True # Proměnná pro řízení herní smyčky.
    while running:
        # --- Zpracování událostí ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # Pokud uživatel zavře okno.
                running = False # Ukončí herní smyčku.
            elif event.type == pygame.KEYDOWN: # Pokud je stisknuta klávesa.
                if game_state == GAME_RUNNING:
                    if event.key == pygame.K_LEFT: # Šipka doleva.
                        player.speed_x = -PLAYER_SPEED # Nastaví rychlost hráče doleva.
                    elif event.key == pygame.K_RIGHT: # Šipka doprava.
                        player.speed_x = PLAYER_SPEED # Nastaví rychlost hráče doprava.
                    elif event.key == pygame.K_SPACE: # Mezerník.
                        new_bullet = player.shoot() # Pokusí se vystřelit.
                        if new_bullet: # Pokud byla střela vytvořena (není cooldown).
                            player_bullets.add(new_bullet) # Přidá střelu do skupiny.
                elif game_state in (GAME_OVER, GAME_WIN): # Pokud je hra u konce.
                    if event.key == pygame.K_r: # Klávesa 'R' pro restart.
                        reset_game() # Resetuje hru.

            elif event.type == pygame.KEYUP: # Pokud je klávesa uvolněna.
                if game_state == GAME_RUNNING:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        player.speed_x = 0 # Zastaví pohyb hráče.

        # --- Aktualizace herního stavu (pouze pokud hra běží) ---
        if game_state == GAME_RUNNING:
            player.update() # Aktualizuje pozici hráče.

            # Aktualizace nepřátel a změna směru.
            move_down = False # Příznak, zda se mají nepřátelé posunout dolů.
            for enemy in enemies:
                enemy.update(enemy_direction) # Aktualizuje pozici nepřítele.
                # Kontrola, zda nepřítel dosáhl okraje obrazovky.
                if enemy.rect.right >= SCREEN_WIDTH or enemy.rect.left <= 0:
                    move_down = True # Nastaví příznak pro posun dolů.
                # Náhodná střelba nepřátel.
                if random.random() < ENEMY_SHOT_CHANCE:
                    enemy_bullets.add(enemy.shoot()) # Přidá nepřátelskou střelu.

            if move_down: # Pokud se mají nepřátelé posunout dolů.
                enemy_direction *= -1 # Obrátí směr pohybu nepřátel.
                for enemy in enemies:
                    enemy.rect.y += ENEMY_DROP_DISTANCE # Posune nepřítele dolů.
                    # Kontrola, zda nepřátelé dosáhli spodní části obrazovky (Game Over).
                    if enemy.rect.bottom >= SCREEN_HEIGHT - player.rect.height:
                        game_state = GAME_OVER # Hra končí.

            # Aktualizace střel hráče.
            player_bullets.update()
            # Odstranění střel, které opustily obrazovku.
            for bullet in player_bullets:
                if bullet.rect.bottom < 0:
                    player_bullets.remove(bullet)

            # Aktualizace střel nepřátel.
            enemy_bullets.update()
            # Odstranění střel, které opustily obrazovku.
            for bullet in enemy_bullets:
                if bullet.rect.top > SCREEN_HEIGHT:
                    enemy_bullets.remove(bullet)

            # --- Detekce kolizí ---
            # Kolize hráčových střel s nepřáteli.
            # Zničené nepřátele a střely se automaticky odstraní ze skupin.
            hits = pygame.sprite.groupcollide(enemies, player_bullets, True, True)
            for enemy_hit in hits: # Pro každého zničeného nepřítele.
                score += SCORE_PER_ENEMY # Zvýší skóre.

            # Kolize nepřátelských střel s hráčem.
            # Střely se odstraní, hráč ztratí život.
            player_hits = pygame.sprite.spritecollide(player, enemy_bullets, True)
            for hit in player_hits:
                if not player.take_hit(): # Pokud hráč ztratil poslední život.
                    game_state = GAME_OVER # Hra končí.

            # Kontrola, zda hráč vyhrál (všichni nepřátelé zničeni).
            if not enemies: # Pokud je skupina nepřátel prázdná.
                game_state = GAME_WIN # Hráč vyhrál.

        # --- Vykreslování ---
        screen.fill(BLACK) # Vyplní celou obrazovku černou barvou (pozadí).

        if game_state == GAME_RUNNING:
            player.draw(screen) # Vykreslí hráče.
            for enemy in enemies: # Projde všechny nepřátele.
                enemy.draw(screen) # Vykreslí každého nepřítele.
            for bullet in player_bullets: # Projde všechny střely hráče.
                bullet.draw(screen) # Vykreslí každou střelu.
            for bullet in enemy_bullets: # Projde všechny střely nepřátel.
                bullet.draw(screen)

            # Zobrazení skóre a životů.
            draw_text(screen, f"Skóre: {score}", 25, YELLOW, SCREEN_WIDTH // 2, 10)
            draw_text(screen, f"Životy: {player.lives}", 25, WHITE, SCREEN_WIDTH - 70, 10)

        elif game_state == GAME_OVER:
            draw_text(screen, "GAME OVER", 64, RED, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50)
            draw_text(screen, f"Vaše skóre: {score}", 36, YELLOW, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 10)
            draw_text(screen, "Stiskněte 'R' pro restart", 24, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 60)
        elif game_state == GAME_WIN:
            draw_text(screen, "VYHRÁLI JSTE!", 64, GREEN, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50)
            draw_text(screen, f"Vaše skóre: {score}", 36, YELLOW, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 10)
            draw_text(screen, "Stiskněte 'R' pro restart", 24, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 60)

        pygame.display.flip() # Aktualizuje celý obsah obrazovky.

        # Omezení snímkové frekvence.
        clock.tick(60) # Hra poběží maximálně na 60 snímků za sekundu.

    pygame.quit() # Odinicializuje Pygame moduly.

if __name__ == "__main__":
    main() # Spustí hlavní herní funkci, pokud je skript spuštěn přímo.
