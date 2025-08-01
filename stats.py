letters_dict = {}
sorted_dicts = []
new_dict = {}


def get_num_words(file_path):
    print("----------- Word Count ----------")
    with open(file_path) as f:
        file_contents = f.read()
        num_words = len(file_contents.split())
        print(f"Found {num_words} total words")


def get_letters(file_path):
    with open(file_path) as f:
        file_contents = str.lower(f.read())
    for key in file_contents:
        if key not in letters_dict:
            letters_dict[key] = 1
        else:
            letters_dict[key] += 1
    return letters_dict


def sort_on(items):
    return items["num"]


def sort_dict():
    print("--------- Character Count -------")
    for char in letters_dict:
        if char.isalpha():
            num = letters_dict[char]
            sorted_dicts.append({"char": char, "num": num})
    sorted_dicts.sort(reverse=True, key=sort_on)
    for dict in sorted_dicts:
        char = dict["char"]
        num = dict["num"]
        print(f"{char}: {num}")
