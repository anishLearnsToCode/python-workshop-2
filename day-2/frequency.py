def frequency(sentence):
    words = {}
    sentence = sentence.split(' ')
    for word in sentence:
        if word in words:
            words[word] += 1
        else:
            words[word] = 1

    if '' in words:
        del words['']
    return words


sentence = input()
print(frequency(sentence))
