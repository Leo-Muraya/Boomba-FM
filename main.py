import customtkinter as ctk
import ctypes
from home.sidebar import Sidebar
from home.top_bar import TopBar
from home.player_bar import PlayerBar
from home.main_area import MainArea
from home.now_playing import NowPlaying
from logic.player import MusicPlayer
from logic.library import SONGS

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Boomba FM")
app.geometry("1100x680")
app.configure(fg_color="#000000")
app.iconbitmap("assets/icon.ico")
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("musicplayer.app")

# ── Grid configuration ─────────────────────────────────
app.grid_rowconfigure(0, weight=0)
app.grid_rowconfigure(1, weight=1)
app.grid_rowconfigure(2, weight=0)
app.grid_columnconfigure(0, weight=0)
app.grid_columnconfigure(1, weight=1)
app.grid_columnconfigure(2, weight=0, minsize=280)

# ── Initialize player ──────────────────────────────────
player = MusicPlayer()
player.load_library(SONGS)

# ── Build UI ───────────────────────────────────────────
top_bar = TopBar(app)
sidebar = Sidebar(app)
now_playing = NowPlaying(app)
main_area = MainArea(app)
player_bar = PlayerBar(app)

# ── Connect song click to player ───────────────────────
def on_song_selected(song):
    player.play(song)
    now_playing.update(song)
    player_bar.song_title.configure(text=song.title)
    player_bar.artist_name.configure(text=song.artist)
    player_bar.play_btn.configure(image=player_bar.pause_icon)

    # Update next in queue
    next_index = (player.current_index + 1) % len(SONGS)
    next_song = SONGS[next_index]

# ── Connect play/pause button ──────────────────────────
def on_play_pause():
    player.toggle_play_pause()
    if player.is_playing:
        player_bar.play_btn.configure(image=player_bar.pause_icon)
    else:
        player_bar.play_btn.configure(image=player_bar.play_icon)

# ── Connect next and previous ──────────────────────────
def on_next():
    player.next_song()
    if player.current_song:
        on_song_selected(player.current_song)

def on_previous():
    player.previous_song()
    if player.current_song:
        on_song_selected(player.current_song)

# ── Connect volume slider ──────────────────────────────
def on_volume_change(value):
    player.set_volume(value)

# ── Assign buttons ─────────────────────────────────────
player_bar.play_btn.configure(command=on_play_pause)
player_bar.next_btn.configure(command=on_next)
player_bar.previous_btn.configure(command=on_previous)
player_bar.volume_slider.configure(command=on_volume_change)

# ── Pass song click callback to main area ──────────────
main_area.set_song_callback(on_song_selected)

app.mainloop()