import customtkinter as ctk

class Sidebar:
    def __init__(self, parent,on_open_add_song=None):
        # sidebar frame
        self.frame = ctk.CTkFrame(master=parent, width=150, fg_color = "#1a1a2e")
        self.frame.grid(row=1, column=0, sticky="nsew", padx =(5,0), pady= 5)
        self.frame.grid_propagate(False)
        self.on_open_add_song = on_open_add_song

        self._build()
    
    def _build(self):
        #App title
        app_label = ctk.CTkLabel(master= self.frame , text = "Your Library", font= ctk.CTkFont(size= 18, weight="bold"))
        app_label.pack(pady = (30 ,20), padx =20, anchor= "w")

        #nav buttons

        nav_buttons = ["Explore", "Added Songs"]

        for btn_text in nav_buttons:
            btn = ctk.CTkButton(
                master= self.frame,
                text= btn_text,
                anchor = "w",
                fg_color="transparent",
                hover_color ="#2a2a4a",
                font=ctk.CTkFont(family = "SFNS Display Bold" ,size = 16)
            )

            btn.pack(fill="x", pady = 2, padx =(20,10))
        
        #personal section label

        # personal_label = ctk.CTkLabel(master = self.frame, text ="Personal", font= ctk.CTkFont(family="SFNS Display Bold", size = 18))
        # personal_label.pack(pady = (20, 5), padx = 20, anchor = "w")

        #personal buttons

        personal_buttons = ["Favorites", "Albums", "Playlist" , "Genres"]
        for btn_text in personal_buttons:
            btn = ctk.CTkButton(
                master = self.frame,
                text = btn_text,
                anchor = "w",
                fg_color="transparent",
                hover_color="#2a2a4a",
                font=ctk.CTkFont(family = "SFNS Display Bold" ,size = 16)
            )
            btn.pack(fill = "x",padx = (20,10), pady = 2)



        # Add song buttin
        add_song = ctk.CTkButton(
            master = self.frame,
            text = "+ Add a song",
            anchor="w",
            fg_color="transparent",
            hover_color="#2a2a4a",
            font = ctk.CTkFont(family = "SFNS Display Bold", size = 13),
            command=lambda: self.on_open_add_song() if self.on_open_add_song else None
         
        )

        add_song.pack(fill = "x", padx= (5,10), pady=(0,5), side ="bottom")
        
        #playlist button at the bottom
        create_playlist = ctk.CTkButton(master = self.frame, 
                                        text ="+ Create Playlist", 
                                        anchor = "w",
                                        fg_color="transparent",
                                        hover_color="#2a2a4a",
                                        font = ctk.CTkFont(family="SFNS Display Bold",size = 13)
                                        )
        create_playlist.pack(fill = "x", padx= (5,10), pady=(0,5), side ="bottom")

