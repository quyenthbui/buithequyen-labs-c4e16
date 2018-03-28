from random import choice
#
# x = 3
#
# op = choice(['+','-','*','/'])
#
# y = 7
#
# result = 9999
#
# if op == '+':
#     result = x+y
# elif op == '-':
#     result = x-y
# elif op == '*':
#     result = x*y
# elif op == '/':
#     result = x*y
#
# print(result)

def calc(x, y, op):
    if op == '+':
        result = x+y
    elif op == '-':
        result = x-y
    elif op == '*':
        result = x*y
    elif op == '/':
        result = x/y

    return result
# argument, parameter

# res = calc(3,7,'+')
# print(res)
#
# r = calc(1,2,'-')
# print(r)

#ops = ['+','-','*','/']
#op = choice(ops)


#calc(1,2,'-')
