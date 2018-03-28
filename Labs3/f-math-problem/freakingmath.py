from random import *
from eval import *
import eval

def generate_quiz():
    x = randint(0, 10)
    y = randint(0, 10)
    op = choice(['+', '+', '-', '*'])
    res = eval.calc(x, y, op) + randint(-1,1)
    return [x, y, op, res]

def check_answer(x, y, op, result, user_choice):
    real = eval.calc(x, y, op)
    if result == real:
        if user_choice ==True:
            return True
        else:
            return False
    else:
        if user_choice == False:
            return True
        else:
            return False
