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
    
