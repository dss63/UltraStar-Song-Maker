import numpy as np
import librosa
# from librosa.core import hz_to_noteName
from pathlib import Path
# import music21
# from pydub import AudioSegment
# from pydub.playback import play

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


recognizeNotes()