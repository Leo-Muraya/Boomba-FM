import customtkinter as ctk
import ctypes
from home.top_bar import TopBar
from home.sidebar import Sidebar
from home.player_bar import PlayerBar
from home.main_area import MainArea
from home.now_playing import NowPlaying

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Boomba FM")
app.geometry("1100x680")
app.configure(fg_color = "#0d0d0d")
app.iconbitmap("logo3.ico")
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("musicplayer.app")

app.grid_rowconfigure(0, weight=0)  
app.grid_rowconfigure(1, weight=1)  
app.grid_rowconfigure(2, weight=0,)  
app.grid_columnconfigure(0, weight=0, minsize=320)
app.grid_columnconfigure(1, weight=1)
app.grid_columnconfigure(2, weight=0, minsize=400)


topbar = TopBar(app)
sidebar = Sidebar(app)
player_bar = PlayerBar(app)
main_area = MainArea(app)
now_playing = NowPlaying(app)

app.mainloop()