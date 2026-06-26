import customtkinter as ctk

class NowPlaying:
    def __init__(self, parent):
        self.frame = ctk.CTkFrame(parent, width=320, fg_color="#1a1a2e")
        self.frame.grid(row=1, column=2, sticky="nsew", padx =(0,5), pady = 5)
        self.frame.grid_propagate(False)

        self._build()

    def _build(self):
        # Title
        title = ctk.CTkLabel(
            self.frame,
            text="Now Playing",
            font=ctk.CTkFont(size=16, weight="bold")
        )
        title.pack(pady=(20, 5), padx=(25), anchor="w")

        # Album art placeholder
        self.album_art = ctk.CTkLabel(
            self.frame,
            text="🎵",
            width=280,
            height=280,
            fg_color="#2a2a4a",
            corner_radius=15,
            font=ctk.CTkFont(size=60)
        )
        self.album_art.pack(pady=(5, 15), padx = 15)

        # Song title
        self.song_label = ctk.CTkLabel(
            self.frame,
            text="No song playing",
            font=ctk.CTkFont(family= "Gill Sans", size=24, weight="bold"),
            wraplength=200
        )
        self.song_label.pack(anchor = "w",pady=(0, ), padx=(25,15))

        # Artist name
        self.artist_label = ctk.CTkLabel(
            self.frame,
            text="Unknown Artist",
            font=ctk.CTkFont(size=12),
            text_color="gray"
        )
        self.artist_label.pack(pady=(0, 5),padx=(25,15), anchor = "w")

        # Genre and duration
        self.meta_label = ctk.CTkLabel(
            self.frame,
            text="",
            font=ctk.CTkFont(size=11),
            text_color="#4a90d9"
        )
        self.meta_label.pack(pady=(0, 20))

    def update(self, song):
        """Call this method when a new song is selected"""
        self.song_label.configure(text=song.title)
        self.artist_label.configure(text=song.artist)
        self.meta_label.configure(text=f"{song.genre} • {song.duration}")