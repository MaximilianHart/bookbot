def get_num_words(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        num_words = len(file_contents.split())
        print(f"{num_words} words found in the document")
