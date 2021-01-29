def normalize(text):
    text = text.replace(",", " ")
    text = text.replace("⁠", " ")
    text = text.replace(";", " ")
    text = text.replace(".", " ")
    text = text.replace("\"", " ")
    text = text.replace("?", " ")
    text = text.replace("\n", " ")
    text = text.replace("(", " ")
    text = text.replace(")", " ")
    text = text.replace("!", " ")
    text = text.lower()

    return text


def count_all_words(text):
    return len(text.split(" "))


def count_words(text):
    return len(set(text.split(" ")))


def answer1(text):
    f = open("out_words_count.txt", "w")
    f.write(str(count_all_words(text)))
    f.write("\n")
    f.write(str(count_words(text)))
    f.close()


def word_frequency(text):
    my_dict = {}
    all_words = text.split(" ")
    unique_wrods = set(text.split(" "))
    for word in unique_wrods:
        my_dict[word] = all_words.count(word)

    del my_dict["" ""]
    return my_dict


def answer3(text):
    my_dict = word_frequency(text)
    key = list(my_dict.keys())
    value = list(my_dict.values())
    f = open("out_most_frequent.txt", "w")

    for i in range(1, 11):
        f.write(str(i) + ". " + key[value.index(max(value))] + "\t" + str(value[value.index(max(value))]) + "\n")
        key.pop(value.index(max(value)))
        value.pop(value.index(max(value)))

    f.close()


def answer4(text):
    my_dict = word_frequency(text)

    new_dict = {}
    for i in range(1, 6):
        max_length = 0
        max_key = ""
        for key in my_dict:
            if (len(key) > max_length):
                max_key = key
                max_length = len(key)

        new_dict[max_key] = my_dict[max_key]
        del my_dict[max_key]

    return new_dict


def normalize_for_q5(text):
    text = text.replace(",", " ")
    text = text.replace("⁠", " ")
    text = text.replace(";", " ")
    text = text.replace(".", " ")
    text = text.replace("\"", " ")
    text = text.replace("?", " ")
    text = text.replace("\n", " ")
    text = text.replace("(", " ")
    text = text.replace(")", " ")
    text = text.replace("!", " ")

    return text


def is_capital(text):
    if (text != '' and text != " "):
        return text[0].isupper()
    else:
        return False


def find_capital_words(text):
    my_dict = {}
    all_words = text.split(" ")
    unique_wrods = set(text.split(" "))
    for word in unique_wrods:
        if (is_capital(word)):
            my_dict[word] = all_words.count(word)

    return my_dict


def answer5(text):
    normalized_text = normalize_for_q5(text)
    my_dict = find_capital_words(normalized_text)
    f = open("out_capital_words.txt", "w")

    for key in my_dict:
        f.write(key + " (" + str(my_dict[key]) + ")\n")

    f.close()


f = open("wasteland.txt", "r")
poem = f.read()
f.close()

normalized_poem = normalize(poem)
answer1(normalized_poem)
answer3(normalized_poem)
answer4(normalized_poem)
answer5(poem)
