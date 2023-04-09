# Application developed by Daniel Santoyo Sirvent
# Copyright 
# Contact: @dsantoyoo

import sys
# from utils.Reader import FileReader
from utils.NotesRecognizer import NotesRecognizer
from utils.NotesRecognizer import Acapella

from pathlib import Path
#Importar clase a capela

if __name__ == '__main__':

    #Instancia de la clase

    #Crear el fichero y abrir formulario de información que debe otorgar el usuario

    #Crear audio vocal e instrumental

    #Enviar ambos audios a la clase de reconocer notas donde acaba el proceso completo


    # FL = FileReader.submit_form()

    # Instancia de la clase
    NT = NotesRecognizer.NotesUtils()
    NA = Acapella

    #Crear audio vocal e instrumental
    NA.separarAudio("src/main/utils/NotesRecognizer/alarma2.mp3")

    # Reconocer notas y guardarlas en fichero
    NT.reconocerNotas("src/main/utils/NotesRecognizer/solovoz.wav")
    NT. reconocerTempo("src/main/utils/NotesRecognizer/solomusica.wav")
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

    