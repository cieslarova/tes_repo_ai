# Název projektu: Správce Inventáře (Inventory Manager)

## Popis a cíl projektu
Projekt "Správce Inventáře" je jednoduchá konzolová aplikace navržená pro efektivní správu seznamu položek s jejich množstvím. Hlavním cílem je poskytnout uživateli intuitivní nástroj pro sledování zásob, který umožňuje přidávat nové položky, aktualizovat množství existujících položek a odebírat je z inventáře. Projekt slouží jako demonstrace základních principů objektově orientovaného programování, práce s datovými strukturami (slovníky) a ošetření uživatelského vstupu.

## Popis funkcionality programu
Program po spuštění zobrazí hlavní menu s následujícími možnostmi:
1.  **Přidat/Aktualizovat položku:** Uživatel zadá název položky a množství. Pokud položka již existuje, její množství se aktualizuje (přičte se zadané množství). Pokud neexistuje, vytvoří se nová položka.
2.  **Odebrat položku:** Uživatel zadá název položky a množství k odebrání. Program ověří, zda položka existuje a zda je dostatečné množství k odebrání. Pokud množství klesne na nulu nebo méně, položka je z inventáře zcela odstraněna.
3.  **Zobrazit inventář:** Vypíše všechny položky aktuálně uložené v inventáři, včetně jejich názvů a množství.
4.  **Ukončit program:** Ukončí aplikaci.

Program je navržen tak, aby byl odolný vůči nesprávnému uživatelskému vstupu (např. zadání textu místo čísla pro množství, pokus o odebrání neexistující položky nebo většího množství, než je k dispozici).

## Technická část
*   **Použité knihovny:** Projekt využívá pouze standardní knihovny Pythonu, konkrétně žádné externí moduly nejsou potřeba.
*   **Algoritmy:**
    *   **Vyhledávání položek:** Pro rychlé vyhledávání a aktualizaci položek je inventář implementován jako slovník (hash mapa), kde klíčem je název položky (string) a hodnotou je objekt třídy `Item`. To umožňuje vyhledávání v průměrném čase O(1).
    *   **Přidávání/Odebírání:** Logika pro přidávání a odebírání položek zahrnuje kontrolu existence klíče ve slovníku a následnou aktualizaci nebo odstranění záznamu.
*   **Vlastní datové struktury:**
    *   **Třída `Item`:** Reprezentuje jednu položku v inventáři s atributy `name` (název, string) a `quantity` (množství, integer).
    *   **Třída `Inventory`:** Spravuje kolekci objektů `Item` pomocí interního slovníku `self.items`. Tato třída zapouzdřuje veškerou logiku pro manipulaci s inventářem.
*   **Ošetření chyb (try/except):**
    *   Program intenzivně využívá bloky `try-except` pro robustní zpracování uživatelského vstupu. Konkrétně se ošetřují chyby typu `ValueError` při pokusu o převod nečíselného vstupu na integer pro množství.
    *   Dále jsou implementovány logické kontroly pro zajištění integrity dat, jako je kontrola existence položky před jejím odebráním nebo ověření dostatečného množství před snížením stavu.