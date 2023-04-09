import librosa
import numpy as np
import soundfile as sf
import spleeter
from sklearn.decomposition import NMF
import os



def separarAudio(path):

    # cargar separador vocal
    separator = spleeter.Spleeter('spleeter:2stems')

    # separar en vocal e instrumental
    separator.separate_to_file(path, 'src/main/utils/NotesRecognizer')

    # Obtener las rutas de las pistas separadas
    directorio_salida = 'src/main/utils/NotesRecognizer'
    pista_vocal = os.path.join(directorio_salida, 'src/main/utils/NotesRecognizer/vocals.wav')
    pista_instrumental = os.path.join(directorio_salida, 'src/main/utils/NotesRecognizer/accompaniment.wav')

    sf.write("src/main/utils/NotesRecognizer/voz.wav", pista_vocal)
    sf.write("src/main/utils/NotesRecognizer/instrumental.wav", pista_instrumental)