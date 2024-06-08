import sys


def get_word_count(text: str) -> int:
    words = text.split()
    return len(words)


def get_char_counts(text: str) -> dict[str, int]:
    char_dict = {}
    for char in text.lower():
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1
    return char_dict


def main() -> int:
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    print(get_word_count(file_contents))
    print(get_char_counts(file_contents))


if __name__ == "__main__":
    sys.exit(main())
