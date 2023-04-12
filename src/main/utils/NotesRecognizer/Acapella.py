import wave
import numpy as np
from scipy.signal import butter, lfilter


def separarAudio(input_file, output_dir):

      # Frecuencia de muestreo
   Fs = 44100

   # Frecuencia de corte para el filtro pasa-banda
   lowcut = 300
   highcut = 3000

   # Orden del filtro
   order = 2

   # Coeficientes del filtro
   def butter_bandpass(lowcut, highcut, fs, order=5):
      nyq = 0.5 * fs
      low = lowcut / nyq
      high = highcut / nyq
      b, a = butter(order, [low, high], btype='band')
      return b, a

   # Lectura del archivo de audio
   audio = wave.open("src/main/utils/NotesRecognizer/lion.wav", 'rb')

   # Obtención de los datos del audio
   nframes = audio.getnframes()
   data = audio.readframes(nframes)

   # Conversión de los datos del audio a un array numpy
   audio_array = np.frombuffer(data, dtype=np.int16)

   # Aplicación del filtro pasa-banda para separar la voz de la música
   b, a = butter_bandpass(lowcut, highcut, Fs, order=order)
   voice_array = lfilter(b, a, audio_array)

   # Creación de los archivos de salida
   voice_wave = wave.open('src/main/utils/NotesRecognizer/aaaaaaa.wav', 'w')
   voice_wave.setnchannels(1)
   voice_wave.setsampwidth(audio.getsampwidth())
   voice_wave.setframerate(audio.getframerate())
   voice_wave.writeframes(voice_array)

   music_array = audio_array - voice_array
   music_wave = wave.open('src/main/utils/NotesRecognizer/aaaaaae.wav', 'w')
   music_wave.setnchannels(1)
   music_wave.setsampwidth(audio.getsampwidth())
   music_wave.setframerate(audio.getframerate())
   music_wave.writeframes(music_array)

   # Cierre de los archivos
   audio.close()
   voice_wave.close()
   music_wave.close()
