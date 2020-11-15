import redis


class CacheHandler:

    def __init__(self):
        self.file_counter = 0
        self.index_conn = redis.Redis(host="localhost", port=6379, db=0)
        self.file_conn = redis.Redis(host="localhost", port=6379, db=1)

    def apply(self, text, stream):
        self.file_conn.set(str(self.file_counter), text)

        pipe = self.index_conn.pipeline()
        for s in stream:
            pipe.lrem(s, 2, str(self.file_counter))
            pipe.rpush(s, str(self.file_counter))
        pipe.execute()

        self.file_counter += 1

    def search(self, token):
        files = self.index_conn.lrange(token, 0, -1)
        pipe = self.file_conn.pipeline()
        for f in files:
            pipe.get(f)
        return pipe.execute()
