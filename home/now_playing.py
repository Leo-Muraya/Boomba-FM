import customtkinter as ctk
from PIL import Image
import os

class NowPlaying:
    def __init__(self, parent):
        self.parent = parent
        self.frame = ctk.CTkFrame(parent, width=320, fg_color="#1a1a2e")
        self.frame.grid(row=1, column=2, sticky="nsew", padx=(0,5), pady=5)
        self.frame.grid_propagate(False)
        
        # Store current image to prevent garbage collection
        self.current_ctk_image = None
        
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
            corner_radius=12,
            font=ctk.CTkFont(size=60)
        )
        self.album_art.pack(pady=(5, 15), padx=15)

        # Song title
        self.song_label = ctk.CTkLabel(
            self.frame,
            text="No song playing",
            font=ctk.CTkFont(family=("SNFS Display Bold", "Arial"), size=24, weight="bold"),
            wraplength=250
        )
        self.song_label.pack(anchor="w", pady=(0,), padx=(25,15))

        # Artist name
        self.artist_label = ctk.CTkLabel(
            self.frame,
            text="Unknown Artist",
            font=ctk.CTkFont(family=("SNFS Display", "Arial"), size=15, weight="bold"),
            text_color="gray"
        )
        self.artist_label.pack(pady=(0, 5), padx=(25,15), anchor="w")

        # Genre and duration
        self.meta_label = ctk.CTkLabel(
            self.frame,
            text="",
            font=ctk.CTkFont(size=11),
            text_color="#4a90d9"
        )
        self.meta_label.pack(pady=(0, 20))

    def load_image(self, image_path):
        """Load image from path and return CTkImage object"""
        try:
            if image_path and os.path.exists(image_path):
                # Open and resize image
                image = Image.open(image_path)
                # Convert to RGB if necessary (for PNG with alpha)
                if image.mode in ('RGBA', 'LA'):
                    background = Image.new('RGB', image.size, (42, 42, 74))  # #2a2a4a
                    background.paste(image, mask=image.split()[-1] if image.mode == 'RGBA' else None)
                    image = background
                elif image.mode != 'RGB':
                    image = image.convert('RGB')
                
                # Create CTkImage
                ctk_image = ctk.CTkImage(light_image=image, dark_image=image, size=(280, 280))
                return ctk_image
            return None
        except Exception as e:
            print(f"Error loading image from {image_path}: {e}")
            return None

    def update(self, song):
        """Update the display with a new song"""
        if not song:
            self.song_label.configure(text="No song playing")
            self.artist_label.configure(text="Unknown Artist")
            self.meta_label.configure(text="")
            self.album_art.configure(image=None, text="🎵")
            self.current_ctk_image = None
            return
            
        # Update text info
        self.song_label.configure(text=song.title)
        self.artist_label.configure(text=song.artist)
        self.meta_label.configure(text=f"{song.genre} • {song.duration}")
        
        # Load and display album art from the song's image_path
        if song.image_path:
            ctk_image = self.load_image(song.image_path)
            if ctk_image:
                # Store reference to prevent garbage collection
                self.current_ctk_image = ctk_image
                self.album_art.configure(image=ctk_image, text="")
                return
        
        # If no image loaded, show placeholder
        self.album_art.configure(image=None, text="🎵")
        self.current_ctk_image = None