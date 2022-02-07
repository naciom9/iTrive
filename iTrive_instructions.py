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
    name_entered = input("Enter your name to play: ")
    if name_entered == "":
        print("You must enter a name to play")
    else:
        database.append(name_entered)
        print("Welcome", name_entered)
        print()

"""
# Player login 
def login(database, player_name):
    if player_name not in database:
        print("You must be register to play")
        return ""
    elif database[player_name] == "":
        print("Welcome", player_name)
        return player_name

# Player registration
def registration(database, player_name):
    if player_name in database:
        print("Name already exist. Enter a different name")
        return ""
    else:
        print(player_name, "has been registered")
        return player_name

"""

# # Dictionary with another dictionary representing the value of the keys. 
# questions_answers = {"""There are a lot of conspiracies floating around about the assassinations
#                     of Abraham Lincoln and John Kennedy. Which of the following things is NOT an eerie 
#                     similarity between the two murders?""" : 
#                     {"a)" : "Both were shot in a theater", "b)" : "Both had vice presidents named Johnson",
#                     "c)" : "Both were shot in the head on a Friday", "d)" : "Both were shot by Southern men in their 20s."},
#                     """Kublai Khan's attempted conquests of Japan and King Philip II's attempted conquest of 
#                     Britain failed for what reason?""" : 
#                     {"a)" : "Having their own kingdoms invaded", "b)" : "Bad weather", "c)" : "The deaths of their wives", 
#                     "d)" : "Plague"}
#                     }

# correct_answers = {"""There are a lot of conspiracies floating around about the assassinations
#                     of Abraham Lincoln and John Kennedy. Which of the following things is NOT an eerie 
#                     similarity between the two murders?""" : "a",
#                     """Kublai Khan's attempted conquests of Japan and King Philip II's attempted conquest of 
#                     Britain failed for what reason?""" : "b"
#                   }

questions_answers = ["""There are a lot of conspiracies floating around about the assassinations 
of Abraham Lincoln and John Kennedy. Which of the following things is NOT an eerie 
similarity between the two murders?\n
 a) Both were shot in a theater.\n b) Both had vice presidents named Johnson.\n c) Both were shot in the head on a Friday.\n d) Both were shot by Southern men in their 20s.\n""",
"""Kublai Khan's attempted conquests of Japan and King Philip II's 
attempted conquest of Britain failed for what reason?\n
 a) Having their own kingdoms invaded.\n b) Bad weather\n c) The deaths of their wives\n d) Plague\n"""]          

#authorized_player = ""

def pick_question():
    while len(questions_answers) > 0:
        for count, value in enumerate(questions_answers, start=1): 
            print ("Question",(count),":",value)
            idx_select_question = questions_answers.index(value)
            player_score = init_score
            if idx_select_question == 0:
                selected_answer = input("Enter your answer: ")
                if selected_answer == "a":
                    print("\nCorrect answer!")
                    player_score += 2
                    print("New score:", player_score, "points\n")
                    input("Press enter for the next question.")
                    # return player_score
                else:
                    print("\nIncorrect answer!")
                    player_score -= 1
                    print("New Score:", player_score, "points\n")
                    input("Press enter for the next question.")
                    # return player_score
                    
            
            if idx_select_question == 1:
                selected_answer = input("Enter your answer: ")
                if selected_answer == "b":
                    print("Correct answer!")
                    player_score += 2
                    print("Your score is", player_score, "points\n")
                    input("Press enter for the next question.")
                    # return player_score
                    
                else:
                    print("\nIncorrect answer ")
                    player_score -= 1
                    print("New Score:", player_score, "points\n")
                    input("Press enter for the next question.")
                    # return player_score


"""
def score_tracker(player_name):
    while player_name is True:
        player_name == my_score
        if correct_answer is True:
            correct_answer = player_init_score + correct_answer
            print("New score:", correct_answer)
            return correct_answer
        elif incorrect_answer is True:
            incorrect_answer = player_init_score - incorrect_answer
            print("New score:", incorrect_answer)
            return incorrect_answer

"""



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


