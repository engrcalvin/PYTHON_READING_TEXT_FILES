
def read_file_content(filename):
    with open(filename) as f:
        contents = f.read()
    return contents


def count_words():
    text = read_file_content("./story.txt")
    words = text.split()
    myDict = {}
    for key in words:
        myDict[key] = words.count(key)

    return myDict


print(count_words())