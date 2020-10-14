import random

def questions():
    name=input("What's your name: ")
    print("Hello there",name,"!")

    choice = random.choice("+-x/")
    finish = False
    questionnumber = 0
    correctquestions = 0

    while finish == False:
        if questionnumber < 10 | questionnumber >= 0:
            number1 = random.randint(1,10)
            number2 = random.randint(1,10)
            print((number1),(choice),(number2))
            answer=int(input("What is the answer?"))
            questionnumber = questionnumber + 1

            if choice==("+"):
                realanswer = number1+number2
                if answer == realanswer:
                    print("That's the correct answer")
                    correctquestions = correctquestions + 1
                else:
                    print("Wrong answer, the answer was",realanswer,"!")

            if choice==("x"):
                realanswer = number1*number2
                if answer==realanswer:
                    print("That's the correct answer")
                    correctquestions = correctquestions + 1
                else:
                    print("Wrong answer, the answer was",realanswer,"!")

            if choice==("-"):
                realanswer = number1-number2

                if answer==realanswer:
                    print("That's the correct answer")
                    correctquestions = correctquestions + 1
                else:
                    print("Wrong answer, the answer was",realanswer,"!")
        else:
            finish = True
    else:
            print("Good job",name,"! You have finished the quiz.")
            print("You scored " + str(correctquestions) + "/10 questions.")

questions()
