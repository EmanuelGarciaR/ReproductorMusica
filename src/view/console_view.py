import sys
sys.path.append("src")
from model.music_player import *
import threading

def data_song():
    song = input("Ingresa el nombre de la canción: ")
    artist = input("Ingresa el nombre del artista: ")
    duration = float(input("Ingresa el tiempo de la canción: "))
    return song, artist, duration

def console_menu():
    print("====Bienvenido====")
    # print(" ===MelodyBox===")
    print("\n🎼 === Bienvenido - Reproductor de música === 🎼")
    print("📋 Ingresa el número de la opción que deseas realizar")
    print("1. Añadir canción a la playlist desde el principio")
    print("2. Reproducir la primera canción de la playlist")
    print("3. Reproducir canción por su nombre")
    print("3. Avanzar a la siguiente canción ⏭️")
    print("4. Devolverse a la canción anterior ⏮️")
    print("5. Eliminar canción actual ❌")
    print("6. Eliminar canción por su nombre ❌")
    print("7. Mostrar playlist 📜")
    print("8. Activar modo aleatorio 🔀")
    print("9. Adelantar canción ⏩") 
    print("10. Generar una subplaylist 🧩") 
    print("11. Reproducir playlist ▶️")
    print("_______________________________\n")
    print("12. Salir 🚪")
    # print("Opciones - Oprime el número correspondiente:\n1. Añadir canción.\n2. Reproducir Canción.\n3. Siguiente canción. \n4. Canción previa. \n5. Eliminar canción actual. \n6. Eliminar canción por nombre. \n7. Mostrar Playlist. \n8. Modo Aleatorio. \n9. Adelantar canción. \n10. Crear subplaylist. \n11. Reproducir playlist")

playlist = Playlist()
playlist.add_song(title="Treat You Better", artist="Shawn Mendes", duration=10)
playlist.add_song(title="Locked Out of Heaven", artist="Bruno Mars", duration=15)
playlist.add_song(title="Wonder", artist="Shawn Mendes", duration=10)

while True:
    console_menu()
    option = int(input("Ingresa tu elección (1-12): "))
    
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
        playlist.shuffle()
    elif option == 9:
        sec = float(input("Ingresa la cantidad de segundos que deseas adelantar: "))
        playlist.forward_time(sec)
    elif option == 10:
        #Hacer metodo para crear subplaylist
        ...

    elif option == 11:
        playlist.play_playlist_continous()
    
    elif option == 12:
        print("👋 ¡Hasta pronto! Cerrando el reproductor...")
        break
    else:
        print("❌ Opción no válida. Por favor, elige una opción del menú.")