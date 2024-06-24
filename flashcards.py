#Possible future upgrades I'd like explore: 
    #Including the definition of the word in either the question or the answer
    #Including info in the answer about what part of it usually indicates feminine or masculine in the French language

import sys
import random

if len(sys.argv) < 2:
    print("Please supply a flash card file.")
    exit(1)

flashcard_filename = sys.argv[1]
f = open(flashcard_filename, "r")

question_dict = {}

for line in f:
    entry = line.strip().split(",")
    question = entry[0]
    answer = entry[1]
    question_dict[question] = answer

f.close()

print("Welcome to the flashcard quizzer.  You will be shown a French noun and asked if it is feminine or masculine.  Answer with 'f' or 'm'.")
print("At any time, type 'quit' to quit.")
print("")

questions = list(question_dict.keys())

while True:
    question = random.choice(questions)
    answer = question_dict[question]

    print("Question: Is " + question + " feminine or masculine?")
    user_input = input("Your guess: ")
    if user_input == "quit":
        print("Thanks for playing!  Au revoir!\nCredit for the original code goes to Jessica McKellar as part of her 'Introduction to Python' course at learning.oreilly.com.  Much gratitude goes to her for encouraging us to use this and adapt it.")
        break
    elif user_input == answer: #Entered correct answer
        if answer == "f": #Word is feminine
            for letter in question:
                if letter[0] in "aehiouy":
                    print("")
                    print("Correct! une " + question + ", l'" + question)
                    print("")
                    break
                else:
                    print("")
                    print("Correct! une " + question + ", la " + question)
                    print("")
                    break
        else: #Word is masculine
            for letter in question:
                if letter[0] in "aehiouy":
                    print("")
                    print("Correct! un " + question + ", l'" + question)
                    print("")
                    break
                else:
                    print("")
                    print("Correct! un " + question + ", le " + question)
                    print("")
                    break

    else: #Entered incorrect answer
        if answer == "f": #Word is feminine
            for letter in question:
                if letter[0] in "aehiouy":
                    print("")
                    print("Sorry, the answer was " + answer + ": une " + question + ", l'" + question)
                    print("")
                    break
                else:
                    print("")
                    print("Sorry, the answer was " + answer + ": une " + question + ", la " + question)
                    print("")
                    break
        else: #Word is masculine
            for letter in question:
                if letter[0] in "aehiouy":
                    print("")
                    print("Sorry, the answer was " + answer + ": un " + question + ", l'" + question)
                    print("")
                    break
                else:
                    print("")
                    print("Sorry, the answer was " + answer + ": un " + question + ", le " + question)
                    print("")
                    break

