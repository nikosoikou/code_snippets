class Sentence:
    def __init__(self, sentence):
        self.sentence = sentence
        self.words = self.sentence.split()
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.words):
            raise StopIteration
        index = self.index
        self.index += 1
        return self.words[index]


def sentence(sentence):
    for word in sentence.split():
        yield word


my_sentences = sentence('This is a test')

for word in my_sentences:
    print(word)

print()

my_sentences = Sentence('This is a test')

for word in my_sentences:
    print(word)

# This should have the following output:
# This
# is
# a
# test
