
import numpy as np
import librosa
# from librosa.core import hz_to_noteName
from pathlib import Path
from glob import glob
import pyaudio

# import music21
# from pydub import AudioSegment
# from pydub.playback import play


# Notas y su frecuencia
# A0: A (La) de la escala 0
# A4: A (La) de la escala 4, es el la de 440 Hz
# Sharp: Sostenido
# Flat: bemol
notes = {'A0': 27.5, 
        'A#0': 29.14, 
        'Bb0': 29.14, 
        'B0': 30.87, 
        'C1': 32.7, 
        'C#1': 34.65, 
        'Db1': 34.65, 
        'D1': 36.71, 
        'D#1': 38.89, 
        'Eb1': 38.89, 
        'E1': 41.2, 
        'F1': 43.65, 
        'F#1': 46.25, 
        'Gb1': 46.25, 
        'G1': 49.0, 
        'G#1': 51.91, 
        'Ab1': 51.91, 
        'A1': 55.0, 
        'A#1': 58.27, 
        'Bb1': 58.27, 
        'B1': 61.74, 
        'C2': 65.41, 
        'C#2': 69.3, 
        'Db2': 69.3, 
        'D2': 73.42,
        'D#2': 77.78,
        'Eb2': 77.78,
        'E2': 82.41, 
        'F2': 87.31, 
        'F#2': 92.5, 
        'Gb2': 92.5, 
        'G2': 98.0, 
        'G#2': 103.83, 
        'Ab2': 103.83, 
        'A2': 110.0, 
        'A#2': 116.54, 
        'Bb2': 116.54, 
        'B2': 123.47, 
        'C3': 130.81, 
        'C#3': 138.59, 
        'Db3': 138.59, 
        'D3': 146.83, 
        'D#3': 155.56, 
        'Eb3': 155.56, 
        'E3': 164.81, 
        'F3': 174.61, 
        'F#3': 185.0, 
        'Gb3': 185.0, 
        'G3': 196.0, 
        'G#3': 207.65, 
        'Ab3': 207.65, 
        'A3': 220.0, 
        'A#3': 233.08, 
        'Bb3': 233.08, 
        'B3': 246.94, 
        'C4': 261.63, 
        'C#4': 277.18, 
        'Db4': 277.18, 
        'D4': 293.66, 
        'D#4': 311.13, 
        'Eb4': 311.13, 
        'E4': 329.63, 
        'F4': 349.23, 
        'F#4': 369.99, 
        'Gb4': 369.99, 
        'G4': 392.0, 
        'G#4': 415.3, 
        'Ab4': 415.3, 
        'A4': 440.0, 
        'A#4': 466.16, 
        'Bb4': 466.16, 
        'B4': 493.88, 
        'C5': 523.25, 
        'C#5': 554.37, 
        'Db5': 554.37, 
        'D5': 587.33, 
        'D#5': 622.25,
        'Eb5': 622.25, 
        'E5': 659.26, 
        'F5': 698.46, 
        'F#5': 739.99,
        'Gb5': 739.99, 
        'G5': 783.99, 
        'G#5': 830.61,
        'Ab5': 830.61,
        'A5': 880.0, 
        'A#5': 932.33, 
        'Bb5': 932.33, 
        'B5': 987.77, 
        'C6': 1046.5, 
        'C#6': 1108.73, 
        'Db6': 1108.73, 
        'D6': 1174.66, 
        'D#6': 1244.51, 
        'Eb6': 1244.51, 
        'E6': 1318.51, 
        'F6': 1396.91, 
        'F#6': 1479.98, 
        'Gb6': 1479.98, 
        'G6': 1567.98, 
        'G#6': 1661.22, 
        'Ab6': 1661.22, 
        'A6': 1760.0, 
        'A#6': 1864.66, 
        'Bb6': 1864.66, 
        'B6': 1975.53, 
        'C7': 2093.0, 
        'C#7': 2217.46, 
        'Db7': 2217.46, 
        'D7': 2349.32, 
        'D#7': 2489.02, 
        'Eb7': 2489.02, 
        'E7': 2637.02, 
        'F7': 2793.83, 
        'F#7': 2959.96, 
        'Gb7': 2959.96, 
        'G7': 3135.96, 
        'G#7': 3322.44, 
        'Ab7': 3322.44, 
        'A7': 3520.0, 
        'A#7': 3729.31, 
        'Bb7': 3729.31, 
        'B7': 3951.07, 
        'C8': 4186.01, }

# Funcion que voy a usar (Aure) para probar distintas liberias
# que ayuden a reconocer notas de audios
def reconocedorDeNotasAure():
    # Audio de entrada
    pista = glob("src/main/utils/NotesRecognizer/prueba2.mp3")
    pistaPersonalidad = glob("src/main/utils/NotesRecognizer/recorte.wav")
    
    # Load
    y, sr = librosa.load(pista[0])
    
    # Extraer la frecuencia fundamental
    f0, voiced_flag, voiced_probs = librosa.pyin(y, fmin=librosa.note_to_hz('C2'), fmax=librosa.note_to_hz('C7'))

    # convertir la frecuencia en una nota musical
    # note_number = int(round(12*np.log2(f0/440) + 69))
    # note_name = librosa.midi_to_note_name(note_number)
    escribirFichero(f0)

