from abc import ABC, abstractmethod

# 1. Parent Class (Abstract Class)
class Instrument(ABC):
    def __init__(self, name):
        self.name = name  # Store the instrument name

    # Abstract method that subclasses MUST implement
    @abstractmethod
    def make_sound(self):
        pass


# 2. Child Class for Guitar
class Guitar(Instrument):
    def __init__(self, name, strings):
        # Call the parent class constructor using super()
        super().__init__(name)
        self.strings = strings

    # Override the abstract method
    def make_sound(self):
        print(f" The {self.name} with {self.strings} strings goes: Strum! Strum! Pluck!")


# 3. Child Class for Piano
class Piano(Instrument):
    def __init__(self, name, keys):
        # Call the parent class constructor using super()
        super().__init__(name)
        self.keys = keys

    # Override the abstract method
    def make_sound(self):
        print(f" The {self.name} with {self.keys} keys goes: Plink! Plonk! Ting!")


# 4. Child Class for Drum
class Drum(Instrument):
    def __init__(self, name, drum_type):
        super().__init__(name)
        self.drum_type = drum_type

    def make_sound(self):
        print(f" The {self.drum_type} {self.name} goes: Boom! Badum-Tss!")


# --- MAIN PROGRAM (Showtime!) ---

# Creating objects (instances) of different instruments
guitar1 = Guitar("Acoustic Guitar", 6)
piano1 = Piano("Grand Piano", 88)
drum1 = Drum("Snare Drum", "Side")

# Store instruments in a list to run the sound show
show_instruments = [guitar1, piano1, drum1]

print("===  Welcome to the Music Instrument Sound Show!  ===\n")

for instrument in show_instruments:
    instrument.make_sound()  # Each instrument plays its own unique sound