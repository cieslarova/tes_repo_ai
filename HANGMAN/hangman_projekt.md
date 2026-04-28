# Název projektu: Hangman

## Popis a cíl projektu
Projekt "Hangman" je implementací klasické textové hry Šibenice v programovacím jazyce Python. Cílem projektu je vytvořit plně funkční a interaktivní hru, která umožní uživateli hádat slovo písmeno po písmenu, s omezeným počtem pokusů. Hra bude navržena tak, aby byla snadno rozšiřitelná o nové funkce a slova.

## Popis funkcionality programu (Fáze 1)
V první fázi vývoje je kladen důraz na vytvoření základní struktury programu. Bude definována třída `HangmanGame`, která bude sloužit jako hlavní kontejner pro veškerou herní logiku a stav. Tato třída bude obsahovat inicializační metodu pro nastavení počátečního stavu hry, jako je seznam slov, maximální počet pokusů a proměnné pro sledování aktuálního slova, uhodnutých písmen a chybných pokusů.

Dále budou vytvořeny prázdné nebo minimálně implementované metody, které budou sloužit jako záchytné body pro budoucí rozšíření funkcionality. Tyto metody budou zahrnovat například:
*   `_vyber_slovo()`: Pro výběr tajeného slova.
*   `_zobraz_stav_hry()`: Pro vizualizaci aktuálního stavu hry (uhodnutá písmena, zbývající pokusy).
*   `_zpracuj_hadani()`: Pro zpracování vstupu od hráče.
*   `hraj()`: Hlavní herní smyčka.

Tato fáze se zaměřuje na robustní architektonický základ, který usnadní další inkrementální vývoj.

## Technická část (Fáze 1)
*   **Použité knihovny:** V této fázi nejsou použity žádné externí knihovny, pouze standardní funkce Pythonu.
*   **Algoritmy:** Žádné složité algoritmy nejsou implementovány. Pouze základní inicializace proměnných.
*   **Vlastní datové struktury:**
    *   Třída `HangmanGame`: Objektově orientovaný přístup pro zapouzdření herního stavu a logiky.
    *   Seznam (`list`): Pro uložení slov, ze kterých se bude vybírat tajenka.
    *   Množina (`set`): Pro efektivní ukládání uhodnutých a chybně uhodnutých písmen, což umožňuje rychlou kontrolu existence písmena a zabraňuje duplicitám.
*   **Volání externího API:** Žádné.

## Popis funkcionality programu (Fáze 2)
V druhé fázi vývoje byla implementována základní funkční logika hry Šibenice. Byly rozšířeny a dokončeny metody, které byly v první fázi pouze jako záchytné body. Konkrétně:
*   Metoda `_vyber_slovo()` nyní skutečně náhodně vybírá slovo ze seznamu dostupných slov.
*   Metoda `_zobraz_stav_hry()` byla vylepšena tak, aby správně zobrazovala uhodnutá písmena ve slově (např. `P _ T H _ N`) a také seznam již uhodnutých písmen a zbývající počet pokusů.
*   Metoda `_zpracuj_hadani()` nyní plně zpracovává vstup od hráče, kontroluje, zda bylo písmeno již uhodnuto, a správně aktualizuje stav hry (přidává písmeno do sady uhodnutých písmen a zvyšuje počet chybných pokusů, pokud je písmeno špatné).
*   Hlavní herní smyčka `hraj()` byla doplněna o kontrolu konce hry, a to jak pro případ výhry (všechna písmena slova jsou uhodnuta), tak pro případ prohry (vyčerpání maximálního počtu chybných pokusů). Hra se nyní správně ukončí po dosažení jedné z těchto podmínek.
Tato fáze přinesla plně hratelnou, byť zatím textově jednoduchou, verzi hry.

