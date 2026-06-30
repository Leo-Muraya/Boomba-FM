class Song:
    def __init__(self, title,artist, genre, duration = "0.00", file_path = ""):
        self.title = title
        self.artist = artist
        self.genre = genre
        self.duration = duration
        self.file_path = file_path


SONGS = [
    Song("Devil In A New Dress", 
         "Kanye West",
         "Pop",
         "5.51", 
         "assets/songs/Devil In A New Dress - Kanye West.mp3"),
    
    
    Song("Champion", 
         "Kanye West", 
         "pop", 
         "2.47",
         "assets/songs/Champion.mp3"),
    
    Song("Good Morning", 
         "Kanye West", 
         "Pop", 
         "3,15", 
         "assets/songs/Good Morning.mp3"),
    
    Song("Family Businness", 
         "Kanye West", 
         "Pop", 
         "4.38", 
         "assets/songs/20.Family Business.mp3"),
    
    Song("All Falls Down", 
         "Kanye West", 
         "Pop", 
         "3.43", 
         "assets/songs/04.All Falls Down (Ft. Syleena Johnson).mp3"),
    
    Song("Through The Wire", 
         "Kanye West", 
         "Pop", 
         "3.41", 
         "assets/songs/19.Through The Wire.mp3"),
    
    Song("Slow Jamz", 
         "Kanye West", 
         "Pop", 
         "5.16", 
         "assets/songs/12.Slow Jamz (Ft. Twista & Jamie Foxx).mp3")
]


