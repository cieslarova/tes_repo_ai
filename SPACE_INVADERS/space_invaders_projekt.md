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

## Popis funkcionality programu (Fáze 2)
Ve druhé fázi projektu byla implementována základní funkční logika pro pohyb herních entit a střelbu. Hra nyní reaguje na uživatelský vstup a nepřátelé se začínají pohybovat.

*   **Pohyb hráče:** Hráčova loď se nyní může pohybovat doleva a doprava na základě stisknutých kláves (šipky vlevo/vpravo). Pohyb je omezen hranicemi herního okna.
*   **Střelba hráče:** Hráč může vystřelit střelu stisknutím mezerníku. Střely se pohybují směrem nahoru. Je implementováno jednoduché omezení rychlosti střelby, aby hráč nemohl střílet příliš rychle.
*   **Pohyb nepřátel:** Nepřátelské lodě se pohybují jako skupina. Celá formace se posouvá doleva a doprava a po dosažení okraje obrazovky se posune o řádek níže.
*   **Aktualizace střel:** Všechny aktivní střely (jak hráčovy, tak nepřátelské, i když nepřátelské střelby zatím nejsou implementovány) se aktualizují v každém snímku hry, pohybují se ve svém definovaném směru. Střely, které opustí obrazovku, jsou odstraněny, aby se šetřily systémové zdroje.

## Technická část (Fáze 2)
*   **Rozšíření tříd:** Třídy `Player`, `Enemy` a `Bullet` byly rozšířeny o metody `update()` pro řízení jejich pohybu a chování.
*   **Správa událostí:** Herní smyčka nyní aktivně zpracovává události stisku kláves (`pygame.KEYDOWN`, `pygame.KEYUP`) pro řízení pohybu hráče a střelby.
*   **Seznamy entit:** Pro správu více nepřátel a střel jsou použity Python seznamy, které se v každém snímku aktualizují a filtrují (např. odstranění střel mimo obrazovku).
*   **Časovač střelby:** Pro omezení frekvence střelby hráče je použit jednoduchý časovač (`last_shot_time`).

## Popis funkcionality programu (Fáze 3)
Ve třetí a finální fázi projektu byla hra Space Invaders dokončena s implementací kolizí, správy skóre, životů, herních stavů a nepřátelské střelby. Hra je nyní plně hratelná s jasnými cíli a podmínkami pro výhru/prohru.

*   **Detekce kolizí:**
    *   **Hráčovy střely vs. Nepřátelé:** Když hráčova střela zasáhne nepřítele, nepřítel je odstraněn a hráč získá body.
    *   **Nepřátelské střely vs. Hráč:** Když nepřátelská střela zasáhne hráče, hráč ztratí jeden život. Po vyčerpání všech životů hra končí.
    *   **Nepřátelé vs. Hráč:** Pokud nepřátelé dosáhnou spodní části obrazovky (kde je hráč), hra okamžitě končí.
*   **Správa skóre:** Hráč získává body za zničené nepřátele. Skóre je zobrazeno na obrazovce.
*   **Správa životů:** Hráč má omezený počet životů, které se snižují při zásahu nepřátelskou střelou. Počet zbývajících životů je zobrazen.
*   **Herní stavy:** Hra nyní rozlišuje mezi stavy `RUNNING`, `GAME_OVER` a `WIN`.
    *   `RUNNING`: Standardní herní stav.
    *   `GAME_OVER`: Zobrazí zprávu "GAME OVER" a skóre, umožní restart.
    *   `WIN`: Zobrazí zprávu "YOU WIN!" a skóre, umožní restart.
*   **Nepřátelská střelba:** Nepřátelé nyní náhodně střílí střely směrem dolů. Frekvence střelby se může zvyšovat s postupem hry nebo s menším počtem nepřátel.
*   **Restart hry:** Po skončení hry (výhra/prohra) je možné hru restartovat stisknutím klávesy 'R'.
*   **Vylepšená stabilita:** Bylo přidáno základní ošetření chyb při inicializaci Pygame a načítání obrázků (i když obrázky jsou stále placeholder).

## Technická část (Fáze 3)
*   **Skupiny spritů:** Pro efektivní detekci kolizí jsou široce využívány `pygame.sprite.Group` a funkce `pygame.sprite.groupcollide()` a `pygame.sprite.spritecollide()`.
*   **Herní stavový automat:** Pro řízení toku hry je použit jednoduchý stavový automat (proměnná `game_state`).
*   **Náhodná střelba nepřátel:** Modul `random` je použit pro simulaci náhodné střelby nepřátel.
*   **Zobrazení textu:** Pro zobrazení skóre, životů a zpráv o stavu hry je použito vykreslování textu pomocí `pygame.font`.
*   **Resetovací logika:** Funkce `reset_game()` byla implementována pro snadné obnovení všech herních entit a proměnných do počátečního stavu.
*   **Error Handling:** Základní `try-except` bloky by mohly být přidány pro robustnější načítání zdrojů, ale pro tuto školní úlohu je dostačující kontrola `pygame.get_error()`.
*   **Optimalizace:** Odstranění střel a nepřátel z paměti po kolizi nebo opuštění obrazovky pomáhá udržet výkon.