## Popis funkcionality programu (Fáze 2)
V druhé fázi vývoje byla implementována základní funkční logika hry Šibenice. Byly rozšířeny a dokončeny metody, které byly v první fázi pouze jako záchytné body. Konkrétně:
*   Metoda `_vyber_slovo()` nyní skutečně náhodně vybírá slovo ze seznamu dostupných slov.
*   Metoda `_zobraz_stav_hry()` byla vylepšena tak, aby správně zobrazovala uhodnutá písmena ve slově (např. `P _ T H _ N`) a také seznam již uhodnutých písmen a zbývající počet pokusů.
*   Metoda `_zpracuj_hadani()` nyní plně zpracovává vstup od hráče, kontroluje, zda bylo písmeno již uhodnuto, a správně aktualizuje stav hry (přidává písmeno do sady uhodnutých písmen a zvyšuje počet chybných pokusů, pokud je písmeno špatné).
*   Hlavní herní smyčka `hraj()` byla doplněna o kontrolu konce hry, a to jak pro případ výhry (všechna písmena slova jsou uhodnuta), tak pro případ prohry (vyčerpání maximálního počtu chybných pokusů). Hra se nyní správně ukončí po dosažení jedné z těchto podmínek.
Tato fáze přinesla plně hratelnou, byť zatím textově jednoduchou, verzi hry.

## Popis funkcionality programu (Fáze 2)
V druhé fázi vývoje byla implementována základní funkční logika hry Šibenice. Byly rozšířeny a dokončeny metody, které byly v první fázi pouze jako záchytné body. Konkrétně:
*   Metoda `_vyber_slovo()` nyní skutečně náhodně vybírá slovo ze seznamu dostupných slov.
*   Metoda `_zobraz_stav_hry()` byla vylepšena tak, aby správně zobrazovala uhodnutá písmena ve slově (např. `P _ T H _ N`) a také seznam již uhodnutých písmen a zbývající počet pokusů.
*   Metoda `_zpracuj_hadani()` nyní plně zpracovává vstup od hráče, kontroluje, zda bylo písmeno již uhodnuto, a správně aktualizuje stav hry (přidává písmeno do sady uhodnutých písmen a zvyšuje počet chybných pokusů, pokud je písmeno špatné).
*   Hlavní herní smyčka `hraj()` byla doplněna o kontrolu konce hry, a to jak pro případ výhry (všechna písmena slova jsou uhodnuta), tak pro případ prohry (vyčerpání maximálního počtu chybných pokusů). Hra se nyní správně ukončí po dosažení jedné z těchto podmínek.
Tato fáze přinesla plně hratelnou, byť zatím textově jednoduchou, verzi hry.

## Popis funkcionality programu (Fáze 2)
V druhé fázi vývoje byla implementována základní funkční logika hry Šibenice. Byly rozšířeny a dokončeny metody, které byly v první fázi pouze jako záchytné body. Konkrétně:
*   Metoda `_vyber_slovo()` nyní skutečně náhodně vybírá slovo ze seznamu dostupných slov.
*   Metoda `_zobraz_stav_hry()` byla vylepšena tak, aby správně zobrazovala uhodnutá písmena ve slově (např. `P _ T H _ N`) a také seznam již uhodnutých písmen a zbývající počet pokusů.
*   Metoda `_zpracuj_hadani()` nyní plně zpracovává vstup od hráče, kontroluje, zda bylo písmeno již uhodnuto, a správně aktualizuje stav hry (přidává písmeno do sady uhodnutých písmen a zvyšuje počet chybných pokusů, pokud je písmeno špatné).
*   Hlavní herní smyčka `hraj()` byla doplněna o kontrolu konce hry, a to jak pro případ výhry (všechna písmena slova jsou uhodnuta), tak pro případ prohry (vyčerpání maximálního počtu chybných pokusů). Hra se nyní správně ukončí po dosažení jedné z těchto podmínek.
Tato fáze přinesla plně hratelnou, byť zatím textově jednoduchou, verzi hry.

