class AlreadySong(Exception):
    def __init__(self, message="La canción ya está en la playlist"):
        super().__init__(message)