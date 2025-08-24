#Random code generator
import random

def code_generator():
    global code
    code = ""
    choice = [random.choice([x for x in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]),random.choice([x for x in "abcdefghijklmnopqrstuvwxyz"]),random.choice([x for x in "1234567890"]),random.choice([x for x in "@#$%^&*!|"])]
    for i in range(len(choice)):
        code_initial = random.choice(choice)
        code += code_initial
        choice.remove(code_initial)

times = int(input("How many code blocks [ 1 block  = 4 characters ]: "))
code_final = ""
for i in range(times):
    code_generator()
    code_final += code
print("Code Generated :",code_final)
