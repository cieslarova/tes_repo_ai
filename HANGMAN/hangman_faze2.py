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
        self.slova = ["PYTHON", "PROGRAMOVANI", "ALGORITMUS", "POCITAC", "VYVOJ", "KLAVESNICE", "MONITOR", "PROCESOR"]
        
        # Slovo, které má hráč uhodnout. Bude vybráno z 'self.slova'.
        self.tajene_slovo = ""
        
        # Množina písmen, která již hráč uhodl správně nebo špatně.
        # Použití množiny zajišťuje rychlou kontrolu a zamezuje duplicitám.
        self.hadana_pismena = set()
        
        # Počet chybných pokusů, které hráč již provedl.
        self.chybne_pokusy = 0
        
        # Maximální počet chybných pokusů, než hráč prohraje.
        self.max_chybne_pokusy = 7 # Standardní počet částí šibenice

        # print("Hra Šibenice inicializována. Připraveno k výběru slova a spuštění.") # Odstraněno pro čistší výstup

    def _vyber_slovo(self):
        """
        Vybere náhodné slovo ze seznamu 'self.slova' a uloží ho jako 'self.tajene_slovo'.
        Všechna slova jsou převedena na velká písmena pro konzistenci.
        """
        self.tajene_slovo = random.choice(self.slova).upper()
        # print(f"Slovo bylo vybráno: {self.tajene_slovo} (pro účely ladění, v reálné hře se nezobrazuje)") # Odstraněno pro reálnou hru

    def _zobraz_stav_hry(self):
        """
        Zobrazí aktuální stav hry hráči.
        Zahrnuje zobrazení uhodnutých písmen ve slově a zbývajících pokusů.
        """
        # Vytvoří zobrazení slova, kde uhodnutá písmena jsou viditelná a neuhodnutá jsou podtržítka.
        zobrazene_slovo = " ".join([p if p in self.hadana_pismena else "_" for p in self.tajene_slovo])
        print("\n" + "="*30)
        print(f"Slovo: {zobrazene_slovo}")
        # Zobrazí již uhodnutá písmena seřazená abecedně pro lepší přehlednost.
        print(f"Uhodnutá písmena: {', '.join(sorted(list(self.hadana_pismena)))}")
        print(f"Zbývající pokusy: {self.max_chybne_pokusy - self.chybne_pokusy}")
        print("="*30)

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
        return all(p in self.hadana_pismena for p in self.tajene_slovo)

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
        a kontroly konce hry.
        """
        print("Vítejte ve hře Šibenice!")
        self._vyber_slovo() # Vybere slovo pro aktuální hru
        
        # Hlavní smyčka hry, která běží, dokud není dosaženo stavu výhry nebo prohry.
        while not self._je_vyhra() and not self._je_prohra():
            self._zobraz_stav_hry() # Zobrazí aktuální stav hry
            
            hadani = input("Zadejte písmeno: ").strip() # Získá vstup od hráče
            
            # Základní validace vstupu: musí být jedno písmeno abecedy.
            if len(hadani) == 1 and hadani.isalpha():
                self._zpracuj_hadani(hadani)
            else:
                print("Neplatný vstup. Zadejte prosím jedno písmeno abecedy.")
            
        # Po ukončení smyčky vypíše výsledek hry.
        self._zobraz_stav_hry() # Zobrazí finální stav
        if self._je_vyhra():
            print(f"\nGratulujeme! Uhodli jste slovo '{self.tajene_slovo}'!")
        else:
            print(f"\nProhráli jste! Tajné slovo bylo '{self.tajene_slovo}'.")
            print("Více pokusů nemáte. Zkuste to znovu!")

# Příklad spuštění hry (pro testování)
if __name__ == "__main__":
    hra = HangmanGame()
    hra.hraj()
