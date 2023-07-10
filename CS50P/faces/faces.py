
def main():
    user_input = input("Type me a message! smilies and frownies are cool. ")
    print(convert(user_input))

def convert(phrase):

    emojiKey = {
        '🙂' : ':)',
        '🙁' : ':(',
        ':)' : '🙂',
        ':(' : '🙁'
     }

    words = phrase.split()
    for i, word in enumerate(words):
        if word in emojiKey:
            words[i] = emojiKey[word]

    return ' '.join(words)


main()