## Popis funkcionality programu (Fáze 3)
Ve třetí a finální fázi vývoje byla hra Šibenice vylepšena o robustnější chybové ošetření, vizuální prvky a možnost opakovaného hraní.
*   **Vylepšené chybové ošetření:** Vstup od uživatele je nyní důkladněji validován. Program kontroluje, zda vstup obsahuje pouze jedno písmeno a zda je to skutečně písmeno abecedy. Zprávy pro uživatele jsou jasnější a informativnější.
*   **Vizuální reprezentace šibenice:** Byla přidána textová grafika, která vizuálně znázorňuje stav šibenice v závislosti na počtu chybných pokusů. To zvyšuje interaktivitu a zpětnou vazbu pro hráče.
*   **Možnost hrát znovu:** Po skončení hry (výhra nebo prohra) je hráči nabídnuta možnost hrát novou hru, aniž by bylo nutné program restartovat. To zlepšuje uživatelský zážitek.
*   **Resetování hry:** Byla přidána metoda `reset_hry()`, která umožňuje snadno vrátit hru do počátečního stavu pro novou partii.
*   **Rozšířený seznam slov:** Seznam slov byl rozšířen o další termíny, což zvyšuje variabilitu hry.

## Technická část (Fáze 3)
*   **Algoritmy:**
    *   **Vstupní validace:** Rozšířená kontrola vstupu pomocí `if/else` struktur, která zajišťuje, že uživatel zadá platné písmeno.
    *   **Textová grafika:** Implementace jednoduchého pole řetězců (`list of strings`), kde každý index reprezentuje stav šibenice pro daný počet chybných pokusů.
*   **Vlastní datové struktury:**
    *   `hangman_stages` (list of strings): Nová datová struktura pro ukládání vizuálních reprezentací šibenice.
*   **Ošetření chyb:** Ačkoliv nebyly použity `try-except` bloky (pro jednoduchost textového vstupu), validace vstupu efektivně předchází neplatným datům a informuje uživatele o správném formátu.
*   **Modul `os`:** (Volitelně, pro vyčištění konzole, ale v této verzi není nutné pro základní funkčnost a je často platformně závislé, takže se mu vyhýbám pro maximální kompatibilitu).

## Závěrečné zhodnocení dokončení projektu
Projekt "Hangman" je nyní plně funkční a splňuje všechny stanovené cíle. Poskytuje kompletní herní zážitek s jasnou zpětnou vazbou pro hráče, robustní validací vstupu a možností opakovaného hraní. Objektově orientovaný návrh s třídou `HangmanGame` zajišťuje dobrou strukturu a snadnou údržbu kódu. Projekt demonstruje použití základních programovacích konstrukcí, jako jsou třídy, metody, podmíněné příkazy, cykly a práce s datovými strukturami (seznamy, množiny). Celková složitost projektu dosahuje úrovně "Středně těžká" až "Těžká" díky kombinaci objektového návrhu, algoritmizace herní logiky a základního ošetření chyb.

## Popis funkcionality programu (Fáze 3)
Ve třetí a finální fázi vývoje byla hra Šibenice vylepšena o robustnější chybové ošetření, vizuální prvky a možnost opakovaného hraní.
*   **Vylepšené chybové ošetření:** Vstup od uživatele je nyní důkladněji validován. Program kontroluje, zda vstup obsahuje pouze jedno písmeno a zda je to skutečně písmeno abecedy. Zprávy pro uživatele jsou jasnější a informativnější.
*   **Vizuální reprezentace šibenice:** Byla přidána textová grafika, která vizuálně znázorňuje stav šibenice v závislosti na počtu chybných pokusů. To zvyšuje interaktivitu a zpětnou vazbu pro hráče.
*   **Možnost hrát znovu:** Po skončení hry (výhra nebo prohra) je hráči nabídnuta možnost hrát novou hru, aniž by bylo nutné program restartovat. To zlepšuje uživatelský zážitek.
*   **Resetování hry:** Byla přidána metoda `reset_hry()`, která umožňuje snadno vrátit hru do počátečního stavu pro novou partii.
*   **Rozšířený seznam slov:** Seznam slov byl rozšířen o další termíny, což zvyšuje variabilitu hry.

