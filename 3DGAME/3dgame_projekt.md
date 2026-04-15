# Projekt: 3D Hra

## Název projektu
3D Hra

## Popis a cíl projektu
Cílem tohoto projektu je vytvořit jednoduchou interaktivní 3D hru, která demonstruje základní principy 3D grafiky, navigace a interakce v trojrozměrném prostředí. Projekt využívá knihovnu Ursina Engine pro rychlý vývoj a zaměřuje se na postupné budování scény a herní logiky. Hlavním cílem je, aby výsledná aplikace "vypadala více 3D" a poskytovala základní pocit hloubky a prostoru.

## Popis funkcionality programu (Fáze 1)
V první fázi projektu je inicializováno herní okno a vytvořeno základní 3D prostředí. To zahrnuje rovnou plochu (zem), která slouží jako podklad pro scénu, a jednoduchý objekt (kostka), který reprezentuje hráče. Kamera je nastavena tak, aby umožňovala základní pohled na scénu, což je klíčové pro vnímání 3D prostoru. Tato fáze se soustředí na vytvoření stabilního základu, na kterém budou v dalších fázích stavěny složitější funkce.

## Technická část (Fáze 1)
*   **Použité knihovny:** Ursina Engine (pro 3D grafiku a herní logiku).
*   **Základní struktura:**
    *   `Ursina()`: Inicializace hlavního herního okna a aplikace.
    *   `Entity`: Základní stavební blok pro všechny objekty ve scéně. Používá se pro vytvoření země a hráče.
    *   `EditorCamera`: Pro účely vývoje a snadné navigace ve scéně je dočasně použita `EditorCamera`, která umožňuje volný pohyb kamerou. V pozdějších fázích bude nahrazena kamerou navázanou na hráče.
*   **Datové struktury:** V této fázi se nepoužívají žádné složité vlastní datové struktury, pouze základní objekty `Entity` s jejich inherentními vlastnostmi (pozice, model, barva, měřítko).
*   **Algoritmy:** Žádné komplexní algoritmy nejsou v této fázi implementovány, pouze inicializační volání knihovny Ursina.

# Projekt: 3D Hra

## Popis funkcionality programu (Fáze 2)
V této fázi byla implementována základní funkčnost pro pohyb hráče v 3D prostoru. Hráč nyní může být ovládán pomocí klávesnice (WASD pro pohyb vpřed/vzad a do stran). Kamera je nově navázána na hráče, což zajišťuje, že se pohled hráče pohybuje s ním, a zvyšuje tak imerzi a pocit "být ve hře". Pro obohacení scény a poskytnutí vizuálních referencí pro pohyb byly přidány další statické objekty (např. stěny nebo překážky), které pomáhají hráči orientovat se v prostoru a vnímat hloubku.

## Technická část (Fáze 2)
*   **Rozšíření třídy `Entity`:** Byla vytvořena vlastní třída `Player`, která dědí z `Entity` a přidává specifickou logiku pro ovládání a interakci.
*   **Ovládání hráče:**
    *   Metoda `input(key)`: Zpracovává stisknutí kláves (WASD) pro detekci směru pohybu.
    *   Metoda `update()`: Je volána každým snímkem a aktualizuje pozici hráče na základě detekovaných vstupů a jeho rychlosti.
*   **Kamera:** `camera.parent = self` (kde `self` je instance hráče) zajišťuje, že kamera sleduje hráče. `camera.position` a `camera.rotation` jsou upraveny tak, aby poskytovaly pohled z pohledu třetí osoby nebo první osoby.
*   **Přidání objektů:** Další instance `Entity` byly přidány do scény s různými modely, barvami a pozicemi, aby vytvořily jednodušší prostředí.

# Projekt: 3D Hra

## Závěrečné zhodnocení dokončení projektu (Fáze 3)
Projekt 3D hry byl úspěšně dokončen a splnil své primární cíle. Byla vytvořena interaktivní 3D scéna, ve které se hráč může volně pohybovat a interagovat s prostředím. Vizuální stránka hry byla vylepšena přidáním rozmanitějších modelů a textur, což výrazně přispělo k realističtějšímu a hlubšímu 3D zážitku.

Implementace zahrnovala robustnější logiku pro pohyb hráče, včetně základního ošetření kolizí, které zabraňuje hráči procházet skrz pevné objekty. Byly přidány další vizuální prvky, jako jsou různé modely a textury, které obohacují scénu a dávají jí větší hloubku a detail. Projekt demonstruje schopnost pracovat s 3D enginem, postupně rozvíjet herní funkcionalitu a dbát na kvalitu kódu a uživatelského zážitku.

Celkově projekt poskytuje solidní základ pro další rozšíření a ukazuje potenciál knihovny Ursina pro rychlý prototypování a vývoj 3D aplikací.

## Technická část (Fáze 3)
*   **Vylepšená kolizní logika:** Ursina automaticky zpracovává kolize mezi entitami s `collider` vlastností. V této fázi bylo zajištěno, že všechny relevantní objekty mají správně nastavené kolizní boxy/sféry, což umožňuje plynulé a realistické interakce.
*   **Vizuální vylepšení:**
    *   **Textury:** Použití různých textur pro objekty (např. tráva pro zem, cihly pro stěny) výrazně zlepšuje vizuální kvalitu a pomáhá vnímat 3D prostor.
    *   **Různorodé modely:** Kromě základních kostek a rovin byly použity i jiné vestavěné modely (např. 'sphere', 'cone'), což přidává scéně na rozmanitosti.
    *   **Osvětlení:** Ursina automaticky aplikuje základní osvětlení. V této fázi bylo možné experimentovat s barvami objektů, aby se simulovaly různé světelné podmínky, nebo přidat `DirectionalLight` pro globální osvětlení.
*   **Robustnost:**
    *   **Defenzivní programování:** Kód je navržen tak, aby byl odolný vůči běžným chybám. Například, pokud by se načítala neexistující textura, Ursina obvykle spadne elegantně nebo použije výchozí.
    *   **Komentáře a čitelnost:** Důraz byl kladen na udržení vysoké úrovně komentářů a čitelnosti kódu, což usnadňuje budoucí údržbu a rozšíření.
*   **Další prvky:** Možné přidání jednoduchého UI prvku (např. `Text` pro zobrazení instrukcí) pro zlepšení uživatelského zážitku.