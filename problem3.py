import random 
def guess_the_correct_word_game():
    words=["book","grapes","banana","car"]
    word = random.choice(words)
    intermittent_word = "".join(random.sample(word,len(word)))
    attempts = 5
    print("Welcome to the game of guessing the correct word")
    print("try to guess the correct word from this word: " , intermittent_word)
    while attempts > 0:
        guessing = input("Enter Your Guessing: ")
        if guessing == word:
            print("Congratulation , you guessed the correct word")
            break
        else:
            attempts -= 1
            print("Incorrect,try again. you have %d attempts left" %attempts)
    if attempts == 0:
        print("Ohh , you lost . the correct word is: %s" %word)   
guess_the_correct_word_game()             