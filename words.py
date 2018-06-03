class Words:
    def __init__(self, _word, _part):
        self.word = _word
        self.part = _part
    
    def add_modifier(self):
        raise Exception("add_modifier is undifined.")

class Nouns(Words):
    def __init__(self, word, part):
        super().__init__(word, part)
    
    def next_particle(self): # 次の助詞を制限する
        if self.part == "person":
            return ["の","が","に","へ","と","、"]
        elif self.part == "place":
            return ["の","で","を","が","に","へ","と","から","、"]
        elif self.part == "food":
            return ["で","を","が","に","へ","と","、"]
        else:
            return ["の","で","を","が","に","へ","と","、"]
    
    def add_modifier(self): # 修飾語をつける
        pass