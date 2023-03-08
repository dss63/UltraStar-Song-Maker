    
from tkinter import *
from tkinter import filedialog
import shutil

class FileReader:
    
    def __init__(self) -> None:
        pass

    def readFile(self, path):
        f = open(path, "r")
        return f.readlines()


    # def save_file():
    #     file_path = file_path_text.get()
    #     file_name = os.path.basename(file_path)
    #     shutil.copyfile(file_path, os.path.join('archivos', file_name))


    def submit_form():
        title = title_entry.get()
        artist = artist_entry.get()
        language = language_entry.get()
        genre = genre_entry.get()
        year = year_entry.get()
        image = image_entry.get()
        video = video_entry.get()

        # Guardar los datos en un archivo de texto
        with open("datos.txt", "w") as f:
            f.write("#TITLE:" + title + "\n")
            f.write("#ARTIST:" + artist + "\n")
            f.write("#LANGUAGE:" + language + "\n")
            f.write("#GENRE:" + genre + "\n")
            f.write("#YEAR:" + year + "\n")
            f.write("#CREATOR:Daniel Santoyo \n")

            f.write("#MP3: --- PONER EL NOMBRE DEL ARCHIVO DE LA CANCION ---\n")

            f.write("#COVER:" + image + "\n")
            f.write("#VIDEO:" + video + "\n")

            f.write("#VIDEOGAP: --- PONER VIDEOGAP --- \n")
            f.write("#BPM: --- PON EL BEAT POR MINUTO DE LA CANCION --- \n")
            f.write("#GAP: --- PON EL GAP DE LA CANCION --- \n")

            #START
            #END
            #VIDEOGAP
            #BPM
            #GAP
            #MEDLEYSTARTBEAT
            #MEDLEYENDBEAT

            #NOTAS Y DE MAS MOVIDAS

        # Crear ventana principal
        root = Tk()

        # Crear campos de entrada para el formulario
        title_label = Label(root, text="Título:")
        title_entry = Entry(root)

        artist_label = Label(root, text="Artista:")
        artist_entry = Entry(root)

        language_label = Label(root, text="Lenguaje:")
        language_entry = Entry(root)

        genre_label = Label(root, text="Género:")
        genre_entry = Entry(root)

        year_label = Label(root, text="Año:")
        year_entry = Entry(root)

        image_label = Label(root, text="Imagen:")
        image_entry = Entry(root)

        video_label = Label(root, text="Video:")
        video_entry = Entry(root)

        #Recoger el audio
        file_path = filedialog.askopenfilename(initialdir = "/", title = "Selecciona la canción", filetypes = [("Audio Files", "*.mp3")])
        file_path_text = StringVar()
        file_path_text.set(file_path)
        file_path_label = Label(root, textvariable = file_path_text)
        # file_path_label.pack()

        # Crear botón para enviar el formulario
        submit_button = Button(root, text="Enviar", command=submit_form)

        # Acomodar los campos en la ventana
        title_label.grid(row=0, column=0)
        title_entry.grid(row=0, column=1)

        artist_label.grid(row=1, column=0)
        artist_entry.grid(row=1, column=1)

        language_label.grid(row=2, column=0)
        language_entry.grid(row=2, column=1)

        genre_label.grid(row=3, column=0)
        genre_entry.grid(row=3, column=1)

        year_label.grid(row=4, column=0)
        year_entry.grid(row=4, column=1)

        image_label.grid(row=5, column=0)
        image_entry.grid(row=5, column=1)

        video_label.grid(row=6, column=0)
        video_entry.grid(row=6, column=1)


        submit_button.grid(row=7, column=1)



    submit_form()

        # root.mainloop()

# Ejecutar la ventana principal


