name = str(input("Please enter your name. "))
print(f"Hello {name}!, Welcome to Guess Game")
print("INSTRUCTIONS\nPlease enter a name of Country that starts with letter N and matches what I have in mind.\nYou have 8 Guess.")
print("Good Luck")
country= str(input("Enter Country  "))
secret_word = "Norway"
num_of_guess= 7
total_guess = 0
while country != secret_word and total_guess <num_of_guess:
    total_guess = total_guess + 1
    country= str(input("Enter Country  "))
if country != secret_word and total_guess ==num_of_guess: 
    print("You're out of guesses\nYou Loose!")
if country == secret_word and total_guess <num_of_guess: 
    print(f"Congratulations\nYou win!")


