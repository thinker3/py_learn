import string
message = "012222 1114142503 0313012513 03141418192102 0113 2419182119021713 06131715070119"
keyed_alphabet = "BHISOECRTMGWYVALUZDNFJKPQX"
message = list(message)
caps = string.letters[26:]

ans = ''
while message:
    one = message.pop(0)
    if one == ' ':
        ans += one
    else:
        one += message.pop(0)
        char = caps[int(one)]
        i = keyed_alphabet.index(char)
        ans += caps[i]
print ans
