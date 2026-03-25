# Projekt: Šibenice

## Název projektu
Šibenice

## Popis a cíl projektu
Cílem projektu je vytvořit jednoduchou textovou hru Šibenice (Hangman), kde hráč hádá slovo písmeno po písmenu. Hra bude spuštěna v konzoli a bude poskytovat zpětnou vazbu o správnosti hádaných písmen a zbývajících pokusech. Hráč má omezený počet pokusů na uhodnutí celého slova. Projekt je navržen tak, aby demonstroval postupné budování softwaru s důrazem na modularitu a čitelnost kódu.

## Popis funkcionality programu (Fáze 1)
V první fázi je vytvořena základní struktura hry. Definuje se třída `HangmanGame`, která bude spravovat stav hry. Tato třída v sobě zapouzdří klíčové informace, jako je hádané slovo, počet zbývajících pokusů a seznam již hádaných písmen. Kód obsahuje inicializaci těchto základních prvků a záchytné body (prázdné metody) pro budoucí implementaci herní logiky, jako je zpracování hádání písmen, kontrola výhry/prohry a zobrazení aktuálního stavu hry. Tato fáze se soustředí na vytvoření robustního základu pro další rozvoj.

## Technická část (Fáze 1)
*   **Použité knihovny:** V této fázi nejsou použity žádné externí knihovny. Vše je implementováno pomocí standardních funkcí Pythonu.
*   **Algoritmy:** Základní inicializace proměnných a definice struktury třídy. Žádné složité algoritmy nejsou zatím implementovány.
*   **Vlastní datové struktury:**
    *   Třída `HangmanGame`: Slouží k zapouzdření veškerého herního stavu a logiky. Obsahuje atributy pro hádané slovo (`word_to_guess`), aktuální stav hádaného slova (`guessed_word_display`), zbývající pokusy (`attempts_left`) a seznam již hádaných písmen (`guessed_letters`).
*   **Volání externího API:** Není použito.
*   **Ošetření chyb:** V této fázi není implementováno žádné specifické ošetření chyb, jelikož se jedná pouze o rámec.