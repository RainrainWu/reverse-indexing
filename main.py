from analyzer.tokenizer import Tokenizer
from analyzer.filter import Filter
from cache.handler import CacheHandler


t = Tokenizer()
f = Filter()
c = CacheHandler()

if __name__ == '__main__':
    t.load(u'Good bye in Swedish is Hej d\xe5').tokenize_by_blank()
    f.load(t.extract()).filter_lower()
    f.filter_ascii()
    print(f.extract())

    c.apply("file one", ["file", "one"])
    c.apply("file two", ["file", "two"])
    c.apply("file three", ["file", "three"])
    print(c.search("file"))
    print(c.search("two"))
