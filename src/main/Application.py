# Application developed by
# Copyright 
# Contact:

import sys
from utils.Reader import FileReader
from utils.NotesRecognizer import NotesRecognizer
from pathlib import Path

if __name__ == '__main__':

    # FL = FileReader.submit_form()

    # Instancia de la clase
    NT = NotesRecognizer.NotesUtils()

    # Reconocer notas y guardarlas en fichero
    NT.reconocerNotas("src/main/utils/NotesRecognizer/alarma.mp3")
    NT. reconocerTempo("src/main/utils/NotesRecognizer/alarma.mp3")
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

    