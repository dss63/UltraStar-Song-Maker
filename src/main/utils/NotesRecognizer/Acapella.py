import os
from spleeter.separator import Separator


def separarAudio(input_file, output_dir):

   # Cargar el modelo pre entrenado de separación de audio
   separator = Separator('spleeter:2stems')

   # Separar el audio en dos y colocarlos en la dirección output
   separator.separate_to_file(input_file, output_dir, codec='wav')


   # Mover archivo vocal.wav al directorio "vocals"
   os.rename(os.path.join(output_dir+"alarma2", "vocals.wav"), os.path.join(output_dir, "solovoz.wav"))
   os.rename(os.path.join(output_dir+"alarma2", "accompaniment.wav"), os.path.join(output_dir, "solomusica.wav"))

   try:
      os.rmdir(output_dir+"alarma2")
   except OSError as error:
      print(f"Ocurrió un error al eliminar la carpeta: {error}")