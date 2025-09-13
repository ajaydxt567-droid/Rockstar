import Art
print(Art.logo)
value=True
print("Welcome to the number Guessing game! : ")
print(" I am Thinking of a number between 1 to 100 ")
attempts=0
password= 47
level=input("Choose the difficulty level: ").lower()

if level=="hard":
    attempts=5
elif level=="easy":
    attempts=10
value=attempts
def trigger():
    if value>0:
        return True
while trigger():
    print(f"you have {attempts} attempts.")
    input_number = int(input("input your number: "))
    if level == "hard":
        attempts-=1
        if attempts <= 0:
            print("you lose the game!")
            value=False
        elif attempts > 0:
            if password < input_number:
                print("Number too high")

            elif password > input_number:
                print("Number too low")

            else:
                print("You won the game!")
                value=False

    elif level== "easy":
        attempts-=1
        if attempts ==0:
            print("you lose the game!")
            value=False
        elif attempts > 0:
            if password < input_number:
                print("Number too high")

            elif password > input_number:
                print("Number too low")

            else:
                print("You won the game!")
                value= False



