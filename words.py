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
    
    # def next_particle(self): # 次の助詞を制限する
    #     if self.part == "person":
    #         return ["の","が","に","へ","と","、"]
    #     elif self.part == "place":
    #         return ["の","で","を","が","に","へ","と","から","、"]
    #     elif self.part == "food":
    #         return ["で","を","が","に","へ","と","、"]
    #     else:
    #         return ["の","で","を","が","に","へ","と","、"]
    
    def word_with_modifier(self, nouns, modi):
        return self.add_modifier(nouns, modi, self.word, 0.2)

    def add_modifier(self, nouns, modi, word, per): # 修飾語をつける
        r  = random.random()
        if r < per:
            w = random.choice(modi) + word
        elif r < per * 1.7:
            w = random.choice(nouns).word + "の" + word
        elif r < per * 2:
            w = random.choice(nouns).word + "と" + word
        else:
            return word
        return self.add_modifier(nouns, modi, w, per)

# もう少し単語を細かく分類してより精度を上げていきたい（希望的観測）