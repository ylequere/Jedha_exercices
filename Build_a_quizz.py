# -*- coding: utf-8 -*-
"""
Created on Sat Sep 24 13:33:45 2022

@author: ylequ
"""

def answer_a_question(question, answer, lives):

    good_answer = False
    while (not good_answer) and (lives > 0):
        user_answer = input(question)
        # print("Your answer :", user_answer)
        
        if user_answer.lower() != user_answer:
            print('Your answer after .lower() function :', user_answer.lower())
            
        if answer  == user_answer.lower():
            good_answer = True
            print(f'Congrats {answer} is the right answer !')
        else:
            lives -= 1
            print(lives)
            print(f'Sorry, you have {lives} chances left')
    return lives
        
questions_answers= {"What is my birthday year ? " : "1971",
                    "How many children do I have ? " : "2",
                    "Who is the richest man in the world ? ": "elon musk"
                    }

user_lives = 3
print(f'Welcome to our quizz!\nYou have {user_lives} lives.')

for i, qa in enumerate(questions_answers.items()):
    print(f'\nQuestion {i+1}')
    user_lives = answer_a_question(qa[0], qa[1], user_lives)
    if user_lives == 0:
        print ("Too bad, you lost the game !")
        break

if user_lives > 0:
    print('Well done! You are the quizz winner!')
 