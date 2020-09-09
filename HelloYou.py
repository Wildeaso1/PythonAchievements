print("Hello You!, Ik ben William!")
print("Wie ben jij?")

naam = input()
print("Hello,", naam)
print("Do you wanna play a game?")
print("Y/N")

answer = input()

if answer == "Y":
	print("Okay, Please choose a number between 1/4")
answer2 = input()

if answer2 == "1":
	print("No luck! Better luck next time!")
if answer2 == "2":
	print("You won a free pizza!")
if answer2 == "3":
	print("No luck! Better luck next time!")
if answer2 == "4":
	print("You won 100$!")
print("See you next time!", naam)

if answer == "N":
	print("Alright! Till next time!")