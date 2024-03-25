def load_word_list(file_path):
    try:
        with open(file_path, 'r') as file:
            word_list = [line.strip() for line in file]
        return word_list
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return []
    