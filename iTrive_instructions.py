def show_instruction():
    print("|-------------------------------------------|")
    print("|        ==== Welcome to iTrive ====        |")
    print("|                                           |")
    print("|               Instructions                |")
    print("| 1- Choose # of players and enter names.   |")
    print("|    * 2 Min and 4 Max.                     |")
    print("| 2- There are 10 questions per game        |")
    print("|    * Each player starts with 10 pts       |")
    print("|    * Earn 2 pts per correct answer        |")
    print("|    * Loose 1 pt per wrong answer          |")
    print("| 3- Highest score after 10 questions win.  |")
    print("|                                           |")
    print("|           Enjoy the game! \U0001F60A              |")
    print("|-------------------------------------------|\n")


database = []
init_score = 10

def player_registration():
    name_entered = input("Enter your name to play: ").capitalize()
    if name_entered == "":
        print("You must enter a name to play")
    else:
        database.append(name_entered)
        print("Welcome", name_entered)
        print()
        return name_entered

questions_answers = ["""There are a lot of conspiracies floating around about the assassinations 
of Abraham Lincoln and John Kennedy. Which of the following things is NOT an eerie 
similarity between the two murders?
 a) Both were shot in a theater.\n b) Both had vice presidents named Johnson.\n c) Both were shot in the head on a Friday.\n d) Both were shot by Southern men in their 20s.\n""",
"""Kublai Khan's attempted conquests of Japan and King Philip II's 
attempted conquest of Britain failed for what reason?
 a) Having their own kingdoms invaded.\n b) Bad weather\n c) The deaths of their wives\n d) Plague\n""",
 """The Great Depression occurred when the stock market crashed in 1929. 
 However, previous to this event, there was another so-called 'Great Depression' 
 that began in 1873. By what name do we now refer to that first Great Depression?
 a) Short Depression\n b) Late Depression\n c) First Depression\n d) Long Depression\n""",
 """One of the more infamous examples of history repeating itself is when both 
 Napoleon and Hitler invaded which nation whose cold temperatures killed off 
 hundreds of thousands of soldiers each instance?\n a) Russia\n b) Canada \n c) England\n d) China""",
 """Barack Obama was not the first U.S. President whose detractors claimed he was born outside 
 of the United States. Which president was the first to have this claim made against 
 him when his opponents claimed he was born in Canada?.\n a) Teddy Roosevelt
 b) James Garfield\n c) Franklin Pierce\n d) Chester A. Arthur\n""",
 """In the United States, the red scares of the 20th century were often said 
 to be (then) modern-day versions of which event that occurred centuries earlier?
Arthur Miller wrote a play about it\n a) Teapot Dome Scandal\n b) Civil War\n c) Salem Witch Trials
 d) Nullification Crisis\n""",
"""Which of these Biblical places was the city where believers of Christ were 
first called Christians?\n a) Zion\n b) Galilee\n c) New York City\n d) Antioch\n""",
"""Where did Moses receive the ten commandments?\n a) Jordan River\n b) Nile River 
 c) Babylon\n d) Mount Sinai\n""",
"""Which of the following Biblical names means "light-bearer"?
 a) Aaron\n b) Saul\n c) Lucifer\n d) Satan\n""",
"""Which nationality describes a very dangerous game and a type of salad 
dressing often served on deli sandwiches?
 a) Mongolian\n b) Russian\n c) French\n d) Italian\n"""]

"""Which nationality could describe a dessert, a side dish, and a disease?
 a) German\n b) Russian\n c) Italian\n d) French\n
"""

correct_answers = {"Question 1" : "a", "Question 2" : "b", "Question 3" : "d",
  "Question 4" : "a", "Question 5" : "d", "Question 6" : "c" ,"Question 7" : "d" , 
  "Question 8" : "d" ,"Question 9" : "c", "Question 10" : "b"}    

