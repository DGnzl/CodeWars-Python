class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
        self.listeners = set()
    
    def how_many(self, people):
        count = 0
        for p in people:
            if p.lower() not in self.listeners:
                self.listeners.add(p.lower())
                count += 1
        return count

test = Song('hi', 'bye')
test.how_many(['John'])
test.how_many(['Sandra'])
test.how_many(['John'])