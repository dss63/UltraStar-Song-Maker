import os
from spleeter.separator import Separator


def separarAudio(input_file, output_dir):

   # Load the pre-trained spleeter model
   separator = Separator('spleeter:2stems')

   # Separate the vocals and instrumental from the input audio file
   separator.separate_to_file(input_file, output_dir, codec='wav')


   # Mover archivo vocal.wav al directorio "vocals"
   os.rename(os.path.join(output_dir+"alarma2", "vocals.wav"), os.path.join(output_dir, "solovoz.wav"))
   os.rename(os.path.join(output_dir+"alarma2", "accompaniment.wav"), os.path.join(output_dir, "solomusica.wav"))

   try:
      os.rmdir(output_dir+"alarma2")
   except OSError as error:
      print(f"Ocurrió un error al eliminar la carpeta: {error}")