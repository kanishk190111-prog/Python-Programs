class ArtGallery:
    def __init__(self, name):
        self.name = name
        self.artworks = []
        print("Welcome to " + self.name + " Art Gallery!")

    def add_artwork(self, title, artist):
        artwork = title + " by " + artist
        self.artworks.append(artwork)
        print("Added: " + artwork)

    def display_artworks(self):
        print("\n " + self.name + " Collection ")
        if not self.artworks:
            print("No artworks added yet.")
        else:
            count = 1
            for item in self.artworks:
                print(str(count) + ". " + item)
                count += 1

    def __del__(self):
        print("\nClosing " + self.name + " Gallery. Goodbye!")


my_gallery = ArtGallery("ROCKY")

my_gallery.add_artwork("Mona Lisa", "Leonardo da Vinci")
my_gallery.add_artwork("Starry Night", "Vincent van Gogh")

my_gallery.display_artworks()

del my_gallery