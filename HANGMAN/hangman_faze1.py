import random

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
        # Tato slova jsou základem pro každou novou hru.
        self.slova = ["PYTHON", "PROGRAMOVANI", "ALGORITMUS", "POCITAC", "VYVOJ"]
        
        # Slovo, které má hráč uhodnout. Bude vybráno z 'self.slova'.
        self.tajene_slovo = ""
        
        # Množina písmen, která již hráč uhodl správně nebo špatně.
        # Použití množiny zajišťuje rychlou kontrolu a zamezuje duplicitám.
        self.hadana_pismena = set()
        
        # Počet chybných pokusů, které hráč již provedl.
        self.chybne_pokusy = 0
        
        # Maximální počet chybných pokusů, než hráč prohraje.
        self.max_chybne_pokusy = 7 # Standardní počet částí šibenice

        print("Hra Šibenice inicializována. Připraveno k výběru slova a spuštění.")

    def _vyber_slovo(self):
        """
        Vybere náhodné slovo ze seznamu 'self.slova' a uloží ho jako 'self.tajene_slovo'.
        Tato metoda je interní a slouží k nastavení tajenky pro novou hru.
        """
        # Prozatím jen placeholder, skutečná logika výběru bude přidána později.
        self.tajene_slovo = random.choice(self.slova)
        print(f"Slovo bylo vybráno: {self.tajene_slovo} (pro účely ladění, v reálné hře se nezobrazuje)")

    def _zobraz_stav_hry(self):
        """
        Zobrazí aktuální stav hry hráči.
        Zahrnuje zobrazení uhodnutých písmen ve slově a zbývajících pokusů.
        """
        # Prozatím jen placeholder, vizuální reprezentace bude přidána později.
        zobrazene_slovo = "".join([p if p in self.hadana_pismena else "_" for p in self.tajene_slovo])
        print(f"Aktuální slovo: {zobrazene_slovo}")
        print(f"Uhodnutá písmena: {', '.join(sorted(list(self.hadana_pismena)))}")
        print(f"Zbývající pokusy: {self.max_chybne_pokusy - self.chybne_pokusy}")

    def _zpracuj_hadani(self, pismeno):
        """
        Zpracuje jedno písmeno uhodnuté hráčem.
        Přidá písmeno do sady uhodnutých písmen a aktualizuje počet chybných pokusů.
        """
        # Prozatím jen placeholder, skutečná logika zpracování bude přidána později.
        pismeno = pismeno.upper() # Převod na velká písmena pro konzistenci
        if pismeno in self.hadana_pismena:
            print(f"Písmeno '{pismeno}' již bylo uhodnuto.")
            return
        
        self.hadana_pismena.add(pismeno)
        if pismeno not in self.tajene_slovo:
            self.chybne_pokusy += 1
            print(f"Písmeno '{pismeno}' není ve slově. Chybných pokusů: {self.chybne_pokusy}")
        else:
            print(f"Písmeno '{pismeno}' je ve slově!")

    def hraj(self):
        """
        Hlavní herní smyčka.
        Řídí průběh hry od začátku do konce.
        """
        print("Vítejte ve hře Šibenice!")
        self._vyber_slovo() # Vybere slovo pro hru
        
        # Hlavní smyčka hry, která poběží, dokud hra neskončí (výhra/prohra).
        while True:
            self._zobraz_stav_hry() # Zobrazí aktuální stav
            hadani = input("Zadejte písmeno: ").strip() # Získá vstup od hráče
            
            # Prozatím velmi jednoduchá kontrola vstupu, bude vylepšena.
            if len(hadani) == 1 and hadani.isalpha():
                self._zpracuj_hadani(hadani)
            else:
                print("Neplatný vstup. Zadejte prosím jedno písmeno.")
            
            # Kontrola konce hry (výhra nebo prohra) bude přidána později.
            if self.chybne_pokusy >= self.max_chybne_pokusy:
                print("Prohráli jste! Více pokusů nemáte.")
                break
            # Kontrola výhry (pokud jsou všechna písmena uhodnuta)
            if all(p in self.hadana_pismena for p in self.tajene_slovo):
                print("Gratulujeme! Slovo bylo uhodnuto.")
                break

# Příklad spuštění hry (pro testování)
if __name__ == "__main__":
    hra = HangmanGame()
    hra.hraj()
