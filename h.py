import random
WORDS= ("variable", "python", "turtle", "string", "loop")

word = random.choice(WORDS)#chooses randomly from the choice of words
print  ("The word is", len(word), "letters long.")# used to show how many letters are in the random word

ln = len(word)
guessed = dict.fromkeys(word, 0)
print guessed
print " "
print " "
print("_ "*ln)
correct = 0
for i in range(1, 9):#gives the amount of guesses allocated
    letter = input("Guess a letter ")

    if letter in word:
        print ("Correct! {} is in the word".format(letter))#if guesses letter is correct print correct
        guessed[letter] = 1
        correct += 1
        if correct == ln:
            print("Congratulations! you win.\n The word was {}".format(word))
            break
    else:
        print ("Incorrect! {} is not in the word".format(letter))
        #if its wrong print incorecct
    print(" ".join([ch if guessed[ch] else "_" for ch in word]))
else:
    print("You lose!\nThe word was {}".format(word))