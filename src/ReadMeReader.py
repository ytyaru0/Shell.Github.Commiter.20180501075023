import pathilb
# descriptionを取得する。
class ReadMeReader:
    def __init__(self, path):
        self.__path_dir_this = pathlib.Path(__file__).parent
        self.__filename = 'ReadMe.md'
        self.__readme = self.__path_dir_this / self.__filename
        self.__desc = None
        self.__LoadDescription()
    
    @property
    def Description(self): return self.__desc

    def __LoadDescription(self):
        if not self.__readme.is_file(): raise Exception('{}ファイルが存在しません。: {}'.format(self.__filename, self.__readme))
        with self.__readme.open() as f:
            f.readline()
            while line:
                l = line.strip()
                if 0 == len(l) or l.startswith('#'): continue
                self.__desc = l
                return
