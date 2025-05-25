def get_num_words(text):
    words = text.split()
    return len(words)

def get_char_count(text):
    lower_text = text.lower()
    char_dict = {}
    for char in lower_text:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def get_sorted_chars(char_dict):
    listed_dict = list(char_dict.items())
    only_letters = []
    for char in listed_dict:
        if char[0].isalpha():
            only_letters.append(char)
    sorted_list = sorted(only_letters, reverse=True, key=lambda item: item [1])
    return sorted_list

    