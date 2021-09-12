def check_guess(guess, answer):
    global score
    still_guessing = True
    attempt = 0
    while still_guessing and attempt < 3:
        if guess.lower() == answer.lower():
            print("Correct Answer")
            score = score + 1
            still_guessing = False
        else:
            if attempt < 2:
                guess = input("Sorry Wrong Answer Try Again: ")
        attempt = attempt + 1
    if attempt == 3:
        print("Correct answer is " + answer)


score = 0
name = input("Enter Your Name: ")
print(f"Welcome {name} to Animal Quiz !! Let's Start")

guess0 =input("Which of the following is fish ? \n \
A)Whale\n B)Dolphin\n C)Shark\n D)Squid.\nType A,B,C, or D: ")
check_guess(guess0, 'C')
guess1 = input("Which Bear lives at North Pole?: ")
check_guess(guess1, 'Polar Bear')
guess2 = input("Which is the fastest land Animal? : ")
check_guess(guess2, 'Cheetah')
guess3 = input("Which is largest Animal?: ")
check_guess(guess3, 'Blue Whale')
guess4 = input("which Animal is called King of Forest?: ")
check_guess(guess4, 'Lion')
guess5 = input("Which is Tallest Animal?: ")
check_guess(guess5, 'Giraffe')


print("your Score is: " + str(score))
