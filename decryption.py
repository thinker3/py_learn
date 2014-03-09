message = "012222 1114142503 0313012513 03141418192102 0113 2419182119021713 06131715070119"
keyed_alphabet = "BHISOECRTMGWYVALUZDNFJKPQX"
message = list(message)


def get_message():
    while message:
        one = message.pop(0)
        if one == ' ':
            yield ' '
        else:
            one += message.pop(0)
            one = int(one)
            yield keyed_alphabet[one]

print ''.join(get_message())