def pick_question():
    player_score = init_score
    for counter, value in enumerate(questions_answers, start=1): 
        print ("Question",(counter),":",value)
        idx_select_question = questions_answers.index(value)
        if idx_select_question == 0:
            selected_answer = input("Enter your answer: ").lower()
            if selected_answer == correct_answers["Question 1"]:
                print("\nCorrect answer!👍👏")
                player_score += 2
                print("New score:", player_score, "points\n")
                input("Press enter to continue...")
                # return player_score
            else:
                print("\nIncorrect answer!👎")
                player_score -= 1
                print("New Score:", player_score, "points\n")
                input("Press enter to continue...")
                # return player_score
        
        if idx_select_question == 1:
            selected_answer = input("Enter your answer: ").lower()
            if selected_answer == correct_answers["Question 2"]:
                print("Correct answer!👍👏")
                player_score += 2
                print("Your score is", player_score, "points\n")
                input("Press enter to continue...")
                # return player_score
                
            else:
                print("\nIncorrect answer!👎")
                player_score -= 1
                print("New Score:", player_score, "points\n")
                input("Press enter to continue...")
                # return player_score

        if idx_select_question == 2:
            selected_answer = input("Enter your answer: ").lower()
            if selected_answer == correct_answers["Question 3"]:
                print("\nCorrect answer!👍👏")
                player_score += 2
                print("New score:", player_score, "points\n")
                input("Press enter to continue...")
                # return player_score
            else:
                print("\nIncorrect answer!👎")
                player_score -= 1
                print("New Score:", player_score, "points\n")
                input("Press enter to continue...")
                # return player_score

        if idx_select_question == 3:
            selected_answer = input("Enter your answer: ").lower()
            if selected_answer == correct_answers["Question 4"]:
                print("\nCorrect answer!👍👏")
                player_score += 2
                print("New score:", player_score, "points\n")
                input("Press enter to continue...\n")
                # return player_score
            else:
                print("\nIncorrect answer!👎")
                player_score -= 1
                print("New Score:", player_score, "points\n")
                input("Press enter to continue...\n")
                # return player_score

        if idx_select_question == 4:
            selected_answer = input("Enter your answer: ").lower()
            if selected_answer == correct_answers["Question 5"]:
                print("\nCorrect answer!👍👏")
                player_score += 2
                print("New score:", player_score, "points\n")
                input("Press enter to continue...\n")
                # return player_score
            else:
                print("\nIncorrect answer!👎")
                player_score -= 1
                print("New Score:", player_score, "points\n")
                input("Press enter to continue...\n")
                # return player_score

        if idx_select_question == 5:
            selected_answer = input("Enter your answer: ").lower()
            if selected_answer == correct_answers["Question 6"]:
                print("\nCorrect answer!👍👏")
                player_score += 2
                print("New score:", player_score, "points\n")
                input("Press enter to continue...\n")
                # return player_score
            else:
                print("\nIncorrect answer!👎")
                player_score -= 1
                print("New Score:", player_score, "points\n")
                input("Press enter to continue...\n")
                # return player_score

        if idx_select_question == 6:
            selected_answer = input("Enter your answer: ").lower()
            if selected_answer == correct_answers["Question 7"]:
                print("\nCorrect answer!👍👏")
                player_score += 2
                print("New score:", player_score, "points\n")
                input("Press enter to continue...\n")
                # return player_score
            else:
                print("\nIncorrect answer!👎")
                player_score -= 1
                print("New Score:", player_score, "points\n")
                input("Press enter to continue...\n")
                # return player_score

        if idx_select_question == 7:
            selected_answer = input("Enter your answer: ").lower()
            if selected_answer == correct_answers["Question 8"]:
                print("\nCorrect answer!👍👏")
                player_score += 2
                print("New score:", player_score, "points\n")
                input("Press enter to continue...\n")
                # return player_score
            else:
                print("\nIncorrect answer!👎")
                player_score -= 1
                print("New Score:", player_score, "points\n")
                input("Press enter to continue...\n")
                # return player_score

        if idx_select_question == 8:
            selected_answer = input("Enter your answer: ").lower()
            if selected_answer == correct_answers["Question 9"]:
                print("\nCorrect answer!👍👏")
                player_score += 2
                print("New score:", player_score, "points\n")
                input("Press enter to continue...\n")
                # return player_score
            else:
                print("\nIncorrect answer!👎")
                player_score -= 1
                print("New Score:", player_score, "points\n")
                input("Press enter to continue...\n")
                # return player_score

        if idx_select_question == 9:
            selected_answer = input("Enter your answer: ").lower()
            if selected_answer == correct_answers["Question 10"]:
                print("\nCorrect answer!👍👏")
                player_score += 2
                print("New score:", player_score, "points\n")
                input("Press enter to see your final score...\n")
                #return player_score
            else:
                print("\nIncorrect answer!👎")
                player_score -= 1
                input("Press enter to see your final score...\n")
                #return player_score

    print("Thank you for playing iTrive 🙏")
    print("Your final score is:", player_score)
    print("")
    

show_instruction()
player_registration()
pick_question()









"""
class QuestionAnswers:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer
    
    def pick_question(self):
        while len(questions_answers) > 0:
            for i, res in enumerate(questions_answers): 
                print ("Question",i,":",res)
                idx_select_question = questions_answers.index(res)
                select_answer = input("Enter your answer: ")
                if idx_select_question == 0 and select_answer == "a":
                    print("Correct answer!\n")
                    questions_answers.pop(idx_select_question)
                    answered_questions.append(res)
                    input("Press enter for the next question.")
                    continue
                else:
                    print("Invalid answer \n")
                    input("Press enter for the next question.")


    
    def pick_question(self):
        select_question = random.choice(questions_answers)
        print(select_question)
        questions_answers.pop(select_question)
        answered_questions.append(select_question)
        select_answer = input("Select your answer")
        #if select_answer == select_question.key():
        # new_list = list(questions_answers.items())
        # select_question = random.choice(new_list)
        # print(select_question)
        # selected_answered = input("Select an answer.")
        # if selected_answered ==  
    """


