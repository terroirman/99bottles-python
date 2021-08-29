class Bottles(object):

    def song(self) -> str:
        return self.verses(99, 0)

    def verses(self, start_verse: int, stop_verse: int) -> str:
        start_verse, stop_verse = sorted([start_verse, stop_verse], reverse=True)
        verses = range(start_verse, stop_verse - 1, -1)
        return '\n\n'.join([self.verse(verse) for verse in verses])

    def verse(self, verse_num: int) -> str:
        return self.phrase1(verse_num) + '\n' + \
               self.phrase2(verse_num-1)

    def phrase1(self, bottle_num: int) -> str:
        s = {1: ''}.get(bottle_num, 's')
        phrase1: dict = {
            0: 'No more bottles of beer on the wall, no more bottles of beer.'
        }
        return phrase1.get(
            bottle_num,
            f'{bottle_num} bottle{s} of beer on the wall, {bottle_num} bottle{s} of beer.'
        )

    def phrase2(self, bottle_num: int) -> str:
        s = {1: ''}.get(bottle_num, 's')
        phrase2: dict = {
            0: 'Take it down and pass it around, no more bottles of beer on the wall.',
            -1: 'Go to the store and buy some more, 99 bottles of beer on the wall.'
        }
        return phrase2.get(
            bottle_num,
            f'Take one down and pass it around, {bottle_num} bottle{s} of beer on the wall.'
        )


if __name__ == '__main__':
    bottles = Bottles()
    print(bottles.verses(99, 98))
    print(bottles.song())
