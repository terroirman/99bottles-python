class Bottles(object):

    plural: dict = {
        0: "",
        1: ""
    }

    def verse(self, verse_num: int):
        return Bottles.phrase1(verse_num) + '\n' + Bottles.phrase2(verse_num-1)

    @staticmethod
    def phrase1(bottle_num: int):
        s = Bottles.plural.get(bottle_num, 's')
        return f"{bottle_num} bottle{s} of beer on the wall, {bottle_num} bottle{s} of beer."

    @staticmethod
    def phrase2(bottle_num: int):
        s = Bottles.plural.get(bottle_num, 's')
        return f"Take one down and pass it around, {bottle_num} bottle{s} of beer on the wall."
