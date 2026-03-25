# TETRIS - Projektová dokumentace

## Název projektu
TETRIS

## Popis a cíl projektu
Cílem tohoto projektu je vytvořit funkční implementaci klasické blokové logické hry Tetris v programovacím jazyce Python. Hra bude spuštěna v konzolovém prostředí a bude simulovat základní mechaniky originální hry, včetně padání bloků (tetromino), jejich otáčení, pohybu a odstraňování plných řádků. Hlavním cílem je poskytnout plně hratelnou verzi hry, která bude demonstrovat pochopení objektově orientovaného programování, algoritmizace a správy herního stavu.

## Popis funkcionality programu (Fáze 1)
V první fázi projektu je kladen důraz na vytvoření základní struktury a definici klíčových komponent hry. Program bude obsahovat:
*   **Herní desku (Board):** Reprezentace hracího pole, kde se budou bloky pohybovat a usazovat. Bude definována její velikost a způsob ukládání informací o obsazených polích.
*   **Tetromino (Herní bloky):** Definice různých tvarů tetromino, jejich počátečních pozic, barev (pro vizualizaci, i když v konzoli to bude textové) a možných rotací. Každé tetromino bude mít své vlastní vlastnosti a metody pro manipulaci.
*   **Inicializace hry:** Nastavení počátečního stavu herní desky a prvního padajícího tetromino.
*   **Záchytné body:** Struktura pro budoucí implementaci herní smyčky a uživatelského vstupu.

Tato fáze se zaměřuje na vytvoření robustního základu, na kterém bude možné v dalších fázích stavět komplexnější herní logiku.

## Technická část (Fáze 1)
*   **Použité knihovny:** Pro tuto fázi nejsou vyžadovány žádné externí knihovny. Vše bude implementováno pomocí standardních Pythonových modulů.
*   **Algoritmy:**
    *   **Reprezentace herní desky:** Použití dvourozměrného seznamu (list of lists) pro reprezentaci herní desky, kde každá buňka bude obsahovat informaci o tom, zda je prázdná, nebo obsazená částí tetromino.
    *   **Reprezentace tetromino:** Každé tetromino bude reprezentováno jako třída, která bude obsahovat seznam souřadnic (relativních k jeho středu nebo kotevnímu bodu) pro každý svůj tvar a rotaci.
*   **Vlastní datové struktury:**
    *   Třída `Board`: Spravuje stav hrací plochy.
    *   Třída `Tetromino`: Abstraktní základní třída pro všechny typy tetromino.
    *   Děděné třídy pro konkrétní tvary tetromino (např. `I_Tetromino`, `J_Tetromino`, `L_Tetromino`, `O_Tetromino`, `S_Tetromino`, `T_Tetromino`, `Z_Tetromino`).
*   **Volání externího API:** Není použito.