

from tkinter import *
import numpy as np

class Formulario:

    def submit_form(self):
        title = self.title_entry.get()
        artist = self.artist_entry.get()
        language = self.language_entry.get()
        genre = self.genre_entry.get()
        year = self.year_entry.get()
        image = self.image_entry.get()
        video = self.video_entry.get()
        audio = self.audio_entry.get()
        tempo = self.tempo
        gap = self.gap


        # Guardar los datos en un archivo de texto
        with open("datos.txt", "r+") as f:

            # Leemos los datos de las notas
            contenido = f.read()

            # Nos posicionamos en el incio del fichero
            f.seek(0)

            # Guardamos los datos del formulario
            f.write("#TITLE:" + title + "\n")
            f.write("#ARTIST:" + artist + "\n")
            f.write("#LANGUAGE:" + language + "\n")
            f.write("#GENRE:" + genre + "\n")
            f.write("#YEAR:" + year + "\n")
            f.write("#CREATOR:Daniel Santoyo \n")
            f.write("#MP3:" + audio + "\n")
            f.write("#COVER:" + image + "\n")
            f.write("#VIDEO:" + video + "\n")

            # Guardamos el tempo y el gap pasándolos a String
            f.write("#BPM:" + str(round(tempo, 2)) + "\n")
            f.write("#GAP:" + str(round(gap, 2)) + "\n")

            # Escribimos la información de las notas
            f.write(contenido)

            # Cerramos la ventana de la interfaz con el formulario
            self.root.destroy()


    def ejecutar(self,tempo,gap):
        self.tempo=tempo
        self.gap=gap

        # Crear ventana principal
        self.root = Tk()
        self.root.title("StarMaker")
        self.root.geometry("400x400")

        # Crear el título de la ventana
        self.titulo = Label(self.root, text="StarMaker", font=("Arial", 24), pady=20)
        self.titulo.grid(row=0, column=1)

        # Crear campos de entrada para el formulario
        self.title_label = Label(self.root, text="Título:")
        self.title_entry = Entry(self.root)

        self.artist_label = Label(self.root, text="Artista:")
        self.artist_entry = Entry(self.root)

        self.language_label = Label(self.root, text="Lenguaje:")
        self.language_entry = Entry(self.root)

        self.genre_label = Label(self.root, text="Género:")
        self.genre_entry = Entry(self.root)

        self.year_label = Label(self.root, text="Año:")
        self.year_entry = Entry(self.root)

        self.audio_label = Label(self.root, text="Audio:")
        self.audio_entry = Entry(self.root)


        self.image_label = Label(self.root, text="Imagen:")
        self.image_entry = Entry(self.root)

        self.video_label = Label(self.root, text="Video:")
        self.video_entry = Entry(self.root)


        #vector = np.array([root, title_entry.get(), artist_entry.get(), language_entry.get(), genre_entry.get(), year_entry.get(), image_entry.get(), video_entry.get(), tempo, gap])

        # Crear botón para enviar el formulario
        self.submit_button = Button(self.root, text="Enviar", command=self.submit_form)

        # Acomodar los campos en la ventana
        self.title_label.grid(row=1, column=0)
        self.title_entry.grid(row=1, column=1)

        self.artist_label.grid(row=2, column=0)
        self.artist_entry.grid(row=2, column=1)

        self.language_label.grid(row=3, column=0)
        self.language_entry.grid(row=3, column=1)

        self.genre_label.grid(row=4, column=0)
        self.genre_entry.grid(row=4, column=1)

        self.year_label.grid(row=5, column=0)
        self.year_entry.grid(row=5, column=1)

        self.audio_label.grid(row=6, column=0)
        self.audio_entry.grid(row=6, column=1)

        self.image_label.grid(row=7, column=0)
        self.image_entry.grid(row=7, column=1)

        self.video_label.grid(row=8, column=0)
        self.video_entry.grid(row=8, column=1)

        self.submit_button.grid(row=9, column=1)

        # Ejecutar la ventana principal
        self.root.mainloop()
