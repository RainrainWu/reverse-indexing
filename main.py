from analyzer.tokenizer import Tokenizer
from analyzer.filter import Filter

t = Tokenizer()
f = Filter()

if __name__ == '__main__':
    t.load(u'Good bye in Swedish is Hej d\xe5').tokenize_by_blank()
    f.load(t.extract()).filter_lower()
    f.filter_ascii()
    print(f.extract())