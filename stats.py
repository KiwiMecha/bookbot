def num_words(output):
    return len(output.split())

def char_count(output):
    char = {}
    for i in output:
        i = i.lower()
        if i in char:
            char[i] += 1
        else:
            char[i] = 1
    return char

def sort_num(count):
    return count["num"]

def sorted_num(char):
    sorting = []
    for letter in char:
        sorting.append({"char": letter, "num": char[letter]})
    sorting.sort(reverse = True, key = sort_num)
    return sorting
