import os


def lista_a_vlc(lista):
    assert isinstance(lista, list)
    canciones = " ".join(lista)
    ruta_vlc = '"C:\\Program Files\\VideoLAN\\VLC\\vlc.exe"'
    try:
        exec(ruta_vlc)
    except OSError:
        print('No tiene instalado el VLC')
    else:
        pass
    comando = ruta_vlc + " " + canciones
    assert isinstance(comando, str)
    return os.popen(comando)
