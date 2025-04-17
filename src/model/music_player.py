import sys
import time
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
    
    def play_song(self):
        try:
            if self.__size == 0:
                raise EmptyPlaylist
        except EmptyPlaylist as e:
            print(e)
            return
        print(f"Reproduciendo ... \n{self.__head.song}")
        time.sleep(self.__head.song.duration)


    def next_song(self):
        try:
            if self.__size == 0:
                raise EmptyPlaylist
        except EmptyPlaylist as e:
            print(e)
            return

        try:
            if self.__head.next is None:
                raise NoMoreSongs
        except NoMoreSongs as e:
            print(e)
            return
        self.__head = self.__head.next
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
    
    def play_playlist_continous(self):
        current_node = self.__head
        while (current_node is not None):
            self.play_song()
            self.next_song()
            current_node = current_node.next
    
    def show_playlist(self):
        current_node = self.__head
        while(current_node is not None):
            print(current_node.song)
            current_node = current_node.next

