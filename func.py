string = input("Enter any string: ")

def make_dict(d):
    dict = {}
    for x in d:
        dict[x] = 1 + dict.get(x, 0)
    return dict


def most_frequent(string):
    letters = [letter.lower() for letter in string if letter.isalpha()]
    dict = make_dict(letters)
    result = []
    for key in dict:
        result.append((dict[key], key))
    result.sort(reverse=True)
    for count, letter in result:
        print(letter, count)

most_frequent(string)