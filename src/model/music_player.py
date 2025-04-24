import sys
import time
import threading
import keyboard
import random

sys.path.append("src")
from exceptions.exceptions import *

class Song:
    def __init__(self, title: str, artist: str, duration: float):
        self.title: str = title
        self.artist: str = artist
        self.duration: float = duration

    def __repr__(self):
        return f"{self.title}💿 - {self.artist} 🎤 - ({self.duration}seg)"

class Node:
    def __init__(self, song: Song, next: Song = None, prev: Song = None):
        self.song: Song = song
        self.next: Song = next
        self.prev: Song = prev
    
    def __repr__(self):
        if self.next is None:
            next_title = "None"
        else:
            next_title = self.next.song.title
        return f"🎵 {self.song.title} < - > 🎵{next_title}"
    
class Playlist:
    #Double linked list
    def __init__(self, head: Node = None, tail: Node = None):
        self.__head: Node = head
        self.__tail: Node = tail
        self.__size: int = 0
        self.__current_time: float = 0.0
        self.is_playing: bool = False
        self.lock = threading.Lock()

    def add_song(self, title: str, artist: str, duration: float):
        new_song = Song(title, artist, duration)
        new_node = Node(new_song)
        if (self.__size == 0):
            self.__head = new_node
            self.__tail = new_node
        else:
            current_song = self.__head
            while current_song is not None:
                try:
                    if current_song.song.title == new_node.song.title:
                        raise AlreadySong
                except AlreadySong as e:
                    print (f"{e}, {current_song.song.title}")
                    return
                current_song = current_song.next

            self.__tail.next = new_node
            new_node.prev = self.__tail
            self.__tail = new_node
        self.__size += 1
    
    def simulate_playback(self, song: Song, start_time: float = 0.0):
        remaining_time = song.duration - start_time
        if remaining_time <= 0:
            print("La canción ya ha terminado.")
            return

        print(f"🎶 Reproduciendo {song.title} - {song.artist} --- ({song.duration} seg)")
        for second in range(int(start_time), int(song.duration)):
            if second >= song.duration:
                break
            progress = int((second + 1) / song.duration * 30)  # Escala la barra a 30 caracteres
            bar = f"[{'=' * progress}{' ' * (30 - progress)}] {second + 1}/{int(song.duration)} seg"
            print(f"\r{bar}", end="")
            time.sleep(1)  # Espera 1 segundo por cada iteración
        print("\nLa canción ha terminado.")
    
    def play_song(self):
        try:
            if self.__size == 0:
                raise EmptyPlaylist
        except EmptyPlaylist as e:
            print(e)
            return

        if self.__head is None:
            print("No hay más canciones en la Playlist")
            return
        self.simulate_playback(self.__head.song, self.__current_time)
        self.__current_time = 0
    
    # def play_song(self):
    #     try:
    #         if self.__size == 0:
    #             raise EmptyPlaylist
    #     except EmptyPlaylist as e:
    #         print(e)
    #         return
        
    #     if self.__head is None:
    #         print("No hay más canciopnes en la playlist")
    #         return

    #     song = self.__head.song
    #     remaining_time = song.duration - self.__current_time

    #     if remaining_time <= 0:
    #         print("La canción ya ha terminado")
    #         self.next_song()
    #         return

    #     print(f"🎶 Reproduciendo {song.title} - {song.artist} --- ({song.duration})")
    #     for second in range(int(self.__current_time), int(song.duration)):
    #         if self.__current_time >= song.duration:
    #             break
    #         progress = int((self.__current_time + 1) / song.duration * 30)  # Escala la barra a 30 caracteres
    #         bar = f"[{'=' * progress}{' ' * (30 - progress)}] {int(self.__current_time)}/{int(song.duration)} seg"
    #         print(f"\r{bar}", end="")
    #         time.sleep(1)  # Espera 1 segundo por cada iteración
    #         self.__current_time +=1

    #     print("\nLa canción ha terminado.")
    #     self.__current_time = 0.0


    def next_song(self):
        try:
            if self.__size == 0:
                raise EmptyPlaylist
        except EmptyPlaylist as e:
            print(e)
            return

        try:
            if self.__head.next is None or self.__head.next is None:
                self.__head = None
                # self.__tail = self.__head
                self.__current_time = 0
                self.is_playing = False
                raise NoMoreSongs
        except NoMoreSongs as e:
            print(e)
            return
        self.__head = self.__head.next
        self.__current_time = 0
        # return print(f"Reproduciendo ahora: {self.__head.song}")
    
    def prev_song(self):
        try:
            if self.__size == 0:
                raise EmptyPlaylist
        except EmptyPlaylist as e:
            print(e)
            return
        
        try:
            if self.__head.prev == None:
                raise NoPreviousSong
        except NoPreviousSong as e:
            print (e)
            return

        self.__head = self.__head.prev
        # return print(f"Reproduciendo ahora: {self.__head.song}")

    def del_song(self):
        try:
            if self.__size == 0:
                raise EmptyPlaylist
        except EmptyPlaylist as e:
            print(e)
            return

        if self.__head == self.__tail:
            self.__head = None
            self.__tail = None
        else:
            self.__head = self.__head.next
            self.__head.prev = None
        self.__size-=1
        print("❌ Canción eliminada ❌")
    
    # def play_playlist_continous(self):
    #     current_node = self.__head
    #     while (current_node is not None):
    #         self.play_song()
    #         self.next_song()
    #         current_node = current_node.next
    #     hilo = threading.Thread(target=self.forward_time)
    #     hilo.start()

    def forward_time(self, seconds: float):
        try:
            if self.__size == 0:
                raise EmptyPlaylist
        except EmptyPlaylist as e:
            print(e)
            return

        song = self.__head.song
        remaining_time = song.duration - self.__current_time
        if seconds >= remaining_time:
            print(f"⏩ La canción ha terminado.")
            self.next_song()  # Avanza a la siguiente canción si se supera el tiempo restante
        else:
            self.__current_time += seconds
            print(f"⏩+{seconds}")


    def play_playlist_continous(self):
        self.is_playing = True
        
        thread1 = threading.Thread(target=self.play_thread)
        thread2 = threading.Thread(target=self.interaction_thread)
        thread1.start()
        thread2.start()
        
        thread1.join()
        thread2.join()
    def play_thread(self):
        while self.__head is not None:
            self.play_song()
            self.next_song()
        self.is_playing = False
    
    def interaction_thread(self):
        while self.is_playing:
            if keyboard.is_pressed('right'):
                with self.lock:
                    self.forward_time(3)
                time.sleep(0.5)

    
    def show_playlist(self):
        current_node = self.__head
        while(current_node is not None):
            print(current_node.song)
            current_node = current_node.next

    def shuffle(self):
        try:
            if self.__size == 0:
                raise EmptyPlaylist
        except EmptyPlaylist as e:
            print(e)
            return

        nodes = [] 
        current = self.__head
        while current is not None:
            nodes.append(current)
            current = current.next
        random.shuffle(nodes)
        
        print("🔀 Modo aleatorio activado:")
        self.is_playing = True
        thread3 = threading.Thread(target=self.shuffle_thread, args=(nodes,))
        thread4 = threading.Thread(target=self.interaction_thread)
        thread3.start()
        thread4.start()
    
        thread3.join()
        thread4.join()

    def shuffle_thread(self, nodes):
        for node in nodes:
            if not self.is_playing:
                break
            self.simulate_playback(node.song, self.__current_time)
            self.__current_time = 0
        self.is_playing = False


