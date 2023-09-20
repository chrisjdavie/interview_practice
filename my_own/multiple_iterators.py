from itertools import chain

def iter_thing():

    word = "ABCDEFGH"

    word_m2 = chain("^", "^", word)
    word_m1 = chain("^", word)
    word_p1 = chain(word, "$")
    next(word_p1)

    yield from zip(word_m2, word_m1, word, word_p1)

for a, b, c, d in iter_thing():
    print(a, b, c, d)
