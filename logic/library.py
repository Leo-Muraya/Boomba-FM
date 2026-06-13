class Song:
    def __init__(self, title,artist, genre, duration = "0.00"):
        self.title = title
        self.artist = artist
        self.genre = genre
        self.duration = duration



SONGS = [
    Song("Love song", "Zak Abel", "Pop", "3.23"),
    Song("Kombucha Burps", "Kendrick Lamar", "Hip Hop", "5:36"),
    Song("On The Regular", "Avicii ft. Derulo", "EDM", "2:39"),
    Song("El Sambroso", "Kaytranada", "Funk", "3:26"),
    Song("Mask Off Soul Flip", "ESTA", "Soul", "6:29"),
    Song("Tokyo Nights", "Dragonette", "Pop", "4:15"),
]
