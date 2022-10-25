from distutils import text_file


def word_count(str):
    counts = dict()
    text_list = str.split()

    for word in text_list:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

print( word_count('the quick brown fox jumps over the lazy dog.'))
