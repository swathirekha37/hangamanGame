import random
WORDS=['lotus','lily','sunflower','jasmine','rose','cactus','lettus']

word=random.choice(WORDS)

hangarr=("""_________________""",
         """_________________
|
|
|
|
|
|
|""",
         """_______________
|      |
|      
|
|
|
|""",
         """______________
|       |
|       0
|
|
|
|
|""","""______________
|       |
|       0
|      /|\ 
|
|
|
|""","""______________
|       |
|       0
|      /|\ 
|       |
|
|
|""","""______________
|       |
|       0
|      /|\ 
|       |
|      /|\ 
|
|""")

WORDS=['lotus','lily','sunflower','jasmine','rose','cactus','lettus']
word=random.choice(WORDS)

print  ("The word is", len(word), "letters long.")# used to show how many letters are in the random word

ln = len(word)
guessed = dict.fromkeys(word, 0)
print " "
print " "
print('- '*ln)
correct=0
fail=0

for i in range(0,len(hangarr)+1):  #num of guesses

    letter=str(input("guess a letter"))

    if letter in word:
        print "{} is in the word ".format(letter)

        for i in word:
            if i==letter:
                correct=correct+1
                guessed[letter] = guessed[letter]+ 1

        if correct == ln:
            print "congrats you win the game! and the word is {}".format(word)
            break
    else:
        print "{} is not in word".format(letter)
        print hangarr[fail]
        fail=fail+1

    print(" ".join([ch if guessed[ch] else '- ' for ch in word]))
else:
    print "you lose and the word is {}".format(word)



