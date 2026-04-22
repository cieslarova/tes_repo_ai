# SPACE INVADERS - Projektová dokumentace

## Název projektu
Space Invaders

## Popis a cíl projektu
Cílem tohoto projektu je vytvořit jednoduchou, ale plně funkční repliku klasické arkádové hry Space Invaders pomocí knihovny Pygame v Pythonu. Hra bude obsahovat hráče, nepřátele (invadery) a střely. Hráč bude ovládat svou loď, střílet na invadery a vyhýbat se jejich střelám. Hlavním cílem je porazit všechny invadery a dosáhnout co nejvyššího skóre.

## Popis funkcionality programu (Fáze 1)
V první fázi projektu je položen základní rámec hry. To zahrnuje inicializaci herního prostředí pomocí Pygame, nastavení okna hry s definovanými rozměry a titulkem. Dále jsou definovány základní třídy pro hlavní herní entity: `Player` (hráčova loď), `Enemy` (nepřátelská loď/invader) a `Bullet` (střela).

*   **Inicializace Pygame:** Program se spustí inicializací knihovny Pygame a vytvořením herního okna.
*   **Herní smyčka:** Je připravena základní herní smyčka, která se stará o udržování hry v chodu, zpracování událostí (např. zavření okna) a aktualizaci obrazovky. V této fázi smyčka pouze vykresluje pozadí a základní entity.
*   **Třída `Player`:** Definuje hráče. Obsahuje inicializační metodu pro nastavení jeho počáteční pozice, rozměrů a obrázku. Metoda `draw` je zodpovědná za vykreslení hráče na obrazovku.
*   **Třída `Enemy`:** Definuje jednoho invadera. Podobně jako `Player` má inicializační metodu pro pozici, rozměry a obrázek. Metoda `draw` invadera vykreslí.
*   **Třída `Bullet`:** Definuje střelu. Inicializační metoda nastavuje pozici, rozměry a barvu/obrázek střely. Metoda `draw` střelu vykreslí.

V této fázi není implementována žádná herní logika jako pohyb, střelba, kolize nebo správa herních stavů. Cílem je pouze vytvořit stabilní základ, na kterém bude možné v dalších fázích stavět.

## Technická část (Fáze 1)
*   **Použité knihovny:** `pygame` pro grafiku a interakci.
*   **Algoritmy:** Žádné složité algoritmy v této fázi nejsou použity. Jde primárně o inicializaci a strukturování kódu.
*   **Vlastní datové struktury:** Třídy `Player`, `Enemy`, `Bullet` slouží jako základní objekty pro reprezentaci herních entit. Každá třída zapouzdřuje data (pozice, rozměry, obrázek) a chování (vykreslení) pro danou entitu.
*   **Volání externího API:** Není použito.
*   **Struktura kódu:** Kód je rozdělen do tříd pro lepší organizaci a budoucí rozšiřitelnost. Konstanty pro nastavení okna jsou definovány na začátku skriptu.