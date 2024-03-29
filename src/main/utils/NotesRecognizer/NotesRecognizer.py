
import numpy as np
import librosa
# from librosa.core import hz_to_noteName
from pathlib import Path
from glob import glob
import pyaudio


import matplotlib.pyplot as plt



import sys
import scipy.signal as sig
from scipy.io import wavfile

# import music21
# from pydub import AudioSegment
# from pydub.playback import play


# Notas y su frecuencia
# A0: A (La) de la escala 0
# A4: A (La) de la escala 4, es el la de 440 Hz
# Sharp: Sostenido
# Flat: bemol

class NotesUtils: 

    # Diccionario que contiene la frecuencia de cada nota CON escala
    notes = {'nan': 0,
            'A0': 27.5, 
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
            'C8': 4186.01 }

    # Diccionario que contiene la frecuencia de cada nota SIN escala
    # C = 1
    notes2 ={ 
        'nan':[0],
        1:[32.7,65.41,130.81,261.63,523.25,1046.5,2093.0,4186.01],
        2:[34.65,69.3,138.59,277.18,554.37,1108.73,2217.46],
        3:[36.71,73.42,146.83,293.66,587.33,1174.66,2349.32],
        4:[38.89,77.78,155.56,311.13,622.25,1244.51,2489.02],
        5:[41.2,82.41,164.81,329.63,659.26,1318.51,2637.02],
        6:[43.65,87.31,174.61,349.23,698.46,1396.91,2793.83],
        7:[46.25,92.5,185.0,369.99,739.99,1479.98,2859.96],
        8:[49.0,98.0,196.0,392.0,783.99,1567.98,3135.96],
        9:[51.91,103.83,207.65,415.3,830.61,1661.22,3322.44],
        10:[27.5,55.0,110.0,220.0,440.0,880.0,1760.0,3520.0],
        11:[29.14,58.27,116.54,233.08,466.16,932.33,1864.66,3729.31],
        12:[30.87,61.74,123.47,246.94,493.88,987.77,1975.53,3951.07]
    }

    # Sample rate para la detección de notas
    sr = 44100
    tempo = 0
    duracion = 0
    gap = 0

    def __init__(self) -> None:
        pass

    # NOTAS CON ESCALAS
    def getNote(self, freq):
        for key, value in self.notes.items():
            if freq == value:
                return key
    
    def getFreq(self, note):
        return self.notes.get(note)

   # NOTAS SIN ESCALA
    def getNote2(self, freq):
        for key, value in self.notes2.items():
            for i in value:
                if freq == i:
                    return key
    
    def getFreq2(self, note):
        return self.notes2.get(note)


    # Función que devuelve la nota más cercana a una frecuencia dada
    def getNearestFrequencyNote(self, f):
        anterior = self.notes['A#0']

        for key in self.notes.keys():
            value = self.notes[key]
            if value > f:
                rightFreq = value
                rightNote = key
                leftFreq = self.notes[anterior]
                leftNote = anterior
                break
            anterior = key
        
        result1 = f - leftFreq
        result2 = rightFreq - f

        note = rightNote
        freq = rightFreq
        if result1 < result2:
            note = leftNote
            freq = leftFreq
        
        return note, freq

    def reconocerTempo(self, path):
        pista = glob(path)
        y, sampleRate = librosa.load(pista[0], sr=self.sr)
        self.tempo, beats = librosa.beat.beat_track(y=y,sr=self.sr)


    # Función que se encarga de extraer las notas de un archivo de audio y escribirlas en "fichero.txt"
    def reconocerNotas(self, path):
        pista = glob(path)
    
        # Load
        y, sampleRate = librosa.load(pista[0], sr=self.sr)

        # Detección de las frecuencias
        f0, voiced_flag, voiced_probs = librosa.pyin(y, fmin=librosa.note_to_hz('C2'), fmax=librosa.note_to_hz('C7'))
        
        # Detección de la duración del audio
        self.duracion = librosa.get_duration(y=y, sr=self.sr)

        # Llamamos al método escribir fichero de las frecuencias
        self.escribirFichero(f0)

    # Función que se encarga de escribir el "fichero.txt" con las frecuencias
    def escribirFichero(self, f0):
        f = open("src/main/utils/NotesRecognizer/fichero.txt", 'w')
        for line in f0:
            # if not np.isnan(line):
            f.write(str(line) + "\n")
           

    # Función que lee "fichero.txt" y devuelve un vector con su contenido
    def leerFichero(self):
        f = open("src/main/utils/NotesRecognizer/fichero.txt", 'r')
        lines = f.readlines()

        notesVector = []
        freqVector = []

        for line in lines:
            if line.find("nan") == -1:
                data = float(line)
                note, freq = self.getNearestFrequencyNote(data)
                notesVector.append(note)
                freqVector.append(freq)
            else:
                notesVector.append("nan")
                freqVector.append(0)

        return freqVector

    # Prueba de sonido
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

    # Función que se encarga de plotear la frecuencia
    def plotFrequency(self, freq, plot, ax):
        
        noFig = False
        if ax == None:
            fig, ax = plt.subplots()
            noFig = True
    

        vx = np.linspace(0, len(freq), len(freq))
        ax.plot(vx, freq, linestyle='-', linewidth=1)

        # Configurar título y etiquetas de los ejes
        plt.suptitle('Análisis frecuencial')
        plt.xlabel('Tiempo')
        plt.ylabel('Frecuencias')
        plt.grid(True)

        # Configurar tamaño de fuente
        plt.tick_params(labelsize=10)

        # Para dar nombre a los labels, necesito saber cual es la frecuencia minima y maxima  
        # Sabiendo esto puedo definir los limites de mi eje Y dos por encima/debajo de mi maximo/minimo
        minNote, minFreq = self.getNearestFrequencyNote(min(freq))
        maxNote, maxFreq = self.getNearestFrequencyNote(max(freq))

        empezarVector = False
        yLabels = []
        yHz = []
        for key, value in self.notes.items():
            if value == minFreq:
                empezarVector = True
            if value > maxFreq:
                empezarVector = False
            if empezarVector: 
                if value not in yHz:
                    yLabels.append(key)
                    yHz.append(value)

        if noFig == True:
            ax.set_yticklabels(yLabels)
            ax.set_yticks(yHz)

        if plot:
            plt.show()

        return ax

    # Función procesa la señal
    def procesamientoDeFrecuencia(self, freqVector, muestreo, envolvente): # Envolvente
        # Envolvente. Para cada valor del vector, se cogen samplingRate/5 
        # elementos por la izquierda y por la derecha y se hace la media
        
        if envolvente:
            tam = int(muestreo/5)
            suavizado = []
            for i in range(len(freqVector)):
                if i < tam/2 + 1 or i > len(freqVector)- tam/2 - 1:
                    if i < tam/2 + 1:
                        avg = sum(freqVector[i : int(i+tam/2)])/tam
                    else:
                        avg = sum(freqVector[int(i-tam/2) : i])/tam
                else:
                    avg = sum(freqVector[int(i-tam/2) : int(i+tam/2)])/tam
                suavizado.append(avg)

            # Busco para cada valor de la freq suavizada su freq más cercana
            for i in range(len(suavizado)):
                note, freq = self.getNearestFrequencyNote(suavizado[i])
                suavizado[i] = freq

        return self.eliminarMinRate(10, freqVector)

    def eliminarMinRate(self, rate, suavizado):
        # Elimino las frecuencias que duren menos de 5 iteraciones
        minCantidad = rate
        ultimaNota = suavizado[0]
        cantidad = 1
        for i in range(1, len(suavizado)-1):
            if suavizado[i] == suavizado[i+1]:
                cantidad += 1
            else:
                if cantidad < minCantidad:
                    suavizado = self.restablecerValoresAnteriores(suavizado, i, ultimaNota)
                else:
                    ultimaNota = suavizado[i - cantidad]
                cantidad = 0
        
        return suavizado

    def restablecerValoresAnteriores(self, suavizado, index, ultimaNota):
        while(suavizado[index] != ultimaNota):
            suavizado[index] = ultimaNota
            index -= 1
        return suavizado

    def notasFichero(self, freq):
        
        f = open("src/main/utils/NotesRecognizer/notas.txt", 'w')

        v = []
        instante = float(self.duracion / float(len(freq)))
        print(instante, self.duracion)
        tiempo = 0
        tiempoAnterior = 0
        keyAnterior = ""    

        index = 0
        for num in freq:
            key = self.getNote2(num)
            if key != keyAnterior :
                if key != "nan":
                    v.append([tiempo, 0, key]) # v = [tiempo, duracion, nota]
                    if (index > 0):
                        v[index - 1][1] = tiempo - tiempoAnterior
                    index += 1
                tiempoAnterior = tiempo
            tiempo += instante
            keyAnterior = key
        
        v[index - 1][1] = tiempo - tiempoAnterior

        # C C C B
        # V = [t,0,C]
        # V = [t,3i,C][t,i,B]

        for vec in v:
            vec[0] = int(vec[0] * 10)
            vec[1] = int(vec[1] * 10)
            f.write(": "+ str(vec[0]) + " " + str(vec[1]) + " " + str(vec[2]) + "\n")


    def notasFicheroBeats(self, freq, tempo):
        f = open("datos.txt", 'w')
    
        bps=tempo/60
        contadorSaltos = 0
        beatsTotales = bps*self.duracion

        v = []
        instante = float(self.duracion / float(len(freq)))
        # print(instante, self.duracion)
        tiempo = 0
        tiempoAnterior = 0
        keyAnterior = ""    
        intro=0
        index = 0
        
        
        for num in freq:
            key = self.getNote2(num)
            if index==2:
                intro=tiempo

            if key != keyAnterior :
                
                if key != "nan":
                    v.append([tiempo, 0, key]) # v = [tiempo, duracion, nota]
                    contadorSaltos = contadorSaltos + tiempo
                    if (index > 0):
                        v[index - 1][1] = tiempo - tiempoAnterior
                    index += 1
           
                tiempoAnterior = tiempo
            if index>1:
                tiempo += instante
            keyAnterior = key

            if contadorSaltos > 100:
                contadorSaltos = 0
                v.append([tiempo, -1, -1]) # v = [tiempo, duracion, nota]
        
        v[index - 1][1] = tiempo - tiempoAnterior
        v.pop(0)

        self.gap=intro*1000

        for x in v:
            if x[1] != -1:
                x[0] =(x[0] * beatsTotales)/(self.duracion)
                x[1] = x[1] * bps
            else:
                x[0] =(x[0] * beatsTotales)/(self.duracion)

        # C C C B
        # V = [t,0,C]
        # V = [t,3i,C][t,i,B]

        size = len(v)
        aux = 0
        anteriorDuracion = 0

        for vec in v:
            if aux == size-1 or vec[1]==0:
                f.write("E")
                return
            else:
                if vec[2] != -1:
                    vec[0] = int(vec[0] * 10)
                    vec[1] = int(vec[1] * 10)
                    anteriorDuracion = vec[1]
                    if str(vec[1]) != "0":
                        f.write(": "+ str(vec[0]) + " " + str(vec[1]) + " " + str(vec[2]) + "\n")

                else:
                    vec[0] = int(vec[0] * 10) + anteriorDuracion
                    f.write("- "+ str(vec[0])+"\n")

            aux = aux + 1


if __name__ == '__main__':

    # Instancia de la clase
    NT = NotesUtils()

    # Reconocer notas y guardarlas en fichero
    NT.reconocerNotas("src/main/utils/NotesRecognizer/alarma.mp3")
    NT. reconocerTempo("src/main/utils/NotesRecognizer/alarma2.mp3")
    # Leo el fichero que contiene las frecuencias
    freqList = NT.leerFichero()

    # Ploteo la grafica sin filtro
    #ax = NT.plotFrequency(freqList, True, None)

    # Filtro
    freqProcesada = NT.procesamientoDeFrecuencia(freqList, 70, False)

    # Ploteo la grafica con filtro
    figure = NT.plotFrequency(freqProcesada, True, None)

    # Creacion del vector notas sin escala para el fichero
    #NT.notasFichero(freqProcesada)

    NT.notasFicheroBeats(freqProcesada, NT.tempo)
    print("TEMPO ", NT.tempo)

    
