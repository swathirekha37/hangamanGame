import random
words=['lotus','lily','sunflower','jasmine','rose','cactus','lettus']

compword=random.choice(words)

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

count=0
while count<len(hangarr):
    guess=str(input("enter the guessing alphabet: "))
    j=0
    for i in compword:
        if i==guess:
            print i
        count=count+1
        if i!=guess:
            print hangarr[j]
            j=j+1
            count=count+1
