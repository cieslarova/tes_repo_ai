# Importování základních komponent z knihovny Ursina Engine.
# Ursina je jednoduchý herní engine v Pythonu, který usnadňuje tvorbu 3D her.
from ursina import Ursina, Entity, color, EditorCamera, application

# Inicializace hlavní aplikace Ursina.
# Toto vytvoří herní okno a připraví engine pro vykreslování 3D scény.
# 'borderless=False' zajišťuje, že okno má standardní rámeček.
# 'fullscreen=False' spouští hru v okně, nikoli na celou obrazovku.
# 'vsync=True' synchronizuje snímkovou frekvenci s obnovovací frekvencí monitoru,
# což pomáhá předcházet trhání obrazu.
app = Ursina(borderless=False, fullscreen=False, vsync=True)

# Nastavení názvu okna aplikace, který se zobrazí v záhlaví okna.
application.title = "Moje 3D Hra - Fáze 1"

# Vytvoření entity reprezentující zemi (podlahu) ve 3D scéně.
# 'Entity' je základní objekt v Ursina, který může mít model, pozici, barvu atd.
ground = Entity(
    model='plane',  # Používá vestavěný model roviny (plochy).
    scale=(100, 1, 100),  # Nastavuje měřítko země: 100 jednotek na šířku a délku, 1 jednotka na výšku.
    color=color.green.tint(-0.2),  # Nastavuje barvu země na tmavší zelenou.
    collider='box'  # Přidává kolizní box, aby se s ní mohly interagovat jiné objekty.
)

# Vytvoření entity reprezentující hráče.
# V této fázi je hráč jednoduchá kostka, která bude později ovladatelná.
player = Entity(
    model='cube',  # Používá vestavěný model kostky.
    color=color.blue,  # Nastavuje barvu hráče na modrou.
    position=(0, 1, 0),  # Umisťuje hráče na pozici (x=0, y=1, z=0).
                        # 'y=1' zajišťuje, že hráč stojí na zemi (jeho spodní část je na y=0).
    scale=1,  # Nastavuje měřítko hráče na 1 jednotku.
    collider='box'  # Přidává kolizní box pro interakci s prostředím.
)

# Nastavení kamery pro vývojové účely.
# 'EditorCamera' umožňuje volný pohyb kamerou pomocí myši a klávesnice (WASD, Q/E),
# což je velmi užitečné pro prohlížení scény během vývoje.
# V pozdějších fázích bude tato kamera nahrazena kamerou navázanou na hráče.
EditorCamera()

# Spuštění hlavní smyčky aplikace Ursina.
# Tato funkce začne vykreslovat scénu a zpracovávat události.
# Hra bude běžet, dokud nebude okno zavřeno.
app.run()
