def palindrome(word):
    word = word.replace(' ','')
    word = word.lower()
    word_inverted = word[::-1]
    if word == word_inverted:
        return True
    else:
        return False


def run():
    word = input ('write a word: ')
    is_palindrome = palindrome (word)
    if is_palindrome == True:
        print (word,' is a palindrome')
    else:
        print (word, ' is not a palindrome')


if __name__ == '__main__':
    run()