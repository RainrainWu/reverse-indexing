class Filter:

    stream = None

    def __init__(self):
        pass

    def load(self, tokens):
        self.stream = tokens
        return self

    def extract(self):
        return self.stream

    def filter_lower(self):
        self.stream = [
            i.lower()
            for i in self.stream
        ]
        return self

    def filter_upper(self):
        self.stream = [
            i.upper()
            for i in self.stream
        ]
        return self

    def filter_ascii(self):
        self.stream = [
            i.encode("ascii", errors="ignore").decode()
            for i in self.stream
        ]
        return self
