import pygame
import os
from mutagen.mp3 import MP3


class MusicPlayer:
    def __init__(self):
        # Initialize pygame audio
        pygame.mixer.init()

        self.current_song = None
        self.current_index = 0
        self.is_playing = False
        self.songs = []
        self.song_length = 0
        self.seek_remember = 0

    def load_library(self, songs):
        """Load the song list into the player"""
        self.songs = songs

    def play(self, song):
     if not os.path.exists(song.file_path):
        print(f"File not found: {song.file_path}")
        return

     self.current_song = song
     self.current_index = self.songs.index(song)
     self.is_playing = True
     self.seek_offset = 0  # reset offset for new song

     pygame.mixer.music.load(song.file_path)
     pygame.mixer.music.play()

     audio = MP3(song.file_path)
     self.song_length = audio.info.length
    def get_position(self):
     """Returns how many seconds into the song we are"""
     if self.is_playing:
        pos = pygame.mixer.music.get_pos() / 1000
        return self.seek_offset + pos
     return 0
    
    def seek(self, seconds):
        '''this jumps to a specific part of the song'''
        
        pygame.mixer.music.play(start=seconds)
        
        

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
            
    def seek_to_percentage(self, percentage):
     """Jump to a specific point in the song using a percentage (0 to 1)"""
     if self.current_song and self.song_length > 0:
        seek_seconds = percentage * self.song_length
        self.seek_remember = seek_seconds  # remember where we jumped to
        pygame.mixer.music.play(start=seek_seconds)

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