import audio_to_midi

class NotesUtils: 

    def midi():
        audio_file = 'song.mp3'
        midi_file = 'song.mid'
        audio_to_midi.audio_to_midi(audio_file, midi_file)


if __name__ == '__main__':

    # Instancia de la clase
    NT = NotesUtils()

    # Reconocer notas y guardarlas en fichero
    NT.midi("src/main/utils/NotesRecognizer/pruebaKiss.mp3")
    # Leo el fichero que contiene las frecuencias
    # freqList = NT.leerFichero()

    # # Ploteo la grafica sin filtro
    # #ax = NT.plotFrequency(freqList, True, None)

    # # Filtro
    # freqProcesada = NT.procesamientoDeFrecuencia(freqList, 70, False)

    # # Ploteo la grafica con filtro
    # figure = NT.plotFrequency(freqProcesada, True, None)

    # Creacion del vector notas sin escala para el fichero
    #NT.notasFichero(freqProcesada)

    # NT.notasFicheroBeats(freqProcesada, NT.tempo)
    # print("TEMPO ", NT.tempo)

    
