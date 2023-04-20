# Application developed by Daniel Santoyo Sirvent
# Copyright TFG StarMaker
# Contact: @dsantoyoo

# Importar clase del fichero y el formulario
from utils.Reader import FileReader

# Importar clase de Reconocer Notas
from utils.NotesRecognizer import NotesRecognizer

#Importar clase a capela
from utils.NotesRecognizer import Acapella


if __name__ == '__main__':

    # Instancia de la clase
    NT = NotesRecognizer.NotesUtils()
    NA = Acapella

    # Crear audio vocal e instrumental
    NA.separarAudio("src/main/utils/NotesRecognizer/cancion.mp3","src/main/utils/NotesRecognizer/")

    # Reconocer notas y guardarlas en fichero
    NT.reconocerNotas("src/main/utils/NotesRecognizer/solovoz.wav")
    NT. reconocerTempo("src/main/utils/NotesRecognizer/musica.wav")

    # Leemos el fichero que contiene las frecuencias
    freqList = NT.leerFichero()

    # Ploteamos la grafica sin filtro
    ax = NT.plotFrequency(freqList, True, None)

    # Filtro de suavizado y eliminación de ruido
    freqProcesada = NT.procesamientoDeFrecuencia(freqList, 50, True)

    # Ploteamos la grafica con filtro
    figure = NT.plotFrequency(freqProcesada, True, None)

    # Creacion del vector notas sin escala para el fichero
    NT.notasFicheroBeats(freqProcesada, NT.tempo)

    # Abrimos formulario y añadimos la información al fichero
    NF = FileReader.Formulario().ejecutar(NT.tempo, NT.gap)







    # try:
    #     os.remove("src/main/utils/NotesRecognizer/solovoz.wav")
    #     os.remove("src/main/utils/NotesRecognizer/solomusica.wav")
    # except OSError as error:
    #     print(f"Ocurrió un error al eliminar la carpeta: {error}")