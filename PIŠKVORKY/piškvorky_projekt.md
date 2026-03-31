# Projekt: Piškvorky

## Název projektu
Piškvorky

## Popis a cíl projektu
Cílem tohoto projektu je vytvořit plně funkční konzolovou hru Piškvorky (Tic-Tac-Toe) pro dva hráče. Hra bude implementována v jazyce Python a bude se řídit standardními pravidly Piškvorek na mřížce 3x3. Projekt slouží k procvičení objektově orientovaného programování, správy herního stavu a interakce s uživatelem v textovém prostředí.

## Popis funkcionality programu (Fáze 1)
V první fázi projektu je kladen důraz na vytvoření základní struktury programu pomocí objektově orientovaného přístupu. Bude definována hlavní třída `Game`, která bude orchestrátorem celé hry. Dále bude vytvořena třída `Board` pro reprezentaci hrací plochy a třída `Player` pro správu informací o jednotlivých hráčích.

**Konkrétní funkcionality Fáze 1:**
*   **Třída `Game`:** Bude obsahovat inicializační logiku pro spuštění hry, nastavení hráčů a hrací plochy. Zatím nebude implementovat herní smyčku ani logiku tahů.
*   **Třída `Board`:** Bude zodpovědná za vytvoření prázdné hrací plochy (mřížky 3x3) a její inicializaci. Bude mít metodu pro zobrazení aktuálního stavu plochy, která zatím jen vypíše prázdnou mřížku.
*   **Třída `Player`:** Bude uchovávat jméno hráče a jeho symbol (X nebo O).
*   **Inicializace:** Program po spuštění inicializuje instanci hry, vytvoří hráče a hrací plochu.

## Technická část (Fáze 1)
*   **Použité knihovny:** V této fázi nebudou použity žádné externí knihovny, pouze standardní funkce Pythonu.
*   **Algoritmy:** Žádné složité algoritmy nejsou v této fázi potřeba. Jde primárně o strukturování kódu.
*   **Vlastní datové struktury:**
    *   Hrací plocha bude reprezentována jako vnořený seznam (list of lists) v rámci třídy `Board`, kde každý prvek bude představovat políčko na mřížce. Inicializována bude prázdnými řetězci nebo speciálním znakem.
    *   Třídy `Game`, `Board`, `Player` budou sloužit jako základní stavební kameny pro objektovou strukturu hry.
*   **Volání externího API:** Není relevantní pro tento projekt.
*   **Ošetření chyb:** V této fázi není implementováno ošetření chyb, jelikož se zaměřujeme na základní strukturu.

## Popis funkcionality programu (Fáze 2)
V druhé fázi projektu byla implementována základní herní smyčka a interakce s uživatelem. Hra nyní umožňuje hráčům střídavě zadávat tahy a zobrazuje aktuální stav hrací plochy po každém tahu.

**Konkrétní rozšíření Fáze 2:**
*   **Herní smyčka:** Třída `Game` nyní obsahuje metodu `run()`, která řídí hlavní průběh hry. Smyčka se opakuje, dokud není hra ukončena (zatím bez kontroly vítěze nebo remízy).
*   **Zpracování vstupu hráče:** Hráči jsou vyzváni k zadání souřadnic (řádek a sloupec), kam chtějí umístit svůj symbol. Vstup je načítán z konzole.
*   **Umístění symbolu na plochu:** Třída `Board` byla rozšířena o metodu `make_move()`, která umožňuje umístit symbol aktuálního hráče na zadané souřadnice.
*   **Přepínání hráčů:** Po každém platném tahu se automaticky přepne na dalšího hráče.
*   **Zobrazení plochy:** Po každém tahu je aktualizovaná hrací plocha zobrazena v konzoli.
*   **Základní validace vstupu:** Byla přidána jednoduchá kontrola, zda zadané souřadnice jsou v rozsahu 0-2. Zatím není řešeno, zda je políčko již obsazené.

## Technická část (Fáze 2)
*   **Rozšíření třídy `Game`:** Byla přidána metoda `run()` pro hlavní herní smyčku a `switch_player()` pro přepínání aktivního hráče.
*   **Rozšíření třídy `Board`:** Byla přidána metoda `make_move(row, col, symbol)` pro umístění symbolu na plochu.
*   **Uživatelský vstup:** Použita vestavěná funkce `input()` pro získání souřadnic od hráče.
*   **Základní ošetření chyb:** Implementována kontrola, zda jsou zadané souřadnice v platném rozsahu (0-2). Neplatné vstupy jsou ignorovány a hráč je vyzván k opakování tahu.