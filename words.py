class Nouns:
    def __init__(self, word, part):
        self.__word = word
        self.__part = part
    
    def to_str(self):
        return self.__word
    
    def next_particle(self): # 次の助詞を制限する
        if self.__part == "person":
            return ["の","が","に","へ","と","、"]
        elif self.__part == "place":
            return ["の","で","を","が","に","へ","と","、"]
        elif self.__part == "food":
            return ["で","を","が","に","へ","と","、"]
        else:
            return ["の","で","を","が","に","へ","と","、"]