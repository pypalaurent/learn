from urllib.request import urlopen


def fetch_words():
    with urlopen('http://sixty-north.com/c/t.txt') as story:
        story_words = []
        for line in story:
            line_words = line.decode('utf-8').split()
            for words in line_words:
                story_words.append(words)

    for word in story_words:
        print(word)


if __name__ == '__main__':
    fetch_words()
