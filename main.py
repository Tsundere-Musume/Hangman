from dictionary import diction


def game(string):
    print('1.Hard\n2.Medium\n3.Easy')
    level = [3, 5, 7]
    while True:
        selected_mode = int(input('Choose your difficulty: '))
        if selected_mode == 1:
            chances = level[0]
            print(f'you have {chances} chances')
            break
        elif selected_mode == 2:
            chances = level[1]
            print(f'you have {chances} chances')
            break
        elif selected_mode == 3:
            chances = level[2]
            print(f'you have {chances} chances')
            break
        else:
            print('Choose a fucking mode from above')
    database = diction(chances)
    base_word = string.upper()
    p = "_" * len(base_word)
    blank = list(p)
    word = list(base_word)
    duplicate = []

    # Adds spaces if any in 'blank' if any in 'string'
    for space in range(len(word)):
        if word[space] == ' ':
            blank[space] = ' '
    a = ''.join(blank)
    print(a)
    count = 0

    while True:
        # To prevent duplicate guesses
        while True:
            guess = input('Guess: ').upper()
            if guess not in duplicate:
                break
            else:
                print(f'You have already guessed {guess}')
        duplicate.append(guess)
        for i in range(len(word)):
            # Fills in the blank
            if guess == word[i]:
                blank[i] = guess
            # Dying message
            elif guess not in word:
                count += 1
                print(database[count])
                break
            a = ("".join(blank))
        print(a)
        if a == base_word:
            print(f'!!!!CONGRATULATIONS YOU WON!!!!')
            break
        if count == chances:
            print('--------------------You no longer alive mate---------------------')
            print(f'-----------------------YOU FUCKING LOSE------------------------')
            break


game("Hello darkness my old friend")
