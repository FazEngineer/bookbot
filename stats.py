def get_word_count(text):
    word = text.split()
    num_word = len(word)
    return num_word

def get_character_number(text):
    text = text.lower()
    char_count = {}
    for char in text:
        if char in char_count:
            char_count[char] = char_count[char] +1
        else:
            char_count[char] = 1
    return char_count

def sort_on(items):
    return items["num"]

def chars_dict_to_list(char_count):
    char_list = []
    for char in char_count:
        count = char_count[char]
        char_list.append({"char":char,"num": count})
    char_list.sort(reverse=True, key=sort_on)
    return char_list