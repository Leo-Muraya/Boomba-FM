import customtkinter as ctk
import ctypes
from home.sidebar import Sidebar
from home.top_bar import TopBar
from home.player_bar import PlayerBar
from home.main_area import MainArea
from home.now_playing import NowPlaying
from logic.player import MusicPlayer
from logic.library import SONGS
from home.add_song import AddSongDialog

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

# ── Build UI (main_area must exist before add_song_dialog) ──
top_bar = TopBar(app)
now_playing = NowPlaying(app)
main_area = MainArea(app)
player_bar = PlayerBar(app)

# ── Add song callback (must be defined before AddSongDialog uses it) ──
def on_song_added(new_song):
    SONGS.append(new_song)
    main_area._display_songs(SONGS)

# ── Now create the add song dialog ──────────────────────
add_song_dialog = AddSongDialog(main_area.frame, on_song_added)

# ── Now create sidebar, passing in the dialog's show method ──
sidebar = Sidebar(app, on_open_add_song=add_song_dialog.show)

# ── Connect song click to player ───────────────────────
def on_song_selected(song):
    player.play(song)
    now_playing.update(song)
    player_bar.song_title.configure(text=song.title)
    player_bar.artist_name.configure(text=song.artist)
    player_bar.play_btn.configure(image=player_bar.pause_icon)

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

def update_progress():
    if player.is_playing and player.current_song:
        position = player.get_position()
        length = player.song_length

        if length > 0:
            progress = position / length
            player_bar.progress_bar.set(progress)

            # Format current time as M:SS
            current_min = int(position // 60)
            current_sec = int(position % 60)
            player_bar.current_time.configure(text=f"{current_min}:{current_sec:02d}")

            # Format total time as M:SS
            total_min = int(length // 60)
            total_sec = int(length % 60)
            player_bar.total_time.configure(text=f"{total_min}:{total_sec:02d}")

            # Auto play next song when current one ends
            if position >= length - 0.5:
                on_next()

    # Run this function again after 500ms
    app.after(500, update_progress)

# ── Connect volume slider ──────────────────────────────
def on_volume_change(value):
    player.set_volume(value)

# ── Connect seek (progress bar dragging) ───────────────
def on_seek(percentage):
    player.seek_to_percentage(percentage)

def on_search(query):
    main_area.search_songs(query)

# ── Assign buttons ─────────────────────────────────────
player_bar.play_btn.configure(command=on_play_pause)
player_bar.next_btn.configure(command=on_next)
player_bar.previous_btn.configure(command=on_previous)
player_bar.volume_slider.configure(command=on_volume_change)
player_bar.on_seek = on_seek
top_bar.on_search = on_search

# ── Pass song click callback to main area ──────────────
main_area.set_song_callback(on_song_selected)

update_progress()
app.mainloop()