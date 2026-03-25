# TETRIS_projekt.md

## Název projektu
Tetris

## Popis a cíl projektu
Cílem projektu je implementovat klasickou logickou hru Tetris v programovacím jazyce Python s využitím knihovny Pygame pro grafické uživatelské rozhraní. Hra bude simulovat základní mechaniky originálního Tetrisu, kde hráči manipulují s padajícími bloky (tetrominy), aby vytvořili plné vodorovné řady, které se následně odstraní.

Hlavním cílem je vytvořit funkční a hratelnou verzi hry, která bude demonstrovat principy objektově orientovaného programování, algoritmizace pohybu a rotace objektů, detekce kolizí a správy herního stavu. Projekt bude rozdělen do tří fází, přičemž každá fáze bude postupně rozšiřovat funkcionalitu a robustnost kódu.

## Popis funkcionality programu (Fáze 1)
V první fázi projektu je kladen důraz na vytvoření základní struktury a rámce pro budoucí implementaci hry. Program bude schopen:
*   Inicializovat herní okno pomocí Pygame.
*   Definovat základní herní desku (grid), na které se budou bloky pohybovat.
*   Definovat různé typy tetromin (herních bloků) s jejich tvary a barvami.
*   Inicializovat herní stav, včetně aktuálního a následujícího padajícího bloku.
*   Zobrazit prázdnou herní desku a aktuální padající blok v počáteční pozici.
*   Zatím nebude implementována žádná herní logika pro pohyb, rotaci, kolize nebo odstraňování řad. Cílem je připravit stabilní základ pro další vývoj.

## Technická část (Fáze 1)
*   **Použité knihovny:** `pygame` pro grafické rozhraní a události, `random` pro generování náhodných tetromin.
*   **Algoritmy:** V této fázi se primárně jedná o inicializační algoritmy pro nastavení herního prostředí a generování počátečních dat.
*   **Vlastní datové struktury:**
    *   **`Board` třída:** Reprezentuje herní desku jako 2D seznam (list of lists) pro ukládání stavu jednotlivých buněk (prázdná/obsazená blokem a jeho barvou).
    *   **`Tetromino` třída:** Reprezentuje padající blok. Obsahuje:
        *   `shapes`: Slovník nebo seznam obsahující matice (list of lists) definující tvary a rotace pro každý typ tetromina (I, J, L, O, S, T, Z).
        *   `color`: Barva tetromina.
        *   `x`, `y`: Souřadnice levého horního rohu ohraničujícího boxu tetromina na herní desce.
        *   `rotation`: Index aktuální rotace tetromina.
    *   **`Game` třída:** Spravuje celkový herní stav, obsahuje instanci `Board`, aktuální a následující `Tetromino`, skóre a stav hry (game over).
*   **Volání externího API:** Není relevantní v této fázi.
*   **Ošetření chyb:** V této fázi se primárně zaměřujeme na robustní inicializaci a strukturu, ošetření chyb bude rozšířeno v pozdějších fázích.