# Coin Collector - Projektová dokumentace

## Název projektu
Coin Collector

## Popis a cíl projektu
Cílem projektu je vytvořit jednoduchou 3D hru, ve které hráč ovládá postavu v otevřeném virtuálním prostředí (poli) a jeho úkolem je sbírat rozmístěné mince. Hra má sloužit jako demonstrace základních principů 3D programování, interakce s objekty a správy herního stavu. Klade se důraz na přehlednost kódu, modularitu a dodržování dobrých programovacích praktik.

## Popis funkcionality programu - Fáze 1: Základní scéna a modely
V první fázi projektu je kladen důraz na vytvoření základního 3D prostředí a načtení všech klíčových herních objektů. Program po spuštění inicializuje 3D okno a zobrazí statickou scénu. Tato scéna bude obsahovat:
1.  **Terén (pole):** Jednoduchá rovinná plocha, která reprezentuje herní pole.
2.  **Hráč:** Model reprezentující postavu hráče, umístěný na terénu. V této fázi se hráč nebude pohybovat.
3.  **Mince:** Jeden nebo více modelů mincí, staticky rozmístěných na terénu. Tyto mince zatím nebudou sbíratelné.
4.  **Kamera a osvětlení:** Základní nastavení kamery pro zobrazení scény a jednoduché osvětlení, aby byly objekty viditelné.

Tato fáze slouží jako základ pro další vývoj, ověřuje správné nastavení 3D enginu a načítání grafických assetů.

## Technická část - Fáze 1
*   **Použité knihovny:** Pro 3D grafiku a herní logiku je použita knihovna `Panda3D`. Tato knihovna je zvolena pro svou flexibilitu a schopnost vytvářet jak jednoduché, tak komplexní 3D aplikace.
*   **Algoritmy:** V této fázi nejsou implementovány žádné složité algoritmy. Hlavní činností je inicializace `Panda3D` aplikace (`ShowBase`).
*   **Vlastní datové struktury:** Jsou definovány základní třídy pro hru (`CoinCollectorGame`), hráče (`Player`) a mince (`Coin`), které slouží jako kontejnery pro jejich 3D modely a základní vlastnosti.
*   **Scénický graf (Scene Graph):** `Panda3D` využívá hierarchický scénický graf pro organizaci 3D objektů. V této fázi jsou modely terénu, hráče a mincí připojeny k tomuto grafu jako `NodePath` objekty.
*   **Načítání modelů:** 3D modely (např. ve formátu `.egg` nebo `.gltf`) jsou načítány pomocí metody `loader.loadModel()`. Pro účely této ukázky budou použity jednoduché geometrické tvary generované přímo v kódu (`render.attachNewNode("model_name")` a `loader.loadModel("models/sphere")` apod.) nebo se předpokládá jejich existence v adresáři `models`.
*   **Inicializace kamery a osvětlení:** Kamera je nastavena do výchozí pozice a orientace. Je přidáno základní ambientní a směrové osvětlení (`DirectionalLight`) pro zajištění viditelnosti scény.

## Popis funkcionality programu - Fáze 2: Pohyb hráče, sbírání mincí a skóre
Druhá fáze projektu rozšiřuje základní scénu o interaktivní prvky a herní logiku. Hlavním cílem je umožnit hráči pohybovat se po terénu, dynamicky generovat mince a implementovat mechanismus jejich sbírání, včetně počítání skóre.

**Klíčové rozšíření funkcionality:**
1.  **Pohyb hráče:** Hráč je nyní schopen pohybovat se po terénu pomocí klávesnice (např. WASD nebo šipky). Pohyb je plynulý a reaguje na stisknutí kláves.
2.  **Generování mincí:** Mince jsou generovány dynamicky na náhodných pozicích v rámci herního pole. Tím se zajišťuje variabilita každé hry.
3.  **Detekce kolizí:** Je implementován jednoduchý systém detekce kolizí mezi hráčem a mincemi. Při kontaktu hráče s mincí je mince považována za sebranou.
4.  **Sbírání mincí a skóre:** Sebraná mince zmizí ze scény a hráčovo skóre se zvýší. Aktuální skóre je zobrazeno na obrazovce pomocí jednoduchého textového UI prvku.
5.  **Kamera sledující hráče:** Kamera je upravena tak, aby sledovala hráče, což zlepšuje herní zážitek a udržuje hráče vždy v centru dění.

