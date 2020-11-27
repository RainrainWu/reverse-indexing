import redis


class CacheHandler:

    def __init__(self):
        self.file_counter = 0
        self.file_conn = redis.Redis(host="localhost", port=6379, db=0)
        self.token_conn = redis.Redis(host="localhost", port=6379, db=1)
        self.index_conn = redis.Redis(host="localhost", port=6379, db=2)

    def apply(self, text, stream):
        counter = str(self.file_counter)
        self.file_conn.set(counter, text)
        
        pipe = self.token_conn.pipeline()
        for s in stream:
            pipe.rpush(counter, s)
        pipe.execute()

        pipe = self.index_conn.pipeline()
        for s in stream:
            pipe.lrem(s, 2, counter)
            pipe.rpush(s, counter)
        pipe.execute()

        self.file_counter += 1


    def search(self, token):
        files = self.index_conn.lrange(token, 0, -1)
        return files


    def fetch_tokens(self, counter):
        tokens = self.token_conn.lrange(counter, 0, -1)
        return tokens

    
    def fetch_files(self, counters):
        pipe = self.file_conn.pipeline()
        for c in counters:
            pipe.get(c)
        return [x.decode("utf-8") for x in pipe.execute()]