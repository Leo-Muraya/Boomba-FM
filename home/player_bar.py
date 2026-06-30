import customtkinter as ctk
from customtkinter import CTkImage
from PIL import Image 


class PlayerBar:
    def __init__(self, parent):
        self.frame = ctk.CTkFrame(master=parent, height=80, fg_color="#000000")
        self.frame.grid(row=2, column=0, columnspan=3, sticky="nsew", padx = 5, pady = (0,5))
        self.frame.grid_propagate(False)
        self.frame.grid_columnconfigure(1, weight=1)

        self._build()

    def _build(self):
        left_frame = ctk.CTkFrame(master=self.frame, fg_color="transparent")
        left_frame.grid(row=0, column=0, sticky="w", padx=8, pady=(1,10))

        album_art = ctk.CTkLabel(
            master=left_frame,
            text="♫",
            width=60,
            height=60,
            fg_color="#1f2937",
            corner_radius=4,
            font=ctk.CTkFont(size=22)
        )
        album_art.pack(side="left", padx=(0, 10))

        song_info = ctk.CTkFrame(master=left_frame, fg_color="transparent")
        song_info.pack(side="left")

        self.song_title = ctk.CTkLabel(
            master=song_info,
            text="No Song",
            font=ctk.CTkFont(family="SNFS Display Bold",size=16, weight="bold"),
            width=150,
            anchor="w"
        )
        self.song_title.pack(anchor="w")

        self.artist_name = ctk.CTkLabel(
            master=song_info,
            text="No Artist",
            font=ctk.CTkFont(size=13),
            text_color="gray"
        )
        self.artist_name.pack(anchor="w")

        center_frame = ctk.CTkFrame(master=self.frame, fg_color="transparent")
        center_frame.grid(row=0, column=1, sticky="nsew", padx=20, pady=10)
        center_frame.grid_propagate(False)

        controls_frame = ctk.CTkFrame(master=center_frame, fg_color="transparent")
        controls_frame.pack(pady=(0, 0))
        
        previous_btn = CTkImage(Image.open("assets/images/prev.png"), size = (30,26))
        self.previous_btn = previous_btn
        
        
        self.previous_btn = ctk.CTkButton(
            master=controls_frame,
            text="",
            image = self.previous_btn,
            width=20,
            height = 20,
            fg_color="transparent",
            hover_color="#000000",
            corner_radius=25
        )
        self.previous_btn.pack(side="left", padx=0)

        # Load icons
        play_icon = CTkImage(Image.open("assets/images/play.png"), size=(35, 35))
        pause_icon = CTkImage(Image.open("assets/images/pause.png"), size=(35, 35))

        # Store icons so we can switch between them later
        self.play_icon = play_icon
        self.pause_icon = pause_icon

        # Play button
        self.play_btn = ctk.CTkButton(
            controls_frame,
            text="",
            image=self.play_icon,
            width=20,
            height=20,
            fg_color="transparent",
            hover_color="#000000",
            corner_radius=25
        )
        self.play_btn.pack(side="left", padx=5)
        
        #next button
        next_btn = CTkImage(Image.open ("assets/images/next.png"), size=(30,26))
        self.next_btn = next_btn
        
    
        self.next_btn = ctk.CTkButton(
            master=controls_frame,
            text="",
            image=self.next_btn,
            width=20,
            height=20,
            fg_color="transparent",
            hover_color="#000000",
            corner_radius=25
        )
        self.next_btn.pack(side="left", padx=0)

        progress_frame = ctk.CTkFrame(master=center_frame, fg_color="transparent", width =150)
        progress_frame.pack(fill = "x", padx= 50, anchor= "center")

        self.current_time = ctk.CTkLabel(
            master=progress_frame,
            text="2:36",
            font=ctk.CTkFont(size=11),
            text_color="gray"
        )
        self.current_time.pack(side="left")

        self.progress_bar = ctk.CTkProgressBar(
            master=progress_frame,
            fg_color="#1b2841",
            progress_color="#2563eb",
            
        )
        self.progress_bar.pack(side="left", fill="x", expand=True, padx=10)
        self.progress_bar.set(0.45)

        self.total_time = ctk.CTkLabel(
            master=progress_frame,
            text="5:00",
            font=ctk.CTkFont(size=11),
            text_color="gray"
        )
        self.total_time.pack(side="left")

        right_frame = ctk.CTkFrame(master=self.frame, fg_color="transparent")
        right_frame.grid(row=0, column=2, sticky="e", padx=20, pady=10)

        volume_label = ctk.CTkLabel(master=right_frame, text="🔊", font=ctk.CTkFont(size=14))
        volume_label.pack(side="left", padx=(0, 8))

        self.volume_slider = ctk.CTkSlider(
            master=right_frame,
            width=120,
            from_=0,
            to=1,
            fg_color="#1b2841",
            progress_color="#2563eb"
        )
        self.volume_slider.pack(side="left")
        self.volume_slider.set(0.7)





            

            


            







