# sys is a module. It lets us access command line arguments, which are
# stored in sys.argv.
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

print("Welcome to the flashcard quizzer.")
print("At any time, type 'quit' to quit.")
print("")

questions = list(question_dict.keys())

while True:
    question = random.choice(questions)
    answer = question_dict[question]

    print("Question: " + question)
    user_input = input("Your gender guess: f or m? ")
    if user_input == "quit":
        print("Thanks for playing! Au revoir.")
        break
    elif user_input == answer: #Entered correct answer
        if answer == "f": #Word is feminine
            for letter in question:
                if letter[0] in "aehiouy":
                    print("Correct! Une " + question + " or L'" + question)
                    print("")
                    break
                else:
                    print("Correct! Une " + question + " or La " + question)
                    print("")
                    break
        else: #Word is masculine
            for letter in question:
                if letter[0] in "aehiouy":
                    print("Correct! Un " + question + " or L'" + question)
                    print("")
                    break
                else:
                    print("Correct! Un " + question + " or Le " + question)
                    print("")
                    break

    else: #Entered incorrect answer
        if answer == "f": #Word is feminine
            for letter in question:
                if letter[0] in "aehiouy":
                    print("Sorry, the answer was: " + answer + ". Une " + question + " or L'" + question)
                    print("")
                    break
                else:
                    print("Sorry, the answer was: " + answer + ". Une " + question + " or La " + question)
                    print("")
                    break
        else: #Word is masculine
            for letter in question:
                if letter[0] in "aehiouy":
                    print("Sorry, the answer was: " + answer + ". Un " + question + " or L'" + question)
                    print("")
                    break
                else:
                    print("Sorry, the answer was: " + answer + ". Un " + question + " or Le " + question)
                    print("")
                    break

