import sys


def get_word_count(text: str) -> int:
    words = text.split()
    return len(words)


def get_sorted_alpha_counts(text: str) -> list[tuple[str, int]]:
    char_dict = {}
    for char in text.lower():
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    sorted = []
    for char, count in char_dict.items():
        if char.isalpha():
            sorted.append((char, count))
    sorted.sort(reverse=True, key=lambda char_count: char_count[1])
    return sorted


def get_char_count_lines(char_counts: list[tuple[str, int]]) -> str:
    char_count_lines = ""
    for count in char_counts:
        char_count_lines += f"The '{count[0]}' character was found {count[1]} times\n"
    return char_count_lines


def get_report(path: str, word_count: int, char_counts: list[tuple[str, int]]) -> str:
    return f"--- Begin report of {path} ---\n{word_count} words found in the document\n\n{get_char_count_lines(char_counts)}--- End report ---"


def main() -> None:
    text_path = "books/frankenstein.txt"
    with open(text_path) as f:
        file_contents = f.read()
    word_count = get_word_count(file_contents)
    alpha_counts = get_sorted_alpha_counts(file_contents)
    print(get_report(text_path, word_count, alpha_counts))


if __name__ == "__main__":
    sys.exit(main())
