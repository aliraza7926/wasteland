def normalize(text):
    text = text.replace(",", " ")
    text = text.replace("⁠", " ")
    text = text.replace(";", " ")
    text = text.replace(".", " ")
    text = text.replace("\"", " ")
    text = text.replace("?", " ")
    text = text.replace("\n"," ")
    text= text.replace("("," ")
    text = text.replace(")"," ")
    text = text.lower()

    return text


#
# f=open("wasteland.txt","r")
# poem=f.read()
# f.close()
#
# poem= normalize(poem)
# g=open("new.txt","w")
# g.write(poem)
# g.close()

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
    dict = {}
    all_words=text.split(" ")
    unique_wrods=set(text.split(" "))
    for word in unique_wrods:
        dict[word]=all_words.count(word)

    del dict["" ""]
    return dict

def answer3(text):
    dict = word_frequency(text)
    key = list(dict.keys())
    value= list(dict.values())
    f=open("out_most_frequent.txt","w")

    for i in range(1,11):
        f.write(str(i)+". "+key[value.index(max(value))]+"\t"+str(value[value.index(max(value))])+"\n")
        key.pop(value.index(max(value)))
        value.pop(value.index(max(value)))

    f.close()


f = open("wasteland.txt", "r")
poem = f.read()
f.close()

normalized_poem= normalize(poem)
answer1(normalized_poem)
answer3(normalized_poem)