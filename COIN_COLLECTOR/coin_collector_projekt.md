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