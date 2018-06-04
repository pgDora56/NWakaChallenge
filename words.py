import random

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
    
    def add_modifier(self, nouns, modi): # 修飾語をつける
    # 実行確認してない
        r  = random.random()
        if r < 0.3:
            return random.choice(modi) + self.word
        elif r < 0.6:
            return random.choice(nouns) + "の" + self.word