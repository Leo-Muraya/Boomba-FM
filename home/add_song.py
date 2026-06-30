import customtkinter as ctk
from tkinter import filedialog
from logic.library import Song

class AddSongDialog:
    def __init__(self, parent, on_song_added):
        self.on_song_added = on_song_added
        self.file_path = ""

        # Frame sits on top of the main area, same grid spot
        self.frame = ctk.CTkFrame(parent, fg_color="#16213e", corner_radius=12, border_width=1, border_color="#2a2a4a")

        self._build()

    def _build(self):
        # Close button
        close_btn = ctk.CTkButton(
            self.frame,
            text="✕",
            width=30,
            height=30,
            fg_color="transparent",
            hover_color="#2a2a4a",
            command=self.hide
        )
        close_btn.pack(anchor="ne", padx=10, pady=10)

        ctk.CTkLabel(
            self.frame,
            text="Add a Song",
            font=ctk.CTkFont(size=18, weight="bold")
        ).pack(pady=(0, 15))

        # Song title input
        ctk.CTkLabel(self.frame, text="Song Title", anchor="w").pack(fill="x", padx=40)
        self.title_entry = ctk.CTkEntry(self.frame, placeholder_text="Enter song title")
        self.title_entry.pack(fill="x", padx=40, pady=(5, 15))

        # Artist input
        ctk.CTkLabel(self.frame, text="Artist", anchor="w").pack(fill="x", padx=40)
        self.artist_entry = ctk.CTkEntry(self.frame, placeholder_text="Enter artist name")
        self.artist_entry.pack(fill="x", padx=40, pady=(5, 15))

        # Genre input
        ctk.CTkLabel(self.frame, text="Genre", anchor="w").pack(fill="x", padx=40)
        self.genre_entry = ctk.CTkEntry(self.frame, placeholder_text="Enter genre (e.g. Pop)")
        self.genre_entry.pack(fill="x", padx=40, pady=(5, 15))

        # File picker button
        self.file_label = ctk.CTkLabel(
            self.frame,
            text="No file selected",
            text_color="gray",
            font=ctk.CTkFont(size=11)
        )
        self.file_label.pack(pady=(5, 5))

        browse_btn = ctk.CTkButton(
            self.frame,
            text="Browse MP3 File",
            command=self._browse_file,
            fg_color="#2a2a4a",
            hover_color="#3a3a5a"
        )
        browse_btn.pack(pady=(0, 20))

        # Add button
        add_btn = ctk.CTkButton(
            self.frame,
            text="Add Song",
            command=self._add_song,
            fg_color="#4a90d9",
            hover_color="#357abd"
        )
        add_btn.pack(pady=(0, 20))

    def _browse_file(self):
        path = filedialog.askopenfilename(
            title="Select an MP3 file",
            filetypes=[("Audio Files", "*.mp3")]
        )
        if path:
            self.file_path = path
            filename = path.split("/")[-1]
            self.file_label.configure(text=filename, text_color="#4a90d9")

    def _add_song(self):
        title = self.title_entry.get().strip()
        artist = self.artist_entry.get().strip()
        genre = self.genre_entry.get().strip()

        if not title or not artist or not self.file_path:
            self.file_label.configure(text="Please fill all fields and select a file", text_color="red")
            return

        new_song = Song(title, artist, genre or "Unknown", "0:00", self.file_path)
        self.on_song_added(new_song)
        self.hide()

    def show(self):
        # Overlay on top of the main area grid spot
        self.frame.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.7, relheight=0.8)
        self.frame.lift()

    def hide(self):
        self.frame.place_forget()