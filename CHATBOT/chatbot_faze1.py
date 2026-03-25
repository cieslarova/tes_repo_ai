# chatbot_faze1.py

"""
Fáze 1: Základní kostra chatbota a inicializace konverzace.
Tento skript definuje základní třídy pro chatbota a uživatele a inicializuje první pozdrav.
"""

class Chatbot:
    """
    Třída reprezentující chatbota.
    Stará se o úvodní pozdrav a budoucí generování odpovědí.
    """
    def __init__(self, name="Asistent"):
        """
        Konstruktor třídy Chatbot.
        Inicializuje jméno chatbota.

        Args:
            name (str): Jméno chatbota. Výchozí je "Asistent".
        """
        self.name = name
        # V této fázi ještě nejsou potřeba složitější stavy nebo paměť.
        # Tyto atributy budou přidány v pozdějších fázích.
        print(f"Chatbot '{self.name}' byl inicializován.") # Kontrolní výpis pro vývoj.

    def greet(self):
        """
        Metoda pro pozdravení uživatele.
        Vypíše úvodní zprávu od chatbota.
        """
        print(f"\n{self.name}: Ahoj! Jsem {self.name}. Jak ti mohu pomoci?")


class User:
    """
    Třída reprezentující uživatele.
    Stará se o získávání vstupu od uživatele.
    """
    def __init__(self, name="Uživatel"):
        """
        Konstruktor třídy User.
        Inicializuje jméno uživatele.

        Args:
            name (str): Jméno uživatele. Výchozí je "Uživatel".
        """
        self.name = name
        print(f"Uživatel '{self.name}' byl inicializován.") # Kontrolní výpis pro vývoj.

    def get_input(self):
        """
        Metoda pro získání textového vstupu od uživatele.
        Vyzve uživatele k zadání textu a vrátí ho.

        Returns:
            str: Text zadaný uživatelem.
        """
        # Zde se získává vstup od uživatele.
        # V budoucnu zde může být přidána validace vstupu.
        user_input = input(f"{self.name}: ")
        return user_input


def main():
    """
    Hlavní funkce programu, která inicializuje chatbota a uživatele
    a spouští základní konverzační smyčku.
    """
    print("Spouštění chatbota...")
    # Vytvoření instance chatbota a uživatele.
    my_chatbot = Chatbot()
    my_user = User()

    # Chatbot pozdraví uživatele.
    my_chatbot.greet()

    # Základní konverzační smyčka.
    # V této fázi pouze přijímá vstup, ale nezpracovává ho komplexně.
    # Uživatel může zadávat text, dokud nezadá 'konec'.
    while True:
        user_message = my_user.get_input()
        if user_message.lower() == 'konec':
            print(f"{my_chatbot.name}: Nashledanou!")
            break
        # V této fázi chatbot zatím na zprávy neodpovídá, pouze je přijímá.
        # Logika odpovědí bude přidána v další fázi.
        print(f"{my_chatbot.name}: Děkuji za zprávu '{user_message}'.") # Potvrzení přijetí zprávy.


if __name__ == "__main__":
    # Zajišťuje, že main() se spustí pouze při přímém spuštění skriptu.
    main()
