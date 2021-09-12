import random
import string

while True:
    adjectives =['sleepy', 'slow', 'smell y', 'wet', 'fat', 'red', 'orange', 'yellow']
    nouns =['apple', 'ball', 'goat', ' dragon', 'panda', 'duck']

    print("Welcome to Password Picker")

    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    number = random.randrange(0, 100)
    special_char = random.choice(string.punctuation)

    password = adjective + noun + str(number) + special_char
    print("Your New Password is: %s" % password)

    response = input("Would you like to another password? Type y or n: ")
    if response == 'n':
        break

print("Thanks for using password picker")
