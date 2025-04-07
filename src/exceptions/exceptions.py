class AlreadySong(Exception):
    def __init__(self, message = "La canción ya está en la playlist"):
        super().__init__(message)

class EmptyPlaylist(Exception):
    def __init__(self, message = "No hay canciones para reproducir en la playlist"):
        super().__init__(message)

class NoPreviousSong(Exception):
    def __init__(self, message = "Estás reproduciendo la primer canción. No hay canción previa"):
        super().__init__(message)

class NoMoreSongs(Exception):
    def __init__(self, message="No hay más canciones siguientes en la playlist"):
        super().__init__(message)