import random
import os # Pro případné vyčištění konzole, ale v této verzi se mu vyhýbáme pro multiplatformní kompatibilitu

class HangmanGame:
    """
    Třída reprezentující hru Šibenice.
    Zapouzdřuje veškerou logiku a stav hry.
    """

    def __init__(self):
        """
        Inicializuje novou instanci hry Šibenice.
        Nastavuje počáteční parametry hry, jako je seznam slov,
        maximální počet pokusů a prázdné sady pro sledování uhodnutých písmen.
        """
        # Seznam slov, ze kterých bude hra vybírat.
        # Slova jsou předem převedena na velká písmena pro zjednodušení logiky.
        self.slova = ["PYTHON", "PROGRAMOVANI", "ALGORITMUS", "POCITAC", "VYVOJ", 
                      "KLAVESNICE", "MONITOR", "PROCESOR", "SOFTWARE", "HARDWARE",
                      "FUNKCE", "TRIDA", "OBJEKT", "MODUL"]
        
        # Slovo, které má hráč uhodnout. Bude vybráno z 'self.slova'.
        self.tajene_slovo = ""
        
        # Množina písmen, která již hráč uhodl správně nebo špatně.
        # Použití množiny zajišťuje rychlou kontrolu a zamezuje duplicitám.
        self.hadana_pismena = set()
        
        # Počet chybných pokusů, které hráč již provedl.
        self.chybne_pokusy = 0
        
        # Maximální počet chybných pokusů, než hráč prohraje.
        self.max_chybne_pokusy = 7 # Standardní počet částí šibenice (0-7)

        # Textová reprezentace šibenice pro různé stavy chybných pokusů.
        # Každý index odpovídá počtu chybných pokusů.
        self.hangman_stages = [
            """
   -----
   |   |
       |
       |
       |
       |
  -------
            """,
            """
   -----
   |   |
   O   |
       |
       |
       |
  -------
            """,
            """
   -----
   |   |
   O   |
   |   |
       |
       |
  -------
            """,
            """
   -----
   |   |
   O   |
  /|   |
       |
       |
  -------
            """,
            """
   -----
   |   |
   O   |
  /|\\  |
       |
       |
  -------
            """,
            """
   -----
   |   |
   O   |
  /|\\  |
  /    |
       |
  -------
            """,
            """
   -----
   |   |
   O   |
  /|\\  |
  / \\  |
       |
  -------
            """,
            """
   -----
   |   |
   O   |
  /|\\  |
  / \\  |
  / \\  |  <-- Poslední pokus, prohra!
  -------
            """
        ]

    def reset_hry(self):
        """
        Resetuje stav hry pro novou partii.
        Vynuluje uhodnutá písmena, chybné pokusy a vybere nové slovo.
        """
        self.tajene_slovo = ""
        self.hadana_pismena = set()
        self.chybne_pokusy = 0
        self._vyber_slovo() # Vybere nové slovo pro novou hru

    def _vyber_slovo(self):
        """
        Vybere náhodné slovo ze seznamu 'self.slova' a uloží ho jako 'self.tajene_slovo'.
        """
        self.tajene_slovo = random.choice(self.slova)

    def _zobraz_stav_hry(self):
        """
        Zobrazí aktuální stav hry hráči.
        Zahrnuje zobrazení uhodnutých písmen ve slově, zbývajících pokusů a vizuální šibenici.
        """
        # os.system('cls' if os.name == 'nt' else 'clear') # Vyčištění konzole (volitelné, pro lepší UX)
        
        print("\n" + "="*40)
        # Zobrazí aktuální stav šibenice podle počtu chybných pokusů.
        # Index je omezen na maximální počet pokusů, aby nedošlo k chybě indexu.
        print(self.hangman_stages[min(self.chybne_pokusy, len(self.hangman_stages) - 1)])
        
        # Vytvoří zobrazení slova, kde uhodnutá písmena jsou viditelná a neuhodnutá jsou podtržítka.
        zobrazene_slovo = " ".join([p if p in self.hadana_pismena else "_" for p in self.tajene_slovo])
        print(f"Slovo: {zobrazene_slovo}")
        
        # Zobrazí již uhodnutá písmena seřazená abecedně pro lepší přehlednost.
        print(f"Uhodnutá písmena: {', '.join(sorted(list(self.hadana_pismena)))}")
        print(f"Zbývající pokusy: {self.max_chybne_pokusy - self.chybne_pokusy}")
        print("="*40)

    def _zpracuj_hadani(self, pismeno):
        """
        Zpracuje jedno písmeno uhodnuté hráčem.
        Přidá písmeno do sady uhodnutých písmen a aktualizuje počet chybných pokusů.
        """
        pismeno = pismeno.upper() # Převod na velká písmena pro konzistenci
        
        # Kontrola, zda písmeno již bylo uhodnuto.
        if pismeno in self.hadana_pismena:
            print(f"Písmeno '{pismeno}' již bylo uhodnuto. Zkuste jiné.")
            return False # Indikuje, že hádání nebylo nové a neovlivnilo stav hry
        
        # Přidání písmena do sady uhodnutých písmen.
        self.hadana_pismena.add(pismeno)
        
        # Kontrola, zda je písmeno ve slově.
        if pismeno not in self.tajene_slovo:
            self.chybne_pokusy += 1
            print(f"Písmeno '{pismeno}' není ve slově. Ztrácíte pokus!")
        else:
            print(f"Písmeno '{pismeno}' je ve slově! Dobrá práce.")
        return True # Indikuje, že hádání bylo zpracováno

    def _je_vyhra(self):
        """
        Kontroluje, zda hráč uhodl celé slovo.
        Vrací True, pokud jsou všechna písmena tajeného slova obsažena v 'hadana_pismena', jinak False.
        """
        # Kontroluje, zda každé unikátní písmeno v tajeném slově je obsaženo v uhodnutých písmenech.
        return all(p in self.hadana_pismena for p in set(self.tajene_slovo))

    def _je_prohra(self):
        """
        Kontroluje, zda hráč vyčerpal všechny pokusy.
        Vrací True, pokud 'chybne_pokusy' dosáhly 'max_chybne_pokusy', jinak False.
        """
        return self.chybne_pokusy >= self.max_chybne_pokusy

    def hraj(self):
        """
        Hlavní herní smyčka.
        Řídí průběh hry od začátku do konce, včetně výběru slova, zpracování hádání
        a kontroly konce hry. Nabízí možnost hrát znovu.
        """
        print("Vítejte ve hře Šibenice!")
        
        pokracovat_ve_hre = True
        while pokracovat_ve_hre:
            self.reset_hry() # Nastaví novou hru
            
            # Hlavní smyčka hry, která běží, dokud není dosaženo stavu výhry nebo prohry.
            while not self._je_vyhra() and not self._je_prohra():
                self._zobraz_stav_hry() # Zobrazí aktuální stav hry
                
                hadani = input("Zadejte písmeno: ").strip() # Získá vstup od hráče
                
                # Robustní validace vstupu: musí být jedno písmeno abecedy.
                if len(hadani) == 1 and hadani.isalpha():
                    self._zpracuj_hadani(hadani)
                else:
                    print("Neplatný vstup. Zadejte prosím jedno písmeno abecedy.")
                
            # Po ukončení smyčky vypíše výsledek hry.
            self._zobraz_stav_hry() # Zobrazí finální stav s uhodnutým slovem nebo šibenicí
            if self._je_vyhra():
                print(f"\nGratulujeme! Uhodli jste slovo '{self.tajene_slovo}'!")
            else:
                print(f"\nProhráli jste! Tajné slovo bylo '{self.tajene_slovo}'.")
                print("Více pokusů nemáte. Zkuste to znovu!")

            # Nabídka hrát znovu
            while True:
                volba = input("Chcete hrát znovu? (ano/ne): ").strip().lower()
                if volba == "ano":
                    break # Opustí vnitřní smyčku a začne novou hru
                elif volba == "ne":
                    pokracovat_ve_hre = False
                    break # Opustí vnitřní smyčku a ukončí hlavní herní smyčku
                else:
                    print("Neplatná volba. Zadejte 'ano' nebo 'ne'.")

        print("Děkujeme za hru! Na shledanou.")

# Spuštění hry
if __name__ == "__main__":
    hra = HangmanGame()
    hra.hraj()
