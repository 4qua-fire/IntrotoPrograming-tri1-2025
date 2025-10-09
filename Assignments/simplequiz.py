print("Welcome to the best quiz ever!")
score=0
#questions
q1=input("Question 1:\nwhat is the population of New Orleans as of october 8th 2025?\n>")
q2=input("Question 2:\nWho is the prime minister of Italy?\n>")
q3=input("Question 3:\nWhat is the derivitive of 3x^2+3x-2?\n>")
q4=input("Question 4:\nHow many years did the Ottomon Empire rule?\n>")
q5=input("Question 5:\nhow many sqaure millimiters is an A4 size piece of paper?\n>")
q6=input("Question 6:\nWhat year was the NBA founded?\n>")
q7=input('Question 7:\nwhat is the third word of "I See A Dreamer" by CG5? \n>')
q8=input("Question 8:\nHow old was George Boole when he died?\n>")
q9=input("Question 9:\nWhat is 1287523 in binary?\n>")
q10=input("Question 10:\nWhat is the 3141th digit of pi?\n>")

def tally_score():
    global score
    if q1 == "362,701":
        score= score+1
        print("\nquestion 1: correct")
    else:
        print(f"question 1: incorrect\nYour answer:{q1} correct answer: 362,701")
    
    if q2.lower == "giorgia meloni" or "jogn poep":
        score=score+1
        print("question 2: correct")
    else:
        print(f"question 2: incorrect\nYour answer:{q2} correct answer: Giorgia Meloni")
    
    if q3 == "6x+3":
        score=score+1
        print("question 3: correct")
    else:
        print(f"question 3: incorrect\nYour answer:{q3} correct answer: 6x+3")
    
    if q4 == "600":
        score=score+1
        print("question 4: correct")
    else:
        print(f"question 4: incorrect\nYour answer:{q4} correct answer: 600")
    
    if q5 == "62370":
        score=score+1
        print("question 5: correct")
    else:
        print(f"question 5: incorrect\nYour answer:{q5} correct answer: 62370")
    
    if q6 == "1946":
        score=score+1
        print("question 6: correct")
    else:
        print(f"question 6: incorrect\nYour answer:{q6} correct answer:  1946")
    
    if q7.lower == "wind":
        score=score+1
        print("question 7: correct")
    else:
        print(f"question 7: incorrect\nYour answer:{q7} correct answer: wind")
    
    if q8 == "49":
        score=score+1
        print("question 8: correct")
    else:
        print(f"question 8: incorrect\nYour answer:{q8} correct answer: 49")
    
    if q9 == "100111010010101100011":
        score=score+1
        print("question 9: correct")
    else:
        print(f"question 9: incorrect\nYour answer:{q9} correct answer: 100111010010101100011")
    
    if q10 == "4":
        score=score+1
        print("question 10: correct")
    else:
        print(f"question 10: incorrect\nYour answer:{q10} correct answer: 4")

tally_score()
print(f"\nFinal score: {score}")

#retake
if score <=5:
    print("you absolute trash bozo\nYou absolute failure\nyou couldn't even pass\n")
    retake = input('A retake exam is available for losers\ntype "yes" or "no" to continue\n>')
    if retake == "yes":
        score=0
        #retake questions
        rq1=input("Question 1:\nWhat is the population of olympia?\n>")
        rq2=input("Question 2:\nWho is the prime minister of New Zealand?\n>")
        rq3=input("Question 3:\nWhat is the derivite of 19x^2-14x+12?\n>")
        rq4=input("Question 4:\nHow many years did the Mongol Empire rule?\n>")
        rq5=input("Question 5:\nHow many square millimiters is lettersized paper?\n>")
        rq6=input("Question 6:\nWhat year was the NFL founded?\n>")
        rq7=input('Question 7:\nWhat is the 7th word of "the moss" by Cosmo Sheldrake?\n>')
        rq8=input("Question 8:\nHow old was christopher columbus when he died\n>")
        rq9=input("Question 9:\nWhat is 924586 in binary?\n>")
        rq10=input("Question 10:\nWhat is the 1618th digit of phi?\n>")
       
       #retake tally score
        def retally_score():
            global score
            if rq1 == "56,271":
                score = score+1
                print("\nquestion 1: correct")
            else:
                print(f"question 1: incorrect\nYour answer:{rq1} correct answer: 56,271")

            if rq2.lower == "christopher luxon" or "jogn poep":
                score=score+1
                print("question 2: correct")
            else:
                print(f"question 2: incorrect\nYour answer:{rq2} correct answer: Christopher Luxon")

            if rq3 == "38x-14":
                score=score+1
                print("question 3: correct")
            else:
                print(f"question 3: incorrect\nYour answer:{rq3} correct answer: 38x-14")

            if rq4 == "132":
                score=score+1
                print("question 4: correct")
            else:
                print(f"question 4: incorrect\nYour answer:{rq4} correct answer: 132")

            if rq5 == "60264":
                score=score+1
                print("question 5: correct")
            else:
                print(f"question 5: incorrect\nYour answer:{rq5} correct answer: 60264")

            if rq6 == "1920":
                score=score+1
                print("question 6: correct")
            else:
                print(f"question 6: incorrect\nYour answer:{rq6} correct answer: 1920")

            if rq7.lower == "grows":
                score=score+1
                print("question 7: correct")
            else:
                print(f"question 7: incorrect\nYour answer:{rq7} correct answer: grows")

            if rq8 == "55":
                score=score+1
                print("question 8: correct")
            else:
                print(f"question 8: incorrect\nYour answer:{rq8} correct answer: 55")

            if rq9 == "11100001101110101010":
                score=score+1
                print("question 9: correct")
            else:
                print(f"question 9: incorrect\nYour answer:{rq9} correct answer: 11100001101110101010")

            if rq10 == "2":
                score=score+1
                print("question 10: correct")
            else:
                print(f"question 10: incorrect\nYour answer:{rq10} correct answer: 2")

            print(f"\nFinal score: {score}")
        
        retally_score()    
        if score >6:
            print("Wow\nso cool\nyou managed to pass the retake")
        else:
            print("im dissapointed you couldnt even pass the retake")   
