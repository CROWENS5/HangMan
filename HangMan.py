secretWord = input('WORD:')
print(secretWord)
# it can only be one word 
letters = [letters for letters in secretWord]
print(letters) # prints out letters in a string in a list

lives = 5

length_Limit = len(secretWord)

correct_lst = []
def playgame():
    if length_Limit > 10:
         print("This program will not run the word is to long")
while True:
    letterGuess1 = input("LETTER:")
    if letterGuess1 in secretWord:
        print("correct")
        correct_lst.append(letterGuess1)
    if not letterGuess1 in secretWord:
            print("This selection is wrong")
            lives -= 1
            print("You have " + str(lives) + " left")
            if lives == 0:
                 print("You Lose")
                 break
    if correct_lst == letters:
        print("You have won")
        break
        

    
