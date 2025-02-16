#Sort them in ascending order of their lengths.
def word():
    words = ["apple", "banana", "cherry", "date", "fig"]
    sorted_words = sorted(words, key=lambda x:len(x))
    print(sorted_words)
word()