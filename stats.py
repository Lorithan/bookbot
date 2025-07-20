

def get_num_words(contents):
    """Get the number of words"""
    return len(contents.split())


def get_num_chars(contents):
    char_dict = {}
    for c in contents.lower():
        if c in char_dict:
            char_dict[c] += 1
        else:
            char_dict[c] = 1

    return char_dict


def get_sorted_chars(char_dict):
    chars = []
    for key, value in char_dict.items():
        chars.append({"char": key, "num": value})

    chars.sort(reverse=True, key= lambda item: item["num"])
    return chars