def escribirFichero(f0):
    f = open("src/main/utils/NotesRecognizer/fichero.txt", 'w')
    for line in f0:
        f.write(str(line) + "\n")


def leerFichero():
    f = open("src/main/utils/NotesRecognizer/fichero.txt", 'r')
    lines = f.readlines()

    notesVector = []
    for line in lines:
        if line.find("nan") == -1:
            data = float(line)
            notesVector.append(getNearestFrequency(data))
            nota= notes[getNearestFrequency(data)]
            print(getNearestFrequency(data))
            # play_note(nota, 0.01)

    print(notesVector[0:40])
    

def getNearestFrequency(f):
    left = 4200
    right = notes['C8'] #<>
    anterior = notes['A#0']

    for key in notes.keys():
        value = notes[key]
        if value > f:
            rightFreq = value
            rightNote = key
            leftFreq = notes[anterior]
            leftNote = anterior
            break
        anterior = key
    
    result1 = f - leftFreq
    result2 = rightFreq - f

    result = rightNote
    if result1 < result2:
        result = leftNote
    
    return result

def recognizeNotes():

    # extractVoice(file)

    filepath = Path("C:/Users/danie/Desktop/UltraStar-Song-Maker/src/main/utils/NotesRecognizer/vocals.wav")

    y, sr = librosa.load(filepath)
    print(y)
    print(sr)

    # Prueba que esta bien cargada la canción
    # with open("notas.txt", "w") as f:
    #     for i in range(len(y)):
    #         f.write(str(y[i])+"\n")

    # # Extraer las frecuencias y la magnitud de la señal de audio
    # freqs, magnitudes = librosa.core.magphase(librosa.stft(y))

    # # Convertir las magnitudes a dB
    # magnitudes_db = librosa.amplitude_to_db(magnitudes)

    # # Encontrar las frecuencias dominantes en cada marco de tiempo
    # frequencies = librosa.core.fft_frequencies(sr=sr, n_fft=2048)
    # times = librosa.core.frames_to_time(np.arange(magnitudes_db.shape[1]), sr=sr, hop_length=512)
    # freqs_idx = np.argmax(magnitudes_db, axis=0)
    # dominant_freqs = frequencies[freqs_idx]

    # # Asignar las frecuencias a notas musicales
    # note_names = librosa.hz_to_note(dominant_freqs)

    # # Escribir las notas en un archivo de texto
    # with open('notas.txt', 'w') as f:
    #     for i in range(len(note_names)):
    #         f.write("{:.2f} {}\n".format(times[i], note_names[i]))


    # # Leer archivo mp3
    # song = AudioSegment.from_mp3(filepath)

    # # Extraer notas musicales
    # samples = song.get_array_of_samples()

    # # Convertir a objeto numpy
    # notes = np.array(samples)


    # # Escribir notas en archivo txt
    # with open("notas.txt", "w") as f:
    #     f.write(str(notes))

    # y, sr = librosa.load(filepath)
    # print(len(y))
    # print("sr",sr)
    # pitches, magnitudes = librosa.piptrack(y, sr=sr)
    # notes = []
    # for i in range(pitches.shape[0]):
    #     curr_pitch = pitches[i]
    #     curr_magnitude = magnitudes[i].max()
    #     note = librosa.hz_to_note(curr_pitch, octave=False, cents=True)
    #     if curr_magnitude > 0.5:
    #         notes.append(note)
    # return notes

    # Convertir audio a notas musicales
#     stream = music21.converter.subConverters.ConverterMEI(filepath)
#     notes = stream.flat.notes
#     output_file = 'notas.txt'
#     with open(output_file, 'w') as f:
#         for note in notes:
#             f.write(str(note.pitch) + ' ' + str(note.offsetSeconds) + '\n')

# def extractVoice(file):
#     return 0

def play_note(freq, duration):
    p = pyaudio.PyAudio()

    # Definir los parámetros del sonido
    volume = 0.5
    sampling_rate = 44100

    # Crear un array con los valores del sonido
    t = np.linspace(0, duration, int(duration * sampling_rate), False)
    note = volume * np.sin(freq * 2 * np.pi * t)

    # Crear un stream para reproducir el sonido
    stream = p.open(format=pyaudio.paFloat32, channels=1, rate=sampling_rate, output=True)

    # Reproducir el sonido
    stream.write(note.astype(np.float32).tobytes())

    # Detener y cerrar el stream
    stream.stop_stream()
    stream.close()
    p.terminate()

# Ejemplo de uso
# play_note(440, 1) # Generar la nota La 440 durante 1 segundo

# leerFichero()
reconocedorDeNotasAure()
leerFichero()