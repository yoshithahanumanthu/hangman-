import random
 
with open('word.txt','r') as f:
    words=f.readlines()

word=random.choice(words)[:-1]

allowed_errors = 7
guesses = []
Done = False

while not Done:
    for letter in word:
        if letter.lower()  in guesses:
            print(letter, end=" ")
        else:
            print("_", end=" ")
    print("")  
    
            
        
    guess = input(f"Allowed Errors Left {allowed_errors}, Next Guess: ")
    guesses.append(guess.lower())
    if guess.lower() not in word.lower():
        allowed_errors -= 1
        if allowed_errors == 0:
            break


    Done = True
    for letter in word:
        if letter.lower() not in guesses:
            Done = False

if Done:
    print(f"You found the word! it was {word}!")
else:
    print(f"Game Over! The word was {word}!")
        
