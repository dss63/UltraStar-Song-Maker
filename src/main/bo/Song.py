from utils.Reader.FileReader import FileReader
from utils.Reader.LyricsReader import LyricsReader
from utils.Reader.SongReader import SongReader
from utils.Reader.VideoReader import VideoReader
from pathlib import Path

class Song:

    def __init__(self, path):
        self.song = SongReader.readFile(Path.joinpath(path, "song.mp3"))
        self.lyrics = LyricsReader().readFile(Path.joinpath(path, "lyrics.txt"))
        self.video = None
        