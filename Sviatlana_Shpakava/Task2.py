def most_common_words(file):
    common_words = {}
    file = open("lorem_ipsum.txt", "r")
    for line in file.readlines():
        for word in line.strip().split():
            if word not in common_words:
                common_words[word] = 0
            common_words[word] += 1
            n = dict(zip(common_words.values(), common_words.keys()))
        file.close()
    return sorted(n.items())[-3:]

print(most_common_words("lorem_ipsum.txt"))
