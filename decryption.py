import string
message = "012222 1114142503 0313012513 03141418192102 0113 2419182119021713 06131715070119"
keyed_alphabet = "BHISOECRTMGWYVALUZDNFJKPQX"
message = list(message)
caps = string.letters[26:]


indexes = []
for one in caps:
    i = keyed_alphabet.index(one)
    indexes.append(i)


def get_message():
    while message:
        one = message.pop(0)
        if one == ' ':
            yield 26
        else:
            one += message.pop(0)
            one = int(one)
            yield indexes[one]

caps += ' '
print ''.join(map(lambda x: caps[x], get_message()))
