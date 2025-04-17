import sys
sys.path.append("src")
from model.music_player import *

def data_song():
    song = input("Ingresa el nombre de la canción: ")
    artist = input("Ingresa el nombre del artista: ")
    duration = float(input("Ingresa el tiempo de la canción: "))
    return song, artist, duration

def console_menu():
    print("====Bienvenido====")
    print(" ===MelodyBox===")
    print("Opciones - Oprime el número correspondiente:\n1. Añadir canción.\n2. Reproducir Canción.\n3. Siguiente canción. \n4. Canción previa. \n5. Eliminar canción actual. \n6. Eliminar canción por nombre. \n7. Mostrar Playlist. \n8. Modo Aleatorio. \n9. Adelantar canción. \n10. Crear subplaylist. \n11. Reproducir playlist")

playlist = Playlist()
playlist.add_song(title="Treat You Better", artist="Shawn Mendes", duration=3.50)
playlist.add_song(title="Locked Out of Heaven", artist="Bruno Mars", duration=3.92)
playlist.add_song(title="Wonder", artist="Shawn Mendes", duration=2.52)

while True:
    console_menu()
    option = int(input("Ingresa tu elección (1-10): "))
    
    if option == 1:
        song, artist, duration = data_song()
        playlist.add_song(title=song, artist=artist, duration=duration)

    elif option == 2:
        playlist.play_song()

    elif option == 3:
        playlist.next_song()

    elif option == 4:
        playlist.prev_song()

    elif option == 5:
        playlist.del_song()

    elif option == 6:
        #Hacer metodo de eliminar con nombre
        ...
    elif option == 7:
        playlist.show_playlist()

    elif option == 8:
        #Hacer metodo modo aleatorio
        ...
    elif option == 9:
        #Hacer metodo para adelantar canción
        ...
    elif option == 10:
        #Hacer metodo para crear subplaylist
        ...

    elif option == 11:
        playlist.play_playlist_continous()