## Technická část - Fáze 2
*   **Pohyb hráče:** Využívá se systém `task` z `Panda3D` pro pravidelnou aktualizaci pozice hráče v každém snímku. Vstup z klávesnice je zpracováván pomocí `base.accept()` pro mapování kláves na akce (pohyb vpřed, vzad, vlevo, vpravo).
*   **Generování mincí:** Mince jsou generovány pomocí `random` modulu pro určení náhodných X a Y souřadnic v rámci definovaných hranic terénu.
*   **Kolizní systém:** `Panda3D` poskytuje robustní kolizní systém. Pro hráče a mince jsou přidány `CollisionSphere` (kolizní koule) jako kolizní tělesa. `CollisionHandlerQueue` je použit pro zpracování detekovaných kolizí. V každém snímku je spuštěn kolizní traverser, který kontroluje překrývání kolizních těles.
*   **Správa skóre a UI:** Skóre je udržováno jako jednoduchá číselná proměnná. Pro zobrazení skóre na obrazovce je použit `OnscreenText` z `Panda3D`, který umožňuje snadné vkládání textových prvků do 2D rozhraní.
*   **Kamera:** Kamera je dynamicky aktualizována v `task` funkci, aby udržovala relativní pozici vůči hráči, čímž ho efektivně sleduje.

## Popis funkcionality programu - Fáze 3: Vylepšení, herní logika a robustnost
Třetí a finální fáze projektu se zaměřuje na dokončení herní logiky, zvýšení robustnosti programu a vylepšení uživatelského zážitku. Cílem je vytvořit plně hratelnou verzi hry s jasnými herními stavy a základním ošetřením chyb.

**Klíčové rozšíření funkcionality:**
1.  **Herní stavy:** Je implementován systém herních stavů (např. "playing", "game_over"), který řídí chování hry v různých fázích.
2.  **Podmínka konce hry:** Hra nyní obsahuje podmínku pro konec hry (např. po sebrání určitého počtu mincí nebo uplynutí času).
3.  **Restart hry:** Po skončení hry je hráči nabídnuta možnost restartovat hru, což vede k novému začátku se všemi resetovanými parametry.
4.  **Vylepšené UI:** Uživatelské rozhraní je rozšířeno o zprávy informující o stavu hry (např. "Game Over", "Stiskněte R pro restart").
5.  **Ošetření chyb:** Jsou přidány základní mechanismy pro ošetření potenciálních chyb, například při načítání 3D modelů, což zvyšuje stabilitu aplikace.
6.  **Zvukové efekty (volitelné):** I když nejsou přímo implementovány v kódu pro zachování stručnosti, je v dokumentaci zmíněna možnost přidání zvukových efektů pro sbírání mincí, což by dále zlepšilo herní zážitek.

## Technická část - Fáze 3
*   **Herní stavy:** Herní stavy jsou spravovány pomocí stavové proměnné (např. `self.game_state`). Logika hry (pohyb, kolize, UI) se podmiňuje aktuálním stavem.
*   **Konec hry a restart:** Po dosažení podmínky konce hry (např. `self.max_coins_to_collect` nebo `self.game_timer`) je herní stav přepnut na "game_over". V tomto stavu je zobrazeno UI pro restart a je aktivováno naslouchání na klávesu pro restart (např. 'r'). Funkce pro restart (`self.reset_game()`) resetuje skóre, pozici hráče, mince a herní stav.
*   **Vylepšené UI:** `OnscreenText` je dynamicky aktualizován pro zobrazení různých zpráv v závislosti na herním stavu.
*   **Ošetření chyb:** Při načítání modelů (`loader.loadModel()`) je použito `try-except` bloků. Pokud model není nalezen, program se nesesype, ale vypíše varování a případně použije zástupný objekt nebo ukončí hru elegantně.
*   **Správa tasků:** Tasky pro pohyb hráče a kontrolu kolizí jsou pozastaveny nebo obnoveny v závislosti na herním stavu, aby se zabránilo interakcím mimo aktivní hru.

**Závěrečné zhodnocení dokončení projektu:**
Projekt "Coin Collector" dosáhl plně hratelné verze, která splňuje původní cíle. Byla úspěšně implementována základní 3D scéna, interaktivní pohyb hráče, dynamické generování a sbírání mincí s počítáním skóre. Dále byla přidána robustní správa herních stavů, možnost restartu a základní ošetření chyb, což zvyšuje stabilitu a uživatelskou přívětivost aplikace. Použití knihovny Panda3D umožnilo efektivní práci s 3D prostředím a herní logikou. Projekt je připraven k dalšímu rozšíření o pokročilejší funkce, jako jsou různé úrovně, nepřátelé, vylepšená grafika nebo zvukové efekty.