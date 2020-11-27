from cache.handler import CacheHandler

class Rater:

    target = None
    candidates = None
    cache_handler = CacheHandler()

    def __init__(self):
        pass

    def load(self, target, candidates):
        self.target = target
        self.candidates = candidates
        return self

    def extract(self):
        return self.candidates

    def limit_by_density(self, size):
        buffer = {}
        for c in self.candidates:
            tokens = self.cache_handler.fetch_tokens(c)
            buffer[c.decode("utf-8")] = tokens.count(self.target) / len(tokens)
        
        result = sorted(buffer.items(), key=lambda item: item[1])
        result = [x[0] for x in result]
        if len(result) > size:
            result = result[:size]
        self.candidates = result
        return self