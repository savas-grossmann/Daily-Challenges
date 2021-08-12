
# Write a function that takes in a string of one or more words
# and returns the same string, but with all five or more letter words reversed


def reverse(sentence):
    reversed_sentence = []
    for word in sentence.split(" "):
        if len(word) >= 5:
            reversed_sentence.append(word[::-1])
        else:
            reversed_sentence.append(word)
    print(" ".join(reversed_sentence))


if __name__ == '__main__':
    reverse(input("Input your Sentence: "))
