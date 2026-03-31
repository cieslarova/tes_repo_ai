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

## Popis funkcionality programu (Fáze 3)
Ve třetí a finální fázi projektu byla hra Piškvorky kompletně dokončena. Byla implementována veškerá chybějící logika pro kontrolu vítězných podmínek, detekci remízy a robustní ošetření chyb. Hra je nyní plně hratelná a poskytuje zpětnou vazbu o výsledku.

**Konkrétní rozšíření Fáze 3:**
*   **Kontrola vítězných podmínek:** Třída `Board` byla rozšířena o metody pro kontrolu, zda některý z hráčů vytvořil řadu tří stejných symbolů v řádku, sloupci nebo na diagonále.
*   **Detekce remízy:** Hra nyní správně detekuje situaci, kdy je celá hrací plocha zaplněna a žádný hráč nevyhrál.
*   **Robustní ošetření chyb:** Vstup od hráče je nyní důkladně validován, včetně kontroly, zda zadané souřadnice jsou v platném rozsahu a zda je cílové políčko volné. Chybné vstupy jsou jasně komunikovány.
*   **Ukončení hry:** Herní smyčka se nyní správně ukončí, jakmile je detekován vítěz nebo remíza, a oznámí výsledek hry.
*   **Počítadlo tahů:** Bylo přidáno počítadlo tahů pro efektivnější detekci remízy (maximálně 9 tahů na 3x3 ploše).

## Technická část (Fáze 3)
*   **Rozšíření třídy `Board`:**
    *   `check_win(symbol)`: Nová metoda pro kontrolu vítězství pro daný symbol. Prochází všechny řádky, sloupce a obě diagonály.
    *   `is_full()`: Nová metoda pro kontrolu, zda je hrací plocha plná (pro detekci remízy).
*   **Rozšíření třídy `Game`:**
    *   `run()` metoda byla upravena tak, aby po každém tahu volala `check_win()` a `is_full()`.
    *   Byla přidána proměnná `moves_count` pro sledování počtu provedených tahů.
*   **Algoritmy:** Pro kontrolu vítězných podmínek je použit jednoduchý algoritmus procházení mřížky. Pro řádky a sloupce se iteruje přes `self.grid`. Pro diagonály se kontrolují specifické indexy.
*   **Ošetření chyb (try/except):** V metodě `get_player_move` je použito `try-except` pro zachycení `ValueError` v případě, že uživatel zadá nečíselný vstup.
*   **Logika hry:** Celková logika hry je nyní robustní a pokrývá všechny standardní scénáře Piškvorek.