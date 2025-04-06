

class Song:
    def __init__(self, title: str, artist: str, duration: float):
        self.title: str = title
        self.artist: str = artist
        self.duration: float = duration
    
    def __repr__(self):
        return f"{self.title} - {self.artist} - ({self.duration})"