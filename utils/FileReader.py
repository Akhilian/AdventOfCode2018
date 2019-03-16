class FileReader:
    @staticmethod
    def read(pathname):
        file_object = open(pathname, 'r')
        return list(map(lambda str: str.replace("\n", ""), file_object.readlines()))
