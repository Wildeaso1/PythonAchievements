print('Welcome new player. Would you like to generate a new character?')
print('Answer with Y/N')

answer = input()

if answer == "Y":
	print('Good. Please choose a name.')

your_name = input()

print('Welcome', your_name)
print('Generating your character')
print('Please enter a name for your character.')

character_name = input()

import random

x = random.randint(0,1000)
power = ["Super Speed", "Teleportation", "Fly", "Light", "Darkness"]
speed = random.randint(0,1000)
level = random.randint(0,10000)
Weapon = ["Spear", "Katana", "Double Katana", "Martial Arts", "Magic Only", "Holy Katana", "Holy Spear"]
MagicPower = random.randint(0,1000)
randomWeapon = random.choice(Weapon)
Wanted = ["Yes", "No"]
Rep = ["Holy Knight", "Hero", "Good Person", "Neutral", "Bad Person", "Evil", "Vilain"]
HP = random.randint(0,10000)


print('Name:', character_name)
print('Strength:' + str(x))
print('Power:' + random.choice(power))
print('Speed:' + str(speed))
print('Level:' + str(level))
print('Weapon:' + randomWeapon )
print('Magic Power:'+ str(MagicPower))
print('Wanted:' + random.choice(Wanted))
print('Reputation: ' + random.choice(Rep))
print('HP: ' + str(HP))

print('Please enjoy your character! ' + your_name)

