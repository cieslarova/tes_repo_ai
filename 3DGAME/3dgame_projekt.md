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