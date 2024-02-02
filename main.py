def open_file(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    
    return file_contents

def count_words(file_contents):
    return len(file_contents.split())


def count_letters(file_contents):
    letter_count = dict()
    
    for word in file_contents.split():
        for letter in word.lower():
            if letter.isalpha():
                if letter not in letter_count:
                    letter_count[letter] = 0
                letter_count[letter] += 1

    letter_count = dict(sorted(letter_count.items(), key=lambda item: item[1], reverse=True))

    return letter_count

    

def main(path_to_file):
    file_contents = open_file(path_to_file)
    word_count = count_words(file_contents)
    print(f"--Begin report of {path_to_file} contents --")
    print(f"{word_count} words found in the document.\n")
    letter_count = count_letters(file_contents=file_contents)
    for k, v in letter_count.items():
        print(f"The '{k}' character was found {v} times")

    print("\n--- End of report ---")

if __name__ == "__main__":
    main("books/frankenstein.txt")
