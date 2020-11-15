import pytest

from cache.handler import CacheHandler


def test_apply_and_search():

    files = ["file one", "file two", "file three"]
    cache_handler = CacheHandler()
    cache_handler.index_conn.flushdb()
    cache_handler.file_conn.flushdb()

    cache_handler.apply(files[0], files[0].split(" "))
    cache_handler.apply(files[1], files[1].split(" "))
    cache_handler.apply(files[2], files[2].split(" "))

    assert cache_handler.search("file") == files
    assert cache_handler.search("two") == files[1:2]

    cache_handler.index_conn.flushdb()
    cache_handler.file_conn.flushdb()

    assert cache_handler.search("file") == []
