class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

lyrics = ["ths is a song for the broken hearted", "no silent prayer for faith departed"]

happy_bday = Song (["Happy birthday to you", "I dont want to get sued",
                    "So I'll stop right there"])

bulls_on_parade = Song(["They rally around the family",
                        "With Pockets full of shells"])

happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()
new_song = Song(lyrics)
new_song.sing_me_a_song()
