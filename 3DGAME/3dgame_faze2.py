# Importování základních komponent z knihovny Ursina Engine.
# Přidáváme 'held_keys' pro snadnou detekci stisknutých kláves.
from ursina import Ursina, Entity, color, held_keys, camera, application, Vec3

# Inicializace hlavní aplikace Ursina.
app = Ursina(borderless=False, fullscreen=False, vsync=True)
application.title = "Moje 3D Hra - Fáze 2"

# Vytvoření entity reprezentující zemi (podlahu) ve 3D scéně.
ground = Entity(
    model='plane',
    scale=(100, 1, 100),
    color=color.green.tint(-0.2),
    collider='box'
)

# Definice třídy Player, která dědí z Ursina Entity.
# To nám umožňuje přidat specifickou logiku pro hráče, jako je pohyb a interakce.
class Player(Entity):
    def __init__(self, **kwargs):
        # Volání konstruktoru rodičovské třídy Entity.
        super().__init__(
            model='cube',  # Hráč je reprezentován kostkou.
            color=color.blue,  # Modrá barva pro hráče.
            position=(0, 1, 0),  # Počáteční pozice hráče, mírně nad zemí.
            scale=1,  # Velikost hráče.
            collider='box',  # Kolizní box pro detekci kolizí s prostředím.
            # 'origin_y = -0.5' posune pivot bod kostky dolů, aby stála na zemi.
            # Bez toho by byla polovina kostky pod zemí.
            origin_y=-0.5,
            **kwargs  # Umožňuje předat další argumenty konstruktoru Entity.
        )
        # Nastavení kamery tak, aby sledovala hráče.
        # 'camera.parent = self' znamená, že kamera se bude pohybovat a otáčet s hráčem.
        camera.parent = self
        # Nastavení relativní pozice kamery vůči hráči.
        # Kamera je umístěna mírně vzad a nahoru, aby poskytovala pohled z třetí osoby.
        camera.position = (0, 2, -3)
        # Nastavení úhlu kamery, aby se dívala mírně dolů na hráče.
        camera.rotation_x = 15

        # Nastavení rychlosti pohybu hráče.
        self.speed = 5

    # Metoda 'update' je volána každým snímkem hry.
    # Zde se implementuje logika pohybu hráče.
    def update(self):
        # Resetování rychlosti pohybu pro aktuální snímek.
        # To zajišťuje, že se hráč nepohybuje, pokud nejsou stisknuty žádné klávesy.
        self.x += held_keys['d'] * self.speed * application.time_scale
        self.x -= held_keys['a'] * self.speed * application.time_scale
        self.z += held_keys['w'] * self.speed * application.time_scale
        self.z -= held_keys['s'] * self.speed * application.time_scale

        # 'application.time_scale' zajišťuje, že pohyb je plynulý a nezávislý na snímkové frekvenci.
        # 'held_keys' je slovník, který obsahuje stav všech stisknutých kláves.
        # Pokud je klávesa stisknuta, její hodnota je 1, jinak 0.

# Vytvoření instance hráče.
player = Player()

# Přidání několika statických objektů do scény pro vytvoření prostředí.
# Tyto objekty slouží jako vizuální referenční body a překážky.
wall1 = Entity(model='cube', color=color.gray, scale=(1, 3, 10), position=(5, 1.5, 0), collider='box')
wall2 = Entity(model='cube', color=color.gray, scale=(1, 3, 10), position=(-5, 1.5, 0), collider='box')
obstacle1 = Entity(model='cube', color=color.red, scale=(2, 2, 2), position=(0, 1, 5), collider='box')
obstacle2 = Entity(model='sphere', color=color.orange, scale=1.5, position=(3, 0.75, -3), collider='sphere')

# Spuštění hlavní smyčky aplikace Ursina.
app.run()
