# --- Define your functions below! ---


# --- Put your main program below! ---

def greeting():
    print ("Hey there, I'm your local chat buddy")

def process_input(answer):
    if answer == "hi":
        #say a greeting
        say_greeting()
    elif answer == "say a poem":
        say_poem()
        print("")
        print("Did you like my poem?")
    elif answer == "yes":
        say_yes()
    elif answer == "what's the weather like?":
        say_weather()
    elif answer== "thanks":
        say_thanks()
    elif answer== "play rock paper scissors":
        playrockpaperscissors()
    else:
        say_default()

def say_greeting():
    print("hey")

def say_default():
    print("That's cool!")


def say_poem():
    print ("Roses are red, Violets are blue, Sugar is sweet, and so are you!")

def say_yes():
    print ( "Awesome!")

def say_weather():
    print ("Today is gonna be 70 degrees with a low of 55 degrees!")

def say_thanks():
    print("No problem")

def playrockpaperscissors():
    from random import randint
    t = ["Rock", "Paper", "Scissors"]
    computer = t[randint(0,2)]
    player = False
    while player == False:
        player = input("Rock, Paper, Scissors?")
        if player == computer:
            print("Tie!")
        elif player == "Rock":
            if computer == "Paper":
                print("You lose!", computer, "covers", player)
            else:
                print("You win!", player, "smashes", computer)
        elif player == "Paper":
                if computer == "Scissors":
                    print("You lose!", computer, "cut", player)
                else:
                    print("You win!", player, "covers", computer)
        elif player == "Scissors":
                    if computer == "Rock":
                        print("You lose...", computer, "smashes", player)
                    else:
                        print("You win!", player, "cut", computer)
        else:
            print("That's not a valid play. Check your spelling!")
            player = False
            computer = t[randint(0,2)]




def main():
    greeting()
    while True:
        answer = input("(What will you say?) ")
        process_input(answer)



# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
  main()
