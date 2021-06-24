class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
    global listeners = set()
    def how_many(self, people):
        global listeners
        for p in people:
            if p.lower() in listeners:
                print('exists')
            else:
                listeners.add(p.lower())
        return len(listeners)

test = Song("hi", 'bye')
test.how_many('John')
test.how_many('john')