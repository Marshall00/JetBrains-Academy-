import random
global guess_counter

print('H A N G M A N\n')

list_of_words=['python', 'java', 'kotlin', 'javascript']
picked_word = (random.sample(list_of_words, 1))[0]

guess_counter = 8
already_picked = []
picked_word_set = set(picked_word)
hidden_picked_word = '-' * len(picked_word)

action = input('Type "play" to play the game, "exit" to quit:')

while action != "play":
    continue
else:
    while 0 < guess_counter <= 8 and action == 'play':

        if hidden_picked_word == picked_word:
            print(picked_word)
            print('You guessed the word!')
            print('You survived!')
            break

        else:
            print(hidden_picked_word)
            letter_guess = input('Input a letter: ')

            if letter_guess in already_picked:
                print('You already typed this letter\n')
                continue

            else:
                if len(letter_guess) == 1:
                    if letter_guess.isalpha() and letter_guess.islower():
                        if letter_guess in picked_word_set:
                            already_picked.append(letter_guess)
                            for i in range(len(picked_word)):
                                if picked_word[i] == letter_guess:
                                    hidden_picked_word_list = list(hidden_picked_word)
                                    hidden_picked_word_list[i] = letter_guess
                                    hidden_picked_word = "".join(hidden_picked_word_list)
                                    print()
                                else:
                                    continue

                        elif letter_guess not in picked_word_set and letter_guess not in already_picked:
                            if guess_counter == 1:
                                print('No such letter in the word')
                                print('You are hanged!\n')
                                action = input('Type "play" to play the game, "exit" to quit:')
                                break
                            else:
                                print('No such letter in the word\n')
                                already_picked.append(letter_guess)
                                guess_counter -= 1
                                continue

                        elif letter_guess in already_picked:
                            print('You already typed this letter\n')
                            continue

                    else:
                        print('It is not an ASCII lowercase letter\n')
                        continue
                else:
                    print('You should input a single letter\n')
                    continue

