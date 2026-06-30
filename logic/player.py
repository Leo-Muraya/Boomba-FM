import pygame
import os

class MusicPlayer:
    def __init__(self):
        # Initialize pygame audio
        pygame.mixer.init()

        self.current_song = None
        self.current_index = 0
        self.is_playing = False
        self.songs = []

    def load_library(self, songs):
        """Load the song list into the player"""
        self.songs = songs

    def play(self, song):
        """Play a specific song"""
        if not os.path.exists(song.file_path):
            print(f"File not found: {song.file_path}")
            return

        self.current_song = song
        self.current_index = self.songs.index(song)
        self.is_playing = True

        pygame.mixer.music.load(song.file_path)
        pygame.mixer.music.play()

    def pause(self):
        """Pause the current song"""
        if self.is_playing:
            pygame.mixer.music.pause()
            self.is_playing = False

    def resume(self):
        """Resume the paused song"""
        if not self.is_playing:
            pygame.mixer.music.unpause()
            self.is_playing = True

    def toggle_play_pause(self):
        """Switch between play and pause"""
        if self.is_playing:
            self.pause()
        else:
            self.resume()

    def next_song(self):
        """Play the next song in the list"""
        if not self.songs:
            return
        self.current_index = (self.current_index + 1) % len(self.songs)
        self.play(self.songs[self.current_index])

    def previous_song(self):
        """Play the previous song in the list"""
        if not self.songs:
            return
        self.current_index = (self.current_index - 1) % len(self.songs)
        self.play(self.songs[self.current_index])

    def set_volume(self, value):
        """Set volume between 0.0 and 1.0"""
        pygame.mixer.music.set_volume(value)

    def stop(self):
        """Stop music completely"""
        pygame.mixer.music.stop()
        self.is_playing = False
        self.current_song = None