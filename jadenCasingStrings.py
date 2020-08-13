#!/usr/bin/python3.7

def to_jaden_case(string):
    words = string.split()

    for x in range(len(words)):
        word = list(words[x])
        word[0] = word[0].upper()
        words[x] = ''.join(word)
    return ' '.join(words)
print(to_jaden_case("How can mirrors be real if our eyes aren't real"))
