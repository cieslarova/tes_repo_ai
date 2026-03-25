# sibenice.py - Fáze 1: Základní kostra hry Šibenice

import random # Bude použito v pozdějších fázích pro výběr slova

class HangmanGame:
    """
    Třída reprezentující hru Šibenice.
    Spravuje stav hry, jako je hádané slovo, zbývající pokusy a hádaná písmena.
    """

    def __init__(self, word):
        """
        Inicializuje novou instanci hry Šibenice.

        Args:
            word (str): Slovo, které se má hádat. Bude převedeno na velká písmena
                        pro zjednodušení porovnávání.
        """
        self.word_to_guess = word.upper() # Slovo převedené na velká písmena
        self.guessed_letters = []         # Seznam písmen, která již byla uhodnuta
        self.attempts_left = 6            # Počet zbývajících pokusů (standardně 6 pro šibenici)
        # Vytvoříme zobrazení slova s podtržítky pro neuhodnutá písmena
        self.guessed_word_display = ["_" for _ in self.word_to_guess]

        # Zde by mohla být inicializace dalších herních prvků, např. grafiky šibenice.
        print(f"Hra Šibenice inicializována se slovem: {self.word_to_guess}")
        print(f"Aktuální stav: {' '.join(self.guessed_word_display)}")
        print(f"Zbývá pokusů: {self.attempts_left}")

    def display_game_state(self):
        """
        Zobrazí aktuální stav hry hráči.
        Tato metoda bude v budoucnu rozšířena o vizuální prvky.
        """
        print("\n--- AKTUÁLNÍ STAV HRY ---")
        print(f"Slovo: {' '.join(self.guessed_word_display)}")
        print(f"Již hádaná písmena: {', '.join(sorted(self.guessed_letters))}")
        print(f"Zbývá pokusů: {self.attempts_left}")
        print("-------------------------")

    def guess_letter(self, letter):
        """
        Zpracuje hádání písmena od hráče.
        Tato metoda bude obsahovat logiku pro kontrolu písmena a aktualizaci stavu hry.
        """
        # Zde bude implementována logika pro kontrolu písmena
        pass # Zástupný symbol pro budoucí implementaci

    def check_win(self):
        """
        Zkontroluje, zda hráč uhodl celé slovo a vyhrál.
        """
        # Zde bude implementována logika pro kontrolu výhry
        return False # Zástupný symbol

    def check_loss(self):
        """
        Zkontroluje, zda hráči došly pokusy a prohrál.
        """
        # Zde bude implementována logika pro kontrolu prohry
        return False # Zástupný symbol

    def play_game(self):
        """
        Hlavní herní smyčka.
        """
        # Zde bude implementována hlavní herní smyčka
        print("Hra začíná...")
        self.display_game_state()
        print("Zatím žádná herní logika, pouze inicializace.")
        print("Konec fáze 1.")

# Příklad použití (pouze pro demonstraci inicializace v Fázi 1)
if __name__ == "__main__":
    # V této fázi je slovo pevně dané, v budoucnu bude vybíráno náhodně.
    game = HangmanGame("PYTHON")
    game.play_game()
