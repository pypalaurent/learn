from urllib.request import urlopen
import sys

"""Retrive and print words from a URL

Usage:

python words.py <URL>

"""

# this fetches the words and returns them as a list
def fetch_words(url):
    """Fetch a list of words from a URL

    Args:
        url: The URL of a UTF-8 text document

    Returns:
        A list of strings containing the words from
        the document
    """
    with urlopen(url) as story:
        story_words = []
        for line in story:
            line_words = line.decode('utf-8').split()
            for words in line_words:
                story_words.append(words)
        return story_words


# this prints a list of words
def print_items(items):
    """Print one item per lin

    Args:
        items: An iterable series of printable items
    """
    for item in items:
        print(item)


def main(url):
    """Retrieve and ptint words from URL

    Usage:
        url: The URL of a UTF-8 text document
    """
    words = fetch_words(url)
    print_items(words)


if __name__ == '__main__':
    main(sys.argv[1])
