from urllib.request import urlopen


# this fetches the words and returns them as a list
def fetch_words():
    with urlopen('http://sixty-north.com/c/t.txt') as story:
        story_words = []
        for line in story:
            line_words = line.decode('utf-8').split()
            for words in line_words:
                story_words.append(words)
        return story_words


# this prints a list of words
def print_items(items):
    for item in items:
        print(item)


def main():
    words = fetch_words()
    print_words(words)


if __name__ == '__main__':
    main()
