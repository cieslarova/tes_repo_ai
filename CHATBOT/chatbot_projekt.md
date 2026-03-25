# Dokumentace projektu: CHATBOT

## Název projektu
CHATBOT

## Popis a cíl projektu
Cílem projektu je vytvořit jednoduchého textového chatbota, který dokáže vést základní konverzaci s uživatelem. Projekt slouží jako ukázka objektově orientovaného programování v Pythonu a práce s uživatelským vstupem. Zaměřuje se na systematický vývoj softwaru v několika fázích, s důrazem na čitelnost kódu, komentáře a dokumentaci.

## Popis funkcionality programu (Fáze 1)
V první fázi je chatbot schopen pozdravit uživatele a inicializovat konverzační smyčku. Program po spuštění vytvoří instanci třídy `Chatbot` a `User`. Chatbot automaticky pozdraví uživatele úvodní zprávou a vyzve ho k prvnímu vstupu. Uživatel může zadat text, který je následně zachycen, ale v této fázi ještě není komplexně zpracováván. Jedná se o základní kostru pro budoucí rozšíření.

## Technická část (Fáze 1)
*   **Použité knihovny:** Standardní knihovny Pythonu.
*   **Algoritmy:** Základní zpracování textového vstupu pomocí funkce `input()`.
*   **Vlastní datové struktury:**
    *   **Třída `Chatbot`:** Reprezentuje samotného chatbota. Obsahuje metodu `greet()` pro úvodní pozdrav.
    *   **Třída `User`:** Reprezentuje uživatele. Obsahuje metodu `get_input()` pro získání vstupu od uživatele.
*   **Volání externího API:** Žádné externí API není v této fázi použito.