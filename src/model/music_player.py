import sys
sys.path.append("src")
from exceptions.exceptions import *

class Song:
    def __init__(self, title: str, artist: str, duration: float):
        self.title: str = title
        self.artist: str = artist
        self.duration: float = duration

    def __repr__(self):
        return f"{self.title} - {self.artist} - ({self.duration})"

class Node:
    def __init__(self, song: Song, next: Song = None, prev: Song = None):
        self.song: Song = song
        self.next: Song = next
        self.prev: Song = prev
    
    def __repr__(self):
        return f"🎵 {self.song.title} < - > 🎵{self.next.title}"
    
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
    
    def traverse(self):
        current_node = self.__head
        while (current_node is not None):
            print(current_node.song)
            current_node = current_node.next

if __name__ == "__main__":
    playlist = Playlist()
    playlist.add_song("Treat you better", "Shawn Mendes", 10)
    playlist.add_song("Treat you better", "Shawn Mendes", 10)
    playlist.add_song("When i was your man", "Bruno Mars", 10)
    playlist.traverse()