import random

# Definice barev pro lepší vizualizaci v konzoli (i když jen textová)
# V reálné grafické hře by to byly RGB hodnoty
COLORS = {
    'I': 'Cyan',
    'O': 'Yellow',
    'T': 'Purple',
    'S': 'Green',
    'Z': 'Red',
    'J': 'Blue',
    'L': 'Orange',
    'EMPTY': 'Black' # Barva pro prázdné pole
}

class Board:
    """
    Třída reprezentující herní desku Tetrisu.
    Spravuje stav hrací plochy, včetně obsazených polí.
    """
    def __init__(self, width, height):
        """
        Inicializuje herní desku s danou šířkou a výškou.
        Deska je reprezentována jako dvourozměrný seznam, kde každá buňka
        obsahuje typ bloku (např. 'I', 'J', 'EMPTY').
        """
        self.width = width
        self.height = height
        # Inicializace prázdné desky. 'EMPTY' značí prázdné pole.
        self.grid = [['EMPTY' for _ in range(width)] for _ in range(height)]
        print(f"Herní deska inicializována: {self.width}x{self.height}")

    def display(self):
        """
        Zobrazí aktuální stav herní desky v konzoli.
        Prozatím zobrazuje jen prázdnou desku.
        """
        print("\n--- Herní deska ---")
        for row in self.grid:
            # Zde by se v budoucnu zobrazovaly tvary tetromino
            print(" ".join(['.' if cell == 'EMPTY' else '#' for cell in row]))
        print("-------------------\n")

class Tetromino:
    """
    Abstraktní základní třída pro všechny tvary tetromino.
    Definuje základní vlastnosti a metody, které budou sdílet všechny typy bloků.
    """
    def __init__(self, shape_type, color, initial_shape):
        """
        Inicializuje tetromino.
        :param shape_type: Typ tvaru (např. 'I', 'J', 'L').
        :param color: Barva tetromino.
        :param initial_shape: Seznam souřadnic reprezentujících tvar v jeho počáteční rotaci.
                              Souřadnice jsou relativní k 'anchor' bodu (0,0).
        """
        self.shape_type = shape_type
        self.color = color
        # Seznam všech možných rotací. Každá rotace je seznam souřadnic bloků.
        self.rotations = [initial_shape]
        self.current_rotation_index = 0
        # Aktuální pozice tetromino na desce (horní levý roh ohraničujícího boxu).
        self.x = 0
        self.y = 0
        print(f"Tetromino typu {self.shape_type} inicializováno.")

    def get_current_shape(self):
        """
        Vrací souřadnice bloků aktuálního tvaru a rotace.
        """
        return self.rotations[self.current_rotation_index]

    def rotate(self):
        """
        Změní rotaci tetromino na další v pořadí.
        Tato metoda bude v dalších fázích rozšířena o logiku rotace.
        """
        # Prozatím jen placeholder, rotace se implementuje později.
        print(f"Tetromino {self.shape_type} bylo otočeno (placeholder).")
        self.current_rotation_index = (self.current_rotation_index + 1) % len(self.rotations)

    def move(self, dx, dy):
        """
        Posune tetromino o dx v horizontálním směru a dy ve vertikálním směru.
        Tato metoda bude v dalších fázích rozšířena o logiku pohybu.
        """
        # Prozatím jen placeholder, pohyb se implementuje později.
        self.x += dx
        self.y += dy
        print(f"Tetromino {self.shape_type} bylo posunuto na ({self.x}, {self.y}) (placeholder).")

# Definice konkrétních tvarů tetromino děděním od základní třídy Tetromino
# Každý tvar má své specifické rotace.

class I_Tetromino(Tetromino):
    def __init__(self):
        # Tvar I:
        # . . . .
        # X X X X
        # . . . .
        # . . . .
        initial_shape = [(0, 1), (1, 1), (2, 1), (3, 1)] # Horizontální
        super().__init__('I', COLORS['I'], initial_shape)
        # Vertikální rotace
        self.rotations.append([(1, 0), (1, 1), (1, 2), (1, 3)])

class J_Tetromino(Tetromino):
    def __init__(self):
        # Tvar J:
        # X . .
        # X X X
        # . . .
        initial_shape = [(0, 0), (0, 1), (1, 1), (2, 1)]
        super().__init__('J', COLORS['J'], initial_shape)
        # Další rotace budou přidány v budoucnu

class L_Tetromino(Tetromino):
    def __init__(self):
        # Tvar L:
        # . . X
        # X X X
        # . . .
        initial_shape = [(2, 0), (0, 1), (1, 1), (2, 1)]
        super().__init__('L', COLORS['L'], initial_shape)
        # Další rotace budou přidány v budoucnu

class O_Tetromino(Tetromino):
    def __init__(self):
        # Tvar O:
        # X X
        # X X
        initial_shape = [(0, 0), (1, 0), (0, 1), (1, 1)]
        super().__init__('O', COLORS['O'], initial_shape)
        # Tvar O má jen jednu rotaci, takže se další nepřidávají

class S_Tetromino(Tetromino):
    def __init__(self):
        # Tvar S:
        # . X X
        # X X .
        # . . .
        initial_shape = [(1, 0), (2, 0), (0, 1), (1, 1)]
        super().__init__('S', COLORS['S'], initial_shape)
        # Další rotace budou přidány v budoucnu

class T_Tetromino(Tetromino):
    def __init__(self):
        # Tvar T:
        # . X .
        # X X X
        # . . .
        initial_shape = [(1, 0), (0, 1), (1, 1), (2, 1)]
        super().__init__('T', COLORS['T'], initial_shape)
        # Další rotace budou přidány v budoucnu

class Z_Tetromino(Tetromino):
    def __init__(self):
        # Tvar Z:
        # X X .
        # . X X
        # . . .
        initial_shape = [(0, 0), (1, 0), (1, 1), (2, 1)]
        super().__init__('Z', COLORS['Z'], initial_shape)
        # Další rotace budou přidány v budoucnu

class Game:
    """
    Hlavní třída pro správu hry Tetris.
    Obsahuje herní desku, aktuální tetromino a hlavní herní smyčku.
    """
    def __init__(self, width=10, height=20):
        """
        Inicializuje hru Tetris.
        :param width: Šířka herní desky.
        :param height: Výška herní desky.
        """
        self.board = Board(width, height)
        self.current_tetromino = None
        self.game_over = False
        print("Hra Tetris inicializována.")

    def spawn_tetromino(self):
        """
        Vytvoří nové náhodné tetromino a umístí ho na začátek desky.
        """
        tetromino_types = [I_Tetromino, J_Tetromino, L_Tetromino, O_Tetromino, S_Tetromino, T_Tetromino, Z_Tetromino]
        self.current_tetromino = random.choice(tetromino_types)()
        # Nastavení počáteční pozice (např. uprostřed nahoře)
        self.current_tetromino.x = self.board.width // 2 - len(self.current_tetromino.get_current_shape()) // 2
        self.current_tetromino.y = 0
        print(f"Nové tetromino typu {self.current_tetromino.shape_type} bylo vytvořeno.")

    def run(self):
        """
        Hlavní herní smyčka.
        Prozatím jen inicializuje desku a vytvoří jedno tetromino.
        """
        self.spawn_tetromino()
        self.board.display() # Zobrazí prázdnou desku
        print("Hra běží (prozatím jen základní inicializace).")
        # Zde by v budoucnu probíhala hlavní herní smyčka s uživatelským vstupem,
        # pohybem bloků, detekcí kolizí a odstraňováním řádků.

# Příklad použití pro ověření základní struktury
if __name__ == "__main__":
    game = Game()
    game.run()
