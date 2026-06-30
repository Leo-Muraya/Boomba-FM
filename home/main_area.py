import customtkinter as ctk
from logic.library import SONGS

class MainArea:
    def __init__(self, parent):
        self.frame = ctk.CTkFrame(parent, fg_color="#16213e")
        self.frame.grid(row=1, column=1, sticky="nsew", padx=5, pady=5)
        self.on_song_selected = None

        self._build()

    def _build(self):
        # Scrollable frame for song list
        self.song_list_frame = ctk.CTkScrollableFrame(self.frame, fg_color="transparent")
        self.song_list_frame.pack(fill="both", expand=True, padx=20, pady=(15, 20))

        self._display_songs(SONGS)

    def _display_songs(self, songs):
        for widget in self.song_list_frame.winfo_children():
            widget.destroy()

        for index, song in enumerate(songs, start=1):
            self._create_song_row(index, song)

    def _create_song_row(self, index, song):
        row = ctk.CTkFrame(master=self.song_list_frame, fg_color="#1a1a2e", corner_radius=8)
        row.pack(pady=4, fill="x")

        # Index number
        index_label = ctk.CTkLabel(row, text=str(index), width=30, font=ctk.CTkFont(size=12), text_color="gray")
        index_label.pack(side="left", padx=(15, 5), pady=10)

        # initializing album art placeholder
        art_label = ctk.CTkLabel(row, text="🎵", width=35, height=35, fg_color="#2a2a4a", corner_radius=4)
        art_label.pack(side="left", padx=10, pady=10)

        # Title and artist
        info_frame = ctk.CTkFrame(row, fg_color="transparent")
        info_frame.pack(side="left", fill="x", expand=True, padx=10)

        title_label = ctk.CTkLabel(info_frame, text=song.title, font=ctk.CTkFont(size=13, weight="bold"))
        title_label.pack(anchor="w")

        artist_label = ctk.CTkLabel(info_frame, text=song.artist, font=ctk.CTkFont(size=11), text_color="gray")
        artist_label.pack(anchor="w")

        # Genre tag
        genre_label = ctk.CTkLabel(row, text=song.genre, font=ctk.CTkFont(size=11), text_color="#4a90d9")
        genre_label.pack(side="left", padx=10)

        # Duration
        duration_label = ctk.CTkLabel(row, text=song.duration, font=ctk.CTkFont(size=11), text_color="gray")
        duration_label.pack(side="right", padx=15)

        # Make row clickable (including all nested widgets, no matter how deep)
        def _bind_click(widget, s=song):
            widget.bind("<Button-1>", lambda e, song=s: self.on_song_selected(song))
            for child in widget.winfo_children():
                _bind_click(child, s)

        _bind_click(row)

    def set_song_callback(self, callback):
        """Store the callback and rebuild song list with it"""
        self.on_song_selected = callback
        self._display_songs(SONGS)

    def search_songs(self, query):
        query = query.lower().strip()

        if query == "":
            self._display_songs(SONGS)
            return

        filtered = [
            song for song in SONGS
            if query in song.title.lower()
            or query in song.artist.lower()
            or query in song.genre.lower()
        ]
        self._display_songs(filtered)