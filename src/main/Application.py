# Application developed by Aurelio Ortiz de Salazar Peris
# Copyright de mis huevos
# Contact: aure.ortizperis@gmail.com

import sys
from bo.Song import Song
from utils.Reader.LyricsReader import LyricsReader
from utils.Reader.LyricsReader import FileReader
from utils.NotesRecognizer import NotesRecognizer
from pathlib import Path

if __name__ == '__main__':
    # filename = Path("/home/aureortiz/Projects/USSM/src/resources/songs/personalidad")

    # STEP 1: LOAD FILES (SONG, LYRICS, VIDEO)
    # lyrics = LyricsReader().readFile(Path.joinpath(filename, "lyrics.txt"))
    
    # STEP 2: EXTRACT MUSICAL NOTES FROM SONG
    notes = NotesRecognizer.reconocedorDeNotasAure()
    notes = NotesRecognizer.leerFichero()

    # STEP 3: ARRANGE FILE TO BE INCLUDED IN ULTRASTAR
    # cancion = Song(filename)

    # Llamamos al .txt
    # FileReader.submit_form()