## Technická část (Fáze 3)
*   **Algoritmy:**
    *   **Vstupní validace:** Rozšířená kontrola vstupu pomocí `if/else` struktur, která zajišťuje, že uživatel zadá platné písmeno.
    *   **Textová grafika:** Implementace jednoduchého pole řetězců (`list of strings`), kde každý index reprezentuje stav šibenice pro daný počet chybných pokusů.
*   **Vlastní datové struktury:**
    *   `hangman_stages` (list of strings): Nová datová struktura pro ukládání vizuálních reprezentací šibenice.
*   **Ošetření chyb:** Ačkoliv nebyly použity `try-except` bloky (pro jednoduchost textového vstupu), validace vstupu efektivně předchází neplatným datům a informuje uživatele o správném formátu.
*   **Modul `os`:** (Volitelně, pro vyčištění konzole, ale v této verzi není nutné pro základní funkčnost a je často platformně závislé, takže se mu vyhýbám pro maximální kompatibilitu).

## Závěrečné zhodnocení dokončení projektu
Projekt "Hangman" je nyní plně funkční a splňuje všechny stanovené cíle. Poskytuje kompletní herní zážitek s jasnou zpětnou vazbou pro hráče, robustní validací vstupu a možností opakovaného hraní. Objektově orientovaný návrh s třídou `HangmanGame` zajišťuje dobrou strukturu a snadnou údržbu kódu. Projekt demonstruje použití základních programovacích konstrukcí, jako jsou třídy, metody, podmíněné příkazy, cykly a práce s datovými strukturami (seznamy, množiny). Celková složitost projektu dosahuje úrovně "Středně těžká" až "Těžká" díky kombinaci objektového návrhu, algoritmizace herní logiky a základního ošetření chyb.

## Popis funkcionality programu (Fáze 3)
Ve třetí a finální fázi vývoje byla hra Šibenice vylepšena o robustnější chybové ošetření, vizuální prvky a možnost opakovaného hraní.
*   **Vylepšené chybové ošetření:** Vstup od uživatele je nyní důkladněji validován. Program kontroluje, zda vstup obsahuje pouze jedno písmeno a zda je to skutečně písmeno abecedy. Zprávy pro uživatele jsou jasnější a informativnější.
*   **Vizuální reprezentace šibenice:** Byla přidána textová grafika, která vizuálně znázorňuje stav šibenice v závislosti na počtu chybných pokusů. To zvyšuje interaktivitu a zpětnou vazbu pro hráče.
*   **Možnost hrát znovu:** Po skončení hry (výhra nebo prohra) je hráči nabídnuta možnost hrát novou hru, aniž by bylo nutné program restartovat. To zlepšuje uživatelský zážitek.
*   **Resetování hry:** Byla přidána metoda `reset_hry()`, která umožňuje snadno vrátit hru do počátečního stavu pro novou partii.
*   **Rozšířený seznam slov:** Seznam slov byl rozšířen o další termíny, což zvyšuje variabilitu hry.

## Technická část (Fáze 3)
*   **Algoritmy:**
    *   **Vstupní validace:** Rozšířená kontrola vstupu pomocí `if/else` struktur, která zajišťuje, že uživatel zadá platné písmeno.
    *   **Textová grafika:** Implementace jednoduchého pole řetězců (`list of strings`), kde každý index reprezentuje stav šibenice pro daný počet chybných pokusů.
*   **Vlastní datové struktury:**
    *   `hangman_stages` (list of strings): Nová datová struktura pro ukládání vizuálních reprezentací šibenice.
*   **Ošetření chyb:** Ačkoliv nebyly použity `try-except` bloky (pro jednoduchost textového vstupu), validace vstupu efektivně předchází neplatným datům a informuje uživatele o správném formátu.
*   **Modul `os`:** (Volitelně, pro vyčištění konzole, ale v této verzi není nutné pro základní funkčnost a je často platformně závislé, takže se mu vyhýbám pro maximální kompatibilitu).

