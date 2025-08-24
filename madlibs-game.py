# A simple mad libs game
import random

def madlib1():
    name = input('Name: ')
    terrify = input('Dangerous Creature name: ')
    loc1 = input('Location: ')
    loc2 = input('Another Location: ')
    sound = input('Sound: ')
    print('Story')
    print(f'''
          His name was {name} and he was terrified of {terrify}. One day he was in the {loc1}, returning to {loc2} when he heard a {sound} behind him,
          he looked back and saw {terrify} standing there. He {sound} and ran towards {loc2} but the {terrify} ate him in no time.
          ''')

def madlib2():
    name = input('Name: ')
    job = input('Job: ')
    age = input('Age: ')
    relative = input('Relative: ')
    loc1 = input('Location: ')
    weapon = input('Weapon: ')
    gesture = input('Gesture: ')
    print('Story')
    print(f'''
          She was a {job} when she was {age}. One day she was doing her {job} when her {relative} came to see her in her {loc1} (She used to work in the {loc1}).
          They greeted her and talked to her when they suddenly pulled a {weapon} and killed her. Then they called her name {name} and {gesture} on it.
         ''')

choice = random.choice([1, 2])
if choice == 1:
    madlib1()
elif choice == 2:
    madlib2()
