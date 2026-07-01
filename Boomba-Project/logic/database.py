class Song:
    def __init__(self, title, artist, genre, duration="0.00", file_path=""):
        self.title = title
        self.artist = artist
        self.genre = genre
        self.duration = duration
        self.file_path = file_path


SONGS = [
    Song("Nzaza",
         "Asake",
         "Afrobeats",
         "3:03",
         "/logic/new resource/Asake - Nzaza (Official Visualizer).mp3"),
    
    Song("Blackbirds",
         "Lancey Foux",
         "Hip Hop",
         "3:12",
         "/logic/new resource/Blackbirds.mp3"),
    
    Song("Face The Flame",
         "Yeat ft. YoungBoy Never Broke Again & Grimes",
         "Hip Hop",
         "2:50",
         "/logic/new resource/Face The Flamë (feat. YoungBoy Never Broke Again & Grimes).mp3"),
    
    Song("Ensalada",
         "Freddie Gibbs & The Alchemist ft. Anderson .Paak",
         "Hip Hop",
         "3:20",
         "/logic/new resource/Freddie Gibbs & The Alchemist - Ensalada (feat. Anderson .Paak) (Official Visualizer).mp3"),
    
    Song("Good Flirts",
         "Baby Keem ft. Kendrick Lamar & Momo Boyd",
         "Hip Hop",
         "3:40",
         "/logic/new resource/Baby Keem - Good Flirts (Official Video) ft. Kendrick Lamar, Momo Boyd.mp3"),
    
    Song("Bazooka",
         "Miami XO",
         "Hip Hop",
         "2:15",
         "/logic/new resource/Miami XO - Bazooka [p.slxwly].mp3"),
    
    Song("You're the Best",
         "Joe Esposito",
         "Rock",
         "2:59",
         "/logic/new resource/You're The Best.mp3"),
    
    Song("Chicago",
         "Michael Jackson",
         "Pop",
         "4:05",
         "/logic/new resource/Michael Jackson - Chicago (Official Audio).mp3"),
    
    Song("One Dance",
         "Drake ft. Wizkid & Kyla",
         "Afrobeats",
         "2:54",
         "/logic/new resource/Drake - One Dance (Lyrics) ft. Wizkid & Kyla.mp3"),
    
    Song("Ex-Factor",
         "Lauryn Hill",
         "R&B",
         "5:26",
         "/logic/new resource/Lauryn Hill - Ex-Factor (Video).mp3"),
    
    Song("Fountains",
         "Drake ft. Tems",
         "Afrobeats",
         "3:12",
         "/logic/new resource/Drake - Fountains (Audio) ft. Tems.mp3"),
    
    Song("Glamorous",
         "Fergie ft. Ludacris",
         "Pop",
         "4:03",
         "/logic/new resource/Fergie - Glamorous ft. Ludacris.mp3"),
    
    Song("Gin and Juice",
         "Snoop Dogg",
         "Hip Hop",
         "3:31",
         "/logic/new resource/Snoop Dogg - Gin And Juice.mp3"),
    
    Song("Hips Don't Lie",
         "Shakira ft. Wyclef Jean",
         "Pop",
         "3:38",
         "/logic/new resource/Shakira - Hips Don't Lie (featuring Wyclef Jean) (Official 4K Video) ft. Wyclef Jean.mp3"),
    
    Song("Get Lucky",
         "Daft Punk ft. Pharrell Williams & Nile Rodgers",
         "Pop",
         "4:08",
         "/logic/new resource/Daft Punk - Get Lucky (Official Audio) ft. Pharrell Williams, Nile Rodgers.mp3"),
    
    Song("No One",
         "Alicia Keys",
         "R&B",
         "4:13",
         "/logic/new resource/Alicia Keys - No One (Official Music Video).mp3"),
    
    Song("Sky",
         "Playboi Carti",
         "Hip Hop",
         "2:48",
         "/logic/new resource/Playboi Carti - Sky (Official Audio).mp3"),
    
    Song("Last Friday Night (T.G.I.F.)",
         "Katy Perry",
         "Pop",
         "3:50",
         "/logic/new resource/Katy Perry - Last Friday Night (T.G.I.F.) [Lyrics].mp3"),
    
    Song("Umbrella",
         "Rihanna ft. JAY-Z",
         "Pop",
         "4:35",
         "/logic/new resource/Rihanna - Umbrella (Orange Version) (Official Music Video) ft. JAY-Z.mp3"),
    
    Song("Waterfalls",
         "TLC",
         "R&B",
         "4:39",
         "/logic/new resource/TLC - Waterfalls (Official HD Video).mp3"),
    
    Song("Magnolia",
         "Playboi Carti",
         "Hip Hop",
         "3:01",
         "/logic/new resource/Playboi Carti - Magnolia (Official Video).mp3"),
    
    Song("Firework",
         "Katy Perry",
         "Pop",
         "3:50",
         "/logic/new resource/Katy Perry - Firework (Official Music Video).mp3"),
    
    Song("Diamonds",
         "Rihanna",
         "Pop",
         "3:45",
         "/logic/new resource/Rihanna - Diamonds.mp3"),
    
    Song("No Scrubs",
         "TLC",
         "R&B",
         "3:36",
         "/logic/new resource/TLC - No Scrubs (Official HD Video).mp3"),
    
    Song("Billie Jean",
         "Michael Jackson",
         "Pop",
         "4:54",
         "/logic/new resource/Michael Jackson - Billie Jean (Official Audio).mp3"),
    
    Song("God's Plan",
         "Drake",
         "Hip Hop",
         "3:18",
         "/logic/new resource/Drake - God's Plan.mp3"),
    
    Song("Terminator",
         "Asake",
         "Afrobeats",
         "3:25",
         "/logic/new resource/Asake - Terminator (Official Video).mp3"),
    
    Song("Empire State of Mind",
         "JAY-Z ft. Alicia Keys",
         "Hip Hop",
         "4:37",
         "/logic/new resource/JAY-Z - Empire State Of Mind ft. Alicia Keys.mp3"),
    
    Song("Waka Waka (This Time for Africa)",
         "Shakira ft. Freshlyground",
         "Pop",
         "3:22",
         "/logic/new resource/Shakira - Waka Waka (This Time for Africa) (The Official 2010 FIFA World Cup™ Song).mp3"),
    
    Song("Hot N Cold",
         "Katy Perry",
         "Pop",
         "3:40",
         "/logic/new resource/Katy Perry - Hot N Cold (Official Music Video).mp3"),
    
    Song("Don't Stop the Music",
         "Rihanna",
         "Pop",
         "4:27",
         "/logic/new resource/Rihanna - Don't Stop The Music.mp3"),
    
    Song("Stronger",
         "Kanye West",
         "Hip Hop",
         "5:12",
         "/logic/new resource/Kanye West - Stronger.mp3"),
    
    Song("Roses",
         "Kanye West",
         "Hip Hop",
         "4:06",
         "/logic/new resource/Roses.mp3"),
    
    Song("All of the Lights",
         "Kanye West ft. Rihanna & Kid Cudi",
         "Hip Hop",
         "4:59",
         "/logic/new resource/Kanye West - All Of The Lights ft. Rihanna, Kid Cudi.mp3"),
    
    Song("Natural High",
         "Freddie Gibbs",
         "Hip Hop",
         "3:31",
         "/logic/new resource/Natural High (Even Higher Learning).mp3"),
    
    Song("SDP Interlude",
         "Travis Scott",
         "Hip Hop",
         "3:11",
         "/logic/new resource/Travis Scott - sdp interlude (Extended).mp3"),
    
    Song("Antidote",
         "Travis Scott",
         "Hip Hop",
         "4:22",
         "/logic/new resource/Travis Scott - Antidote.mp3"),
    
    Song("Lights",
         "Ellie Goulding",
         "Pop",
         "3:30",
         "/logic/new resource/Ellie Goulding - Lights (Official Video).mp3"),
    
    Song("Lush Life",
         "Zara Larsson",
         "Pop",
         "3:21",
         "/logic/new resource/Zara Larsson - Lush Life (Official Video).mp3"),
    
    Song("No Role Modelz",
         "J. Cole",
         "Hip Hop",
         "4:52",
         "/logic/new resource/No Role Modelz.mp3")
]