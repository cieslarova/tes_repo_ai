# Importování základních komponent z knihovny Ursina Engine.
# Přidáváme 'mouse' pro možnost otáčení kamery myší a 'Sky' pro pozadí.
from ursina import Ursina, Entity, color, held_keys, camera, application, Vec3, mouse, Sky, scene

# Inicializace hlavní aplikace Ursina.
app = Ursina(borderless=False, fullscreen=False, vsync=True)
application.title = "Moje 3D Hra - Fáze 3"

# Nastavení oblohy pro realističtější pozadí.
# 'Sky' je jednoduchá entita, která vykresluje oblohu kolem scény.
Sky(texture='sky_default') # Používá výchozí texturu oblohy.

# Vytvoření entity reprezentující zemi (podlahu) ve 3D scéně.
# Nyní s texturou trávy pro lepší vizuální dojem.
ground = Entity(
    model='plane',
    scale=(100, 1, 100),
    texture='grass',  # Používá texturu trávy. Ursina automaticky najde 'grass.png' nebo 'grass.jpg'.
    texture_scale=(100, 100), # Opakuje texturu 100x na šířku a délku, aby nevypadala rozmazaně.
    color=color.green.tint(-0.1), # Mírné zatmavení zelené barvy.
    collider='box'
)

# Definice třídy Player, která dědí z Ursina Entity.
class Player(Entity):
    def __init__(self, **kwargs):
        super().__init__(
            model='cube',
            color=color.blue,
            position=(0, 1, 0),
            scale=1,
            collider='box',
            origin_y=-0.5,
            **kwargs
        )
        # Kamera je stále navázána na hráče.
        camera.parent = self
        # Pozice kamery je upravena pro lepší pohled z třetí osoby.
        camera.position = (0, 2.5, -4)
        camera.rotation_x = 20 # Mírně se dívá dolů.

        self.speed = 5
        self.jump_height = 1 # Výška skoku.
        self.gravity = 0.5 # Gravitace pro pád.
        self.velocity_y = 0 # Vertikální rychlost pro skok a pád.
        self.is_grounded = True # Indikátor, zda je hráč na zemi.

        # Nastavení citlivosti myši pro otáčení kamery.
        self.mouse_sensitivity = 100

    # Metoda 'input' je volána, když je stisknuta nebo uvolněna klávesa.
    def input(self, key):
        # Pokud je stisknuta mezerník a hráč je na zemi, skočí.
        if key == 'space' and self.is_grounded:
            self.velocity_y = self.jump_height
            self.is_grounded = False # Hráč už není na zemi.

    # Metoda 'update' je volána každým snímkem hry.
    def update(self):
        # Pohyb hráče vpřed/vzad a do stran.
        # 'self.forward' a 'self.right' jsou vektory směru hráče.
        # 'application.time_scale' zajišťuje plynulý pohyb nezávislý na FPS.
        if held_keys['w']:
            self.position += self.forward * self.speed * application.time_scale
        if held_keys['s']:
            self.position -= self.forward * self.speed * application.time_scale
        if held_keys['d']:
            self.position += self.right * self.speed * application.time_scale
        if held_keys['a']:
            self.position -= self.right * self.speed * application.time_scale

        # Aplikace gravitace.
        self.velocity_y -= self.gravity * application.time_scale
        self.y += self.velocity_y

        # Detekce kolize s podlahou pro resetování skoku.
        # 'raycast' je paprsek, který kontroluje, zda něco zasáhne.
        # Zde se kontroluje, zda je pod hráčem země.
        hit_info = self.intersects(ignore=[self, ground]) # Ignorujeme hráče samotného a zemi, abychom nekolidovali s sebou.
        if hit_info.hit and hit_info.entity == ground and self.velocity_y < 0:
            self.y = hit_info.point.y + self.scale_y / 2 # Nastaví hráče přesně na zem.
            self.velocity_y = 0
            self.is_grounded = True

        # Otáčení hráče a kamery myší.
        # 'mouse.x' a 'mouse.y' jsou pozice myši na obrazovce.
        # 'mouse.velocity' je rychlost pohybu myši.
        if mouse.right: # Pouze pokud je stisknuto pravé tlačítko myši.
            self.rotation_y += mouse.velocity[0] * self.mouse_sensitivity
            camera.rotation_x -= mouse.velocity[1] * self.mouse_sensitivity
            # Omezení rotace kamery, aby se nedívala příliš nahoru nebo dolů.
            camera.rotation_x = max(-90, min(90, camera.rotation_x))

# Vytvoření instance hráče.
player = Player()

# Přidání několika statických objektů do scény s různými modely a texturami.
# To pomáhá vytvořit bohatší a vizuálně zajímavější 3D prostředí.
Entity(model='cube', texture='brick', scale=(1, 3, 10), position=(5, 1.5, 0), collider='box')
Entity(model='cube', texture='brick', scale=(1, 3, 10), position=(-5, 1.5, 0), collider='box')
Entity(model='sphere', texture='rock', scale=2, position=(0, 1, 5), collider='sphere')
Entity(model='cone', color=color.orange, scale=1.5, position=(3, 0.75, -3), collider='box')
Entity(model='cube', texture='wood', scale=(4, 0.5, 4), position=(-4, 0.25, -6), collider='box')
Entity(model='cube', texture='stone', scale=(2, 2, 2), position=(7, 1, 7), collider='box')

# Spuštění hlavní smyčky aplikace Ursina.
app.run()
