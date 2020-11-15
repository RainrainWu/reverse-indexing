class Tokenizer:

    def __init__(self):
        self.digest = None
        self.stream = None

    def load(self, text):
        self.digest = text
        return self

    def extract(self):
        return self.stream

    def tokenize_by_blank(self):
        try:
            self.stream = self.digest.split(" ")
        except AttributeError:
            print("digest {DIGEST} are not tokenizable!".format(DIGEST=self.digest))

    def tokenize_by_comma(self):
        try:
            self.stream = self.digest.split(",")
        except AttributeError:
            print("digest {DIGEST} are not tokenizable!".format(DIGEST=self.digest))