## Závěrečné zhodnocení dokončení projektu
Projekt "Hangman" je nyní plně funkční a splňuje všechny stanovené cíle. Poskytuje kompletní herní zážitek s jasnou zpětnou vazbou pro hráče, robustní validací vstupu a možností opakovaného hraní. Objektově orientovaný návrh s třídou `HangmanGame` zajišťuje dobrou strukturu a snadnou údržbu kódu. Projekt demonstruje použití základních programovacích konstrukcí, jako jsou třídy, metody, podmíněné příkazy, cykly a práce s datovými strukturami (seznamy, množiny). Celková složitost projektu dosahuje úrovně "Středně těžká" až "Těžká" díky kombinaci objektového návrhu, algoritmizace herní logiky a základního ošetření chyb.

## Popis funkcionality programu (Fáze 3)
Ve třetí a finální fázi vývoje byla hra Šibenice vylepšena o robustnější chybové ošetření, vizuální prvky a možnost opakovaného hraní.
*   **Vylepšené chybové ošetření:** Vstup od uživatele je nyní důkladněji validován. Program kontroluje, zda vstup obsahuje pouze jedno písmeno a zda je to skutečně písmeno abecedy. Zprávy pro uživatele jsou jasnější a informativnější.
*   **Vizuální reprezentace šibenice:** Byla přidána textová grafika, která vizuálně znázorňuje stav šibenice v závislosti na počtu chybných pokusů. To zvyšuje interaktivitu a zpětnou vazbu pro hráče.
*   **Možnost hrát znovu:** Po skončení hry (výhra nebo prohra) je hráči nabídnuta možnost hrát novou hru, aniž by bylo nutné program restartovat. To zlepšuje uživatelský zážitek.
*   **Resetování hry:** Byla přidána metoda `reset_hry()`, která umožňuje snadno vrátit hru do počátečního stavu pro novou partii.
*   **Rozšířený seznam slov:** Seznam slov byl rozšířen o další termíny, což zvyšuje variabilitu hry.

## Technická část (Fáze 3)
*   **Algoritmy:**
    *   **Vstupní validace:** Rozšířená kontrola vstupu pomocí `if/else` struktur, která zajišťuje, že uživatel zadá platné písmeno.
    *   **Textová grafika:** Implementace jednoduchého pole řetězců (`list of strings`), kde každý index reprezentuje stav šibenice pro daný počet chybných pokusů.
*   **Vlastní datové struktury:**
    *   `hangman_stages` (list of strings): Nová datová struktura pro ukládání vizuálních reprezentací šibenice.
*   **Ošetření chyb:** Ačkoliv nebyly použity `try-except` bloky (pro jednoduchost textového vstupu), validace vstupu efektivně předchází neplatným datům a informuje uživatele o správném formátu.
*   **Modul `os`:** (Volitelně, pro vyčištění konzole, ale v této verzi není nutné pro základní funkčnost a je často platformně závislé, takže se mu vyhýbám pro maximální kompatibilitu).

## Závěrečné zhodnocení dokončení projektu
Projekt "Hangman" je nyní plně funkční a splňuje všechny stanovené cíle. Poskytuje kompletní herní zážitek s jasnou zpětnou vazbou pro hráče, robustní validací vstupu a možností opakovaného hraní. Objektově orientovaný návrh s třídou `HangmanGame` zajišťuje dobrou strukturu a snadnou údržbu kódu. Projekt demonstruje použití základních programovacích konstrukcí, jako jsou třídy, metody, podmíněné příkazy, cykly a práce s datovými strukturami (seznamy, množiny). Celková složitost projektu dosahuje úrovně "Středně těžká" až "Těžká" díky kombinaci objektového návrhu, algoritmizace herní logiky a základního ošetření chyb.