
class FileReader:
    def __init__(self) -> None:
        pass

    def readFile(self, path):
        f = open(path, "r")
        return f.readlines()