import customtkinter as ctk

class TopBar:
    def __init__(self, parent):
        self.frame = ctk.CTkFrame(parent, height=55, fg_color="#000000", corner_radius=0)
        self.frame.grid(row=0, column=0, columnspan=3, sticky="ew", padx=10, pady=(5, 0))
        self.frame.grid_propagate(False)

        self._build()

    def _build(self):
        # Back and forward buttons
        nav_frame = ctk.CTkFrame(self.frame, fg_color="transparent")
        nav_frame.pack(side="left", padx=15)

        back_btn = ctk.CTkButton(
            nav_frame,
            text="‹",
            width=30,
            height=30,
            fg_color="#2a2a4a",
            hover_color="#3a3a5a",
            font=ctk.CTkFont(size=18),
            corner_radius=15
        )
        back_btn.pack(side="left", padx=(0, 5))

        forward_btn = ctk.CTkButton(
            nav_frame,
            text="›",
            width=30,
            height=30,
            fg_color="#2a2a4a",
            hover_color="#3a3a5a",
            font=ctk.CTkFont(size=18),
            corner_radius=15
        )
        forward_btn.pack(side="left")

        # Search bar in the middle
        self.search_entry = ctk.CTkEntry(
            self.frame,
            placeholder_text="Search songs, artists, genres...",
            font= ctk.CTkFont(family= "San Fransisco Display Bold", weight = "bold", size = 13),
            width=350,
            height=40,
            corner_radius=20,
            border_width =  0 
            # fg_color="#2a2a4a",
            # border_color="#3a3a5a",
            
        )
        self.search_entry.pack(anchor="center",side = "left", padx=(50,20))

        # Login button on the right
        Register_btn = ctk.CTkButton(
            self.frame,
            text="Register",
            width=80,
            height=35,
            fg_color="#2563eb",
            hover_color="#2a2a4a",
            border_width=1,
            border_color="#4a90d9",
            corner_radius=20
        )
        Register_btn.pack(side="right", padx=5)
        
        login_btn = ctk.CTkButton(
            self.frame,
            text="Login",
            width=80,
            height=35,
            fg_color="transparent",
            hover_color="#2a2a4a",
            border_width=1,
            border_color="#4a90d9",
            corner_radius=20
        )
        login_btn.pack(side="right", padx=5)