class Song:
    def __init__(self, title: str, artist: str, duration: float):
        self.title: str = title
        self.artist: str = artist
        self.duration: float = duration

    def __repr__(self):
        return f"{self.title} - {self.artist} - ({self.duration})"

class Node:
    def __init__(self, value: Song, next: Song = None, prev: Song = None):
        self.value: Song = value
        self.next: Song = next
        self.prev: Song = prev
    
    def __repr__(self):
        return f"🎵 {self.value.title} < - > 🎵{self.next.title}"
    
class DoubleLinkedList:
    def __init__(self, head: Node = None, tail: Node = None):
        self.__head: Node = head
        self.__tail: Node = tail
        self.__size: int = 0