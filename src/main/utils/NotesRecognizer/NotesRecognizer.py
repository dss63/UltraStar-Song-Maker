import numpy as np
import librosa
from pathlib import Path


def recognizeNotes(file):

    extractVoice(file)

    filepath = Path("/home/aureortiz/Projects/USSM/src/resources/songs/personalidad/output/song/vocals.wav")

    y, sr = librosa.load(filepath)
    print(y)
    print(sr)
    pitches, magnitudes = librosa.piptrack(y, sr=sr)
    notes = []
    for i in range(pitches.shape[0]):
        curr_pitch = pitches[i]
        curr_magnitude = magnitudes[i].max()
        note = librosa.hz_to_note(curr_pitch, octave=False, cents=True)
        if curr_magnitude > 0.5:
            notes.append(note)
    return notes

def extractVoice(file):
    return 0