class Song:
    def __init__(self, title, artist, genre, duration="0.00"):
        self.title = title
        self.artist = artist
        self.genre = genre
        self.duration = duration

    def __repr__(self):
        return f"{self.title} - {self.artist} ({self.genre}, {self.duration})"


SONGS = [
    Song("Love song", "Zak Abel", "Pop", "3.23"),
    Song("Kombucha Burps", "Kendrick Lamar", "Hip Hop", "5:36"),
    Song("On The Regular", "Avicii ft. Derulo", "EDM", "2:39"),
    Song("El Sambroso", "Kaytranada", "Funk", "3:26"),
    Song("Mask Off Soul Flip", "ESTA", "Soul", "6:29"),
    Song("Tokyo Nights", "Dragonette", "Pop", "4:15"),
]

FAVORITES = []

def add_favorite(song):
    if song in FAVORITES:
        print(f"'{song.title}' is already in your favorites.")
    else:
        FAVORITES.append(song)
        print(f"'{song.title}' has been added to your favorites.")


def remove_favorite(song):
    if song in FAVORITES:
        FAVORITES.remove(song)
        print(f"'{song.title}' has been removed from your favorites.")
    else:
        print(f"'{song.title}' is not in your favorites.")

def show_favorites():
    if not FAVORITES:
        print("Your favorites list is empty.")
    else:
        print("Your favorites:")
        for song in FAVORITES:
            print(f" - {song}")
            