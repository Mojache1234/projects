__author__ = 'Ariel =)'
import random
wordlist = {}
while True:
    (x, y) = (input('Type in a word: ').upper(), input('Type in a clue: '))
    if (x, y) == ('', ''):
        break
    wordlist[x] = y
(words, correct, incorrect, overall_score, out_of) = (list(wordlist.keys), [], [], 0, 5 * len(wordlist.keys))
while len(words):
    word = words[random.randint(0, len(words) - 1)]
    (answers, guesses, score) = (('_ ' * len(word)).split(' ')[:-1], [], 5)
    print(f' New round! You have {score} guesses. '.center(75, '=') + '\n' + answers + '\n\n' + 'Clue: ' + wordlist[word])
while '_' in answes:
    print('Guess letter? ')
    guess = input()[0].upper()
    if guess in guesses:
        print('You\'ve already guessed ', guess, '!')
    elif guess in [chr(i) for i in range(65, 91)]:
        guesses.append(guess)
        times = 0
