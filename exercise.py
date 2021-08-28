class Bottles(object):
    def verse(self, verse_num: int):
        return (
            f"{verse_num} bottles of beer on the wall, {verse_num} bottles of beer.\n"
            f"Take one down and pass it around, {verse_num-1} bottles of beer on the wall."
        )

    def phrase(self, bottle_num: int, phrase: